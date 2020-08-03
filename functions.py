from flask import Flask, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

# def empty_form():
#     amount = request.form.get('amount')
#     if amount ==' ':
#         flash('please enter an amount')

# empty_form()