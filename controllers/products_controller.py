
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
    toys = product_repository.total_products("Toys")
    uniforms = product_repository.total_products("Uniforms")
    other = product_repository.total_products("Other")
    return render_template('products/index.html', all_products = products, toys = toys, uniforms = uniforms, other = other)



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
    product_image = request.form["product_image"]
    product = product_repository.select(product_manufacturer)
    create_product = Product(product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, product, product_image)
    product_repository.save(create_product)
    return redirect("/products")


# SHOW
# GET '/products/<id>'
@products_blueprint.route("/products/<id>")
def show_product(id):
    product_index = product_repository.select(id)
    return render_template("products/show.html", product_index = product_index)
    
# products/{{product.id}}



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