
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)


# INDEX

@manufacturers_blueprint.route('/manufacturers')
def manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/index.html', all_manufacturers = manufacturers)



# NEW
# GET '/manufacturer/new'
@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    products = product_repository.select_all()
    return render_template("manufacturers/new.html", all_products=products)


# CREATE
# POST '/manufacturer'
@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    manufacturers_name = request.form["manufacturers_name"]
    country_origin = request.form["country_origin"]
    create_manufacturer = Manufacturer(manufacturers_name, country_origin)
    manufacturer_repository.save(create_manufacturer)
    return redirect("/manufacturers")


# SHOW
# GET '/manufacturers/<id>'

# EDIT
# GET '/manufacturers/<id>/edit'

# UPDATE
# POST '/manufacturers/<id>'

# DELETE
# DELETE '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturer/<id>/delete", methods=["POST"])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")