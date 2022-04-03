from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Borrower:

    def __init__(self, data: dict):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.money_for = data["money_for"]
        self.description = data["description"]
        self.amount_needed = data["amount_needed"]
        self.amount_raised = data["amount_raised"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        if("amount_lent" in data):
            self.amount_lent = data["amount_lent"]

    @classmethod
    def save(cls, data: dict):
        query = "INSERT INTO desafiocodingdojo.borrowers (first_name, last_name, email, password, money_for, description, amount_needed, amount_raised) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s, %(money_for)s, %(description)s, %(amount_needed)s,%(amount_raised)s)"
        nuevoId = connectToMySQL("desafiocodingdojo").query_db(query, data)
        return nuevoId

    @staticmethod
    def validaUsuario(user):
        valid = True
        if(len(user["first_name"]) < 2):
            flash("Name must be at least 2 characters long", "borrower")
            valid = False
        if(len(user["last_name"]) < 2):
            flash("Last Name must be at least 2 characters long", "borrower")
            valid = False

        if(not EMAIL_REGEX.match(user["email"])):
            flash("Invalid email", "borrower")
            valid = False
        if(len(user["password"]) < 8):
            flash("Password must be at least 8 characters long", "borrower")
            valid = False

        if(len(user["money_for"]) < 10):
            flash("Money for must be at least 10 characters long", "borrower")
            valid = False

        if(len(user["description"]) < 20):
            flash("Description must be at least 20 characters long", "borrower")
            valid = False

        if(len(user["amount_needed"]) < 3):
            flash("Borrower must borrow at least 100$", "borrower")
            valid = False

        query = "SELECT * FROM desafiocodingdojo.borrowers WHERE email = %(email)s"
        result = connectToMySQL("desafiocodingdojo").query_db(query, user)

        if(len(result) > 0):
            flash("Email already taken", "borrower")
            valid = False
        return valid

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM desafiocodingdojo.borrowers WHERE id = %(id)s;"
        result = connectToMySQL("desafiocodingdojo").query_db(query, data)
        usr = result[0]
        user = cls(usr)
        return user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM desafiocodingdojo.borrowers WHERE email = %(email)s;"
        result = connectToMySQL("desafiocodingdojo").query_db(query, data)
        if(len(result) < 1):
            return False
        else:
            usr = result[0]
            user = cls(usr)
            return user

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM desafiocodingdojo.borrowers "
        results = connectToMySQL("desafiocodingdojo").query_db(query)
        usuarios = []
        for x in results:
            usuarios.append(cls(x))
        return usuarios

    @classmethod
    def update(cls, data):
        query = "UPDATE desafiocodingdojo.borrowers SET amount_raised = %(amount)s WHERE (id = %(id)s);"
        result = connectToMySQL("desafiocodingdojo").query_db(query, data)
        return result

    @classmethod
    def getByLender(cls, data):
        query = "SELECT  borrowers.* ,SUM(amount) as amount_lent FROM desafiocodingdojo.debts "\
                "JOIN desafiocodingdojo.borrowers ON debts.borrower_id=borrowers.id "\
                "WHERE lender_id=%(lender_id)s "\
                "GROUP BY borrower_id;"
        results = connectToMySQL("desafiocodingdojo").query_db(query,data)
        usuarios = []
        for x in results:
            usuarios.append(cls(x))
        return usuarios
