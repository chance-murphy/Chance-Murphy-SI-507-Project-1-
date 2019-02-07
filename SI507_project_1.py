from flask import Flask
from lab3_code import *

app = Flask(__name__)

@app.route('/') #Home page of the app
def home():
    return "Hello, Welcome to our online banking application!"

@app.route('/bank/<name>')
def bank_name(name):
    bank_name = Bank(name, Dollar, 50)
    return "Welcome to {}".format(bank_name.name)

@app.route('/dollar/<amt>')
def display_amt(amt):
    dollar = Dollar(int(amt))
    return dollar.__str__()

@app.route('/yuan/<amt>')
def display_amt1(amt):
    yuan = Yuan(int(amt))
    return yuan.__str__()

@app.route('/pound/<amt>')
def display_amt2(amt):
    pound = Pound(int(amt))
    return pound.__str__()

@app.route('/bank/<name>/<currency>/<value>')
def banking(name,currency,value):
    if currency == "Dollar":
        p = Dollar


    elif currency == "Yuan":
        p = Yuan

    elif currency == "Pound":
        p = Pound

    else:
        return "Invalid URL inputs for bank"

    bank_inst1 = Bank(name,p,int(value))
    return bank_inst1.__str__()


if __name__ == "__main__":
    app.run()
