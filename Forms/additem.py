from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from flask_mysqldb import MySQL

from BusinessLayer.Food import validate_food
from DataAccess.DBConnectionFood import insert_into_database
from Models import List
from Models.Food import Food
import Models.User

app = Flask(__name__)
app.secret_key = 'watermelonsugar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'wasteless'

# Intialize MySQL
mysql = MySQL(app)


def add_item():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'quantity' in request.form and 'calories' in request.form and 'expiredate' in request.form:
        name = request.form['name']
        quantity = request.form['quantity']
        calories = request.form['calories']
        expiredate = request.form['expiredate']
        if validate_food(name, quantity, calories, expiredate) == 'ok':
            f = Food(name, quantity, calories, expiredate)
            insert_into_database(f)
            m1 = Food.compute_calories_perday(f)
            m2 = Food.compute_grams_perday(f)
            flash(m1)
            flash(m2)
            return render_template('welcome.html', msg=msg)
    return render_template('additem.html', msg=msg)
