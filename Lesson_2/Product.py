class Product:
    name = None
    price = None
    quantity = None
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f'Product name is {self.name}, with a price {self.price} and {self.quantity} pieces'