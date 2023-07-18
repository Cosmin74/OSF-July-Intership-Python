from Cart import Cart

class Customer:
    name = None
    cart = None
    
    def __init__(self, name):
        self.name = name
        self.cart = Cart()
        
    def add_to_cart(self, product):
        self.cart.add_product(product)
        print(f"{product.name} added to {self.name}'s cart")
        
    def remove_from_cart(self, product):
        self.cart.remove_product(product)
        print(f"{product.name} removed from {self.name}'s cart")
    
    def complete_purchase(self):
        total = 0
        total = self.cart.calculate_total_price()
        print(f"{self.name}'s cart total: ${total}")
        return total