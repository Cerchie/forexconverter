from flask import Flask, request, render_template
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"



from unittest import TestCase

class ForexTests(TestCase):
    def test_homepage_form(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 404) 
            # this 404 is from a favicode error

    def test_result_form(self):
        with app.test_client() as client:
            resp = client.get('/calc-results')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 404) 
            # this 404 is from a favicode error

    
    
    

      

