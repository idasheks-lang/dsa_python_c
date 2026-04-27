class Product:
    def __init__(self, product_name, product_price):
        self.product_name= product_name
        self.product_price = product_price
        
    def get_name(self):
        return self.product_name
    
    def set_name(self, name):
        self.product_name=name
        
p1 = Product("Laptop", 12346)
# p1.product_name="Laptop"
# p1.product_price=123424
print(p1.product_price)
print(p1.get_name())
p1.set_name("Phone")
print(p1.get_name())
        
        