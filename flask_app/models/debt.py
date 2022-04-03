from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Debt:

    def __init__(self, data: dict):
        self.id = data["id"]
        self.borrower_id = data["borrower_id"]
        self.lender_id = data["lender_id"]
        self.amount = data["amount"]


    @classmethod
    def save(cls, data: dict):
        query = "INSERT INTO desafiocodingdojo.debts (borrower_id, lender_id, amount) VALUES (%(borrower_id)s,%(lender_id)s,%(amount)s)"
        nuevoId = connectToMySQL("desafiocodingdojo").query_db(query, data)
        return nuevoId


