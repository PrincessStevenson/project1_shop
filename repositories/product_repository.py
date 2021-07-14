from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.product import Product
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository


def save(product):
    sql = "INSERT INTO products (product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, manufacturer_id, product_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.product_name, product.product_type, product.product_description, product.stock_quantity, product.buying_cost, product.selling_price, product.product_manufacturer.id, product.product_image]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product



def select_all():
    all_products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        product = Product(row['product_name'], row['product_type'], row['product_description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], manufacturer, row['product_image'], row['id'])
        all_products.append(product)
    return all_products


def total_products(product_type):
    sql = "SELECT COUNT(product_type) from products WHERE product_type = %s"
    values = [product_type]
    results = run_sql(sql, values)[0][0]
    return(results)


def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product = Product(result['product_name'], result['product_type'] , result['product_description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], manufacturer, result['product_image'], result['id'])
    return product




def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(product):
    sql = "UPDATE products SET (product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, product_manufacturer, product_image) = (%s, %s, %s, %s) WHERE id = %s"
    values = [product.product_name, product.product_type, product.product_description, product.stock_quantity, product.buying_cost, product.selling_cost, product.product_manufacturer.id, product.product_image, product.id]
    run_sql(sql, values)
