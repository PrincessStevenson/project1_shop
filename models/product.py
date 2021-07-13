class Product:

    def __init__(self, product_name, product_type, product_description, stock_quantity, buying_cost, selling_price, product_manufacturer, id = None, ):
        self.product_name = product_name
        self.product_type = product_type
        self.product_description = product_description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.product_manufacturer = product_manufacturer
        self.id = id

    # def mark_outofstock(self):
        
    #     stock_quantity = self.stock_quantity
        
    #     if stock_quantity is <5:
    #         print ("Low in Stock!") 
            
    #     elif stock_quantity == 0
    #         print ("Out of Stock!")
            
    #     else: print ("In Stock!")
    
    # selling_price - buying_cost = 