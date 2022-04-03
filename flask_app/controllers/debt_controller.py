from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app
from flask_app.models.lender import Lender
from flask_app.models.borrower import Borrower
from flask_app.models.debt import Debt


@app.route("/lendMoney", methods=["POST"])
def lendMoney():
    if("user_id" not in session or "lender" not in session):
        return redirect("/")

    data = {"id": session["user_id"]}
    lender = Lender.get_by_id(data)
    data = {"id": request.form["borrower_id"]}
    borrower = Borrower.get_by_id(data)
    
    if(lender.money == 0):
        flash("Insufficient funds","lender")
        return redirect("/lender/"+str(session["user_id"]))

    if(int(request.form["amount"])<=0):
        flash("Amount to lent must be greater than 0","lender")
        return redirect("/lender/"+str(session["user_id"]))

    if(lender.money < int(request.form["amount"])):
        flash("Cannot lend more money than current Balance","lender")
        return redirect("/lender/"+str(session["user_id"]))

    data = {
        "borrower_id": borrower.id ,
        "lender_id": lender.id,
        "amount": request.form["amount"]
    }
    Debt.save(data)

    data = {
        "id": lender.id,
        "amount": (lender.money - int(request.form["amount"]))
    }
    Lender.update(data)

    data = {
        "id": borrower.id,
        "amount": (borrower.amount_raised + int(request.form["amount"]))
    }
    Borrower.update(data)

    return redirect("/lender/"+str(session["user_id"]))
