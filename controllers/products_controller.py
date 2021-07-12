from flask import Flask, render_template
from flask import Blueprint
from models.product import Product

products_blueprint = Blueprint("products", __name__)

