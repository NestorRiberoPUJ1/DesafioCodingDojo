import bcrypt
from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app

from flask_app.models.borrower import Borrower
from flask_app.models.lender import Lender
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)



@app.route("/registerBorrower", methods=["POST"])
def registerBorrower():
    if (not Borrower.validaUsuario(request.form)):
        return redirect("/")
    pwd = bcrypt.generate_password_hash(request.form["password"])

    formulario = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "money_for" : request.form["money_for"],
        "description" : request.form["description"],
        "amount_needed": request.form["amount_needed"],
        "amount_raised": 0,
        "password": pwd
    }
    id = Borrower.save(formulario)

    session["user_id"] = id
    session["borrower"] = True
    return redirect("/borrower/"+str(session["user_id"]))

@app.route("/loginB")
def loginB():
    return render_template("loginBorrower.html")

@app.route("/loginBorrower", methods=["POST"])
def loginBorrower():
    user = Borrower.get_by_email(request.form)

    if(not user):
        flash("Email no encontrado", "login")
        return redirect("/loginB")

    if(not bcrypt.check_password_hash(user.password, request.form["password"])):
        flash("Contraseña incorrecta", "login")
        return redirect("/loginB")

    session["user_id"] = user.id
    session["borrower"] = True

    return redirect("/borrower/"+str(session["user_id"]))


@app.route("/borrower/<int:id>")
def borrowerHome(id):
    print(id)
    if("user_id" not in session or "borrower" not in session):
        return redirect("/")

    data = {"id": session["user_id"]}
    user = Borrower.get_by_id(data)

    data={
        "borrower_id":user.id
    }
    myLenders= Lender.getByBorrower(data)

    return render_template("borrowerHome.html", user=user, myLenders=myLenders)
