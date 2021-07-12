from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.product import Product
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository


def save(product):
    sql = "INSERT INTO products (product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [product.product.name, product.product.type, product.product.description, product.stock.quantity, product.buying.cost, product.selling.cost, product.manufacturer.id, product.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product



def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        product = product_repository.select(row['manufacturer_id'])
        Manufacturer = Product(row['manufacturers_name'], manufacturer, row['country_origin'], row['id'] )
        products.append(product)
    return products


def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product = Product(result['product_name'], result['product_type'] , result['product_description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], result['product_manufacturer'], result['id'])
    return product




def delete_all():
    sql = "DELETE  FROM products"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(product):
    sql = "UPDATE products SET (product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, product_manufacturer) = (%s, %s, %s, %s) WHERE id = %s"
    values = [tproduct.product.name, product.product.type, product.product.description, product.stock.quantity, product.buying.cost, product.selling.cost, product.manufacturer.id, product.id]
    run_sql(sql, values)
