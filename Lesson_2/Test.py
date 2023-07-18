from Customer import Customer
from Product import Product


if __name__ == "__main__" :
    product1 = Product("Shirt", 20, 2)
    print(str(product1))
    product2 = Product("Shoes", 50, 1)
    print(str(product2))
    product3 = Product("Hat", 10, 3)
    print(str(product3))
    
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    
    customer1.add_to_cart(product1)
    customer1.add_to_cart(product2)
    customer2.add_to_cart(product3)
    
    customer1.complete_purchase()
    customer2.complete_purchase()
    
    customer1.remove_from_cart(product1)
    customer1.complete_purchase()