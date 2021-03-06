class Product:

    def __init__(self, product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, product_manufacturer, product_image, id = None, ):
        self.product_name = product_name
        self.product_type = product_type
        self.product_description = product_description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.product_manufacturer = product_manufacturer
        self.product_image = product_image
        self.id = id

    def check_stock(self):
        
        stock_quantity = self.stock_quantity
        
        if stock_quantity == 0:
            return (["Out of Stock!", "red"]) 
            
        elif stock_quantity <5:
            return (["Low in Stock!", "orange"])
            
        else: return (["In Stock!", "green"])
    
