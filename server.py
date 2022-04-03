from flask_app import app
from flask_app.controllers import lender_controller, borrower_controller,debt_controller  # Controladores


if(__name__ == "__main__"):
    app.run(debug=True)