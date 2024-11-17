from flask import Flask, request, render_template
from markupsafe import escape
from models import Products
from database import session
import random

app = Flask(__name__)

@app.route("/")
def homepage():
    get_Product()
    return render_template('homepage.html')

@app.route("/hello/")
@app.route("/hello/<name>")
def greet(name = None):
    return render_template('greet.html', name=name)

# @app.route("/products/", methods=['GET', 'POST'])
# def products():
#     if request.method == 'POST':
#         return "This is post call"
#     else:
#         return "<h1> Products </h1>"
    
@app.get("/products/")
def product_get():
        products = get_Product()
        page = "<h1> Products Get</h1>"
        page += '<ul>'
        for product in products:
            page += f'<li>{product.name} </li>'
        page += '</ul>'
        return page

    
@app.get("/addproduct/")
def product_add():
    return render_template('addProduct.html')


@app.post("/addproduct/")
def product_post():
    name = request.form['name']
    price = int(request.form['price'])
    quantity = int(request.form['quantity'])
    add_Product(name, price, quantity)
    return "<h2> Product Added </h2>"

@app.route("/products/<int:id>")
def product(id):
    return render_template('products.html', productid = id)

# @app.route("/users/", methods=['GET', 'POST'])
# def users():
#     if request.method == 'POST':
#         firstName = request.form['fname']
#         lastName = request.form['lname']
#         print(request.form)
#         # do whatever you want with the values
#         return f"<h1> Users page: {firstName} {lastName} </h1>"
#     else:
#         firstName = request.args.get('fname')
#         lastName = request.args.get('lname', default="")
#         print(request.args)
#         # do whatever you want with the values
#         return f"<h1> Users page: {firstName} {lastName} </h1>"
    
@app.get("/users/")
def users_get():
    firstName = request.args.get('fname')
    lastName = request.args.get('lname', default="")
    print(request.args)
    # do whatever you want with the values
    return f"<h1> Users page: {firstName} {lastName} </h1>"

@app.post("/users/")
def users_post():
    firstName = request.form['fname']
    lastName = request.form['lname']
    print(request.form)
    # do whatever you want with the values
    return f"<h1> Users page: {firstName} {lastName} </h1>"

@app.route("/users/<username>/")
def user(username):
    return f"<h1> User: #{escape(username)} </h1>"

@app.route("/about/<path:subpath>/")
def about(subpath):
    return f"<h1> Path: #{escape(subpath)} </h1>"

def add_Product(name, price, quantity):
    product = Products(name = name, price = price, quantity = quantity)
    session.add(product)
    session.commit()

def get_Product():
    return session.query(Products).all()