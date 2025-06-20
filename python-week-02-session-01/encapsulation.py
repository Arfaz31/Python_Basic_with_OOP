class Shop:
    # products = [] #class attribute

    def __init__(self, name):
        self.name = name
        self.products = []  #instance attribute
        self._balance = 500 #Access modifier-> private

    def __repr__(self):
        return f"This is sho name is: {self.name}"
    
    def add_product(self, name, price):
        product = Product(name, price)
        self.products.append(product)

    def sell(self, product):
        self._balance += product.price
    
    def _tax_add(self):   #private
        return self._balance * 0.1
    
    def get_balance(self):
        return self._balance - self._tax_add()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return self.name
    

shop1 = Shop("Test Shop")
shop1.add_product("Product 1", 100)
shop1.add_product("Product 2", 200)
shop1.add_product("Product 3", 300)

print(shop1.get_balance())


