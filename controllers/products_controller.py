from flask import Flask, render_template
from flask import Blueprint
from models.product import Product

products_blueprint = Blueprint("products", __name__)

# NEW
# GET '/product/new'

# CREATE
# POST '/products'

# SHOW
# GET '/products/<id>'

# EDIT
# GET '/products/<id>/edit'

# UPDATE
# PUT '/products/<id>'

# DELETE
# DELETE '/products/<id>'