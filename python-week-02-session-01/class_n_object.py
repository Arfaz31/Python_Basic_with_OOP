class Shop:
    # products = [] #class attribute


#যখনই তুমি কোনো class থেকে নতুন object তৈরি করো, তখন Python স্বয়ংক্রিয়ভাবে __init__ method-টা চালায়। এরমানে Python __init__ method এ "Test Shop" পাঠায়, আর self.name = name এর মাধ্যমে সেই নামটা object এ save হয়ে যায়।
    def __init__(self, name):
        self.name = name
        self.products = []  #instance attribute

#__repr__ method:এটা হলো object print করার সময় কি দেখাবে, সেটা ঠিক করে দেয়।
    def __repr__(self):
        return f"This is sho name is: {self.name}"
    
    def add_product(self, name, price):
        product = Product(name, price)
        # Shop.products.append(product) #class attribute এটা করলে products সবার জন্য একই হবে
        self.products.append(product) #instance attribute

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

print(shop1)

shop2 = Shop("Test Shop 2")
shop2.add_product("Product 1", 100)
shop2.add_product("Product 2", 200)
shop2.add_product("Product 3", 300)

print(shop2)
        