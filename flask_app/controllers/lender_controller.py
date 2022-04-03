import bcrypt
from flask import Flask, render_template, redirect, session, flash, request
from flask_app import app
from flask_app.models.borrower import Borrower

from flask_app.models.lender import Lender
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/")
def root():
    return redirect("/register")


@app.route("/register")
def index():
    return render_template("index.html")


@app.route("/registerLender", methods=["POST"])
def registerLender():
    if (not Lender.validaUsuario(request.form)):
        return redirect("/")
    pwd = bcrypt.generate_password_hash(request.form["password"])

    formulario = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "money": request.form["money"],
        "password": pwd
    }
    id = Lender.save(formulario)

    session["user_id"] = id
    session["lender"] = True
    return redirect("/lender/"+str(id))


@app.route("/loginL")
def loginL():
    return render_template("loginLender.html")


@app.route("/loginLender", methods=["POST"])
def loginLender():
    user = Lender.get_by_email(request.form)

    if(not user):
        flash("Email no encontrado", "login")
        return redirect("/loginL")

    if(not bcrypt.check_password_hash(user.password, request.form["password"])):
        flash("Contraseña incorrecta", "login")
        return redirect("/loginL")

    session["user_id"] = user.id
    session["lender"] = True
    return redirect("/lender/"+str(session["user_id"]))


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/lender/<int:id>")
def lenderHome(id):
    print(id)
    if("user_id" not in session or "lender" not in session):
        return redirect("/")

    data = {"id": session["user_id"]}
    user = Lender.get_by_id(data)

    borrowers= Borrower.getAll()

    data={
        "lender_id":user.id
    }
    myBorrowers= Borrower.getByLender(data)

    return render_template("lenderHome.html", user=user, borrowers=borrowers,myBorrowers=myBorrowers)
