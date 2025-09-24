from flask import Flask,abort
import requests
import json
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    
    res = requests.get("https://682179f7259dad2655af56ae.mockapi.io/api/product")
    data = res.json()
    
    return data

@app.route('/product')
def product():
    pass

@app.route("/insert_user")
def insert():
    req = 
    conn = sqlite3.connect("mydatabase.db")
    


app.run(debug=True)
