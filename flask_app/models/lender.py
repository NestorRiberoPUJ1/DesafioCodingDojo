from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Lender:

    def __init__(self, data: dict):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.money = data["money"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        if ("amount_lent" in data):
            self.amount_lent = data["amount_lent"]

    @classmethod
    def save(cls, data: dict):
        query = "INSERT INTO desafiocodingdojo.lenders (first_name, last_name, email, password, money) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s, %(money)s)"
        nuevoId = connectToMySQL("desafiocodingdojo").query_db(query, data)
        return nuevoId

    @staticmethod
    def validaUsuario(user):
        valid = True
        if(len(user["first_name"]) < 2):
            flash("Name must be at least 2 characters long", "lender")
            valid = False
        if(len(user["last_name"]) < 2):
            flash("Last Name must be at least 2 characters long", "lender")
            valid = False

        if(not EMAIL_REGEX.match(user["email"])):
            flash("Invalid email", "lender")
            valid = False
        if(len(user["password"]) < 8):
            flash("Password must be at least 8 characters long", "lender")
            valid = False

        if(len(user["money"]) < 5):
            flash("Lender must have at least 10k to lend", "lender")
            valid = False

        query = "SELECT * FROM desafiocodingdojo.lenders WHERE email = %(email)s"
        result = connectToMySQL("desafiocodingdojo").query_db(query, user)

        if(len(result) > 0):
            flash("Email already taken", "lender")
            valid = False
        return valid

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM desafiocodingdojo.lenders WHERE id = %(id)s;"
        result = connectToMySQL("desafiocodingdojo").query_db(query, data)
        usr = result[0]
        user = cls(usr)
        return user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM desafiocodingdojo.lenders WHERE email = %(email)s;"
        result = connectToMySQL("desafiocodingdojo").query_db(query, data)
        if(len(result) < 1):
            return False
        else:
            usr = result[0]
            user = cls(usr)
            return user

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM desafiocodingdojo.lenders "
        results = connectToMySQL("desafiocodingdojo").query_db(query)
        usuarios = []
        for x in results:
            usuarios.append(cls(x))
        return usuarios

    @classmethod
    def update(cls, data):
        query = "UPDATE desafiocodingdojo.lenders SET money = %(amount)s WHERE (id = %(id)s);"
        result = connectToMySQL("desafiocodingdojo").query_db(query, data)
        return result

    @classmethod
    def getByBorrower(cls, data):
        query = "SELECT  lenders.* ,SUM(amount) as amount_lent FROM desafiocodingdojo.debts "\
                "JOIN desafiocodingdojo.lenders ON debts.lender_id=lenders.id "\
                "WHERE borrower_id=%(borrower_id)s "\
                "GROUP BY lender_id;"
        results = connectToMySQL("desafiocodingdojo").query_db(query, data)
        usuarios = []
        for x in results:
            usuarios.append(cls(x))
        return usuarios
