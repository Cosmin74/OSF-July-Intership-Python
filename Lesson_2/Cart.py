class Cart:
    products = None
    
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        
    def remove_product(self, product):
        self.products.remove(product)
    
    def calculate_total_price(self):
        total = 0
        for product in self.products:
            total = total + product.price * product.quantity
        return total
        