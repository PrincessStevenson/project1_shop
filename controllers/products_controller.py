
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)


# INDEX

@products_blueprint.route('/products')
def product():
    products = product_repository.select_all()
    return render_template('products/index.html', all_products = products)



# NEW
# GET '/product/new'
@products_blueprint.route("/products/new")
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", all_manufacturers=manufacturers)


# CREATE
# POST '/products'
@products_blueprint.route("/products", methods=["POST"])
def create_product():
    product_name = request.form["product_name"]
    product_type = request.form["product_type"]
    product_description = request.form["product_description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    product_manufacturer = request.form["product_manufacturer"]
    product = product_repository.select(product_manufacturer)
    create_product = Product(product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, product)
    product_repository.save(create_product)
    return redirect("/products")


# SHOW
# GET '/products/<id>'

# EDIT
# GET '/products/<id>/edit'

# UPDATE
# POST '/products/<id>'

# DELETE
# DELETE '/products/<id>'
@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")