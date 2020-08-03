from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal
# import functions.py
app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('/homepage.html')

@app.route('/calc_results', methods=['GET', 'POST'])
def convert():
    
    convert_to = request.form.get('convert-to')
    convert_from = request.form.get('convert-from')
    old_amount = request.form.get('amount', 0)

 
    try: #read about this and update
        amount = float('0'+ old_amount)
        c = CurrencyRates(force_decimal=True)
        resultOne = c.convert(convert_from, convert_to, Decimal(amount))
        resultTwo = round(resultOne, 2)
        cc = CurrencyCodes()
        symbol = cc.get_symbol(convert_to)
    
        return render_template('result.html', resultTwo=resultTwo, symbol=symbol)
    except:
        flash("please enter an integer")
        return render_template('/flash_homepage.html')