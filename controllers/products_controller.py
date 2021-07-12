from app import manufacturers
from flask import Flask, render_template
from flask import Blueprint
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

# NEW
# GET '/product/new'
@tasks_blueprint.route("/products/new")
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", all_manufacturers=manufacturers)


# CREATE
# POST '/products'
@tasks_blueprint.route("/products", methods=["POST"])
def new_product():
    product_name = request.form["product_name"]
    product_type = request.form["product_type"]
    product_description = request.form["product_description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    product_manufacturer = request.form["product_manufacturer"]
    product_id = request.form['product_id']
    product = product_repository.select(product_id)
    new_product = Product(roduct_name, product_type, product_description, stock_quantity, buying_cost, selling_price, product_manufacturer)
    product_repository.save(new_product)
    return redirect("/products")


# SHOW
# GET '/products/<id>'

# EDIT
# GET '/products/<id>/edit'

# UPDATE
# PUT '/products/<id>'

# DELETE
# DELETE '/products/<id>'
@tasks_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")