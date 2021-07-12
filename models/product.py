class Product:

    def __init__(self, product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, product_manufacturer, in_stock, id = None, ):
        self.product_name = product_name
        self.product_type = product_type
        self.product_description = product_description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.product_manufacturer = product_manufacturer
        self.id = id

    def mark_outofstock(self)
        self.outofstock = False