# 4. Define a `Product` class
class Product:
    # 5. Define constructor with names (String), price (float), and sku (int).
    def __init__(self, name, price, sku):
        # 6. Assign params to properties. 
        self.name = name
        self.price = price
        self.sku = sku
        # Go to main.py to see the next steps.
    
    # 11. Create a `__str__()` method  that takes the object as an argument and returns a string printing out the information about the object. This string should be in the format `"[NAME] (SKU: [SKU]) - $[PRICE]"`.
    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f}"

# 13. Create a `ShoppingCart` class.
class ShoppingCart:
    # 14. Define constructor with items (list) that will hold a list of `Product` objects.
    def __init__(self):
        self.items = []

    # 15. Define a `__str()__` method that prints out information about the `ShoppingCart` object. This string should be in the format `"Shopping Cart with [NUMBER_OF_ITEMS] items.""`.
    def __str__(self):
        return f"Shopping Cart with {len(self.items)} items."
    # Go to main.py to see the next steps.
    
    # 18a.  Define a `add_items` method that takes the object, a product, and a quantity as an argument
    def add_items(self, product, quantity=1):
        # 18b. Add the item to the object's `items` list. It should be added as a dictionary in the format `{"product": [PRODUCT_OBJECT], "quantity": [QUANTITY]}`.
        self.items.append({"product": product, "quantity": quantity})
    
    # 19. Define a `get_total` method that takes the object as an argument.
    def get_total(self):
        # 19b. Initialize a variable called `total` with a value of zero.
        total = 0
        # 19c.  Iterate through `items` and total up the cost of all the items in the cart
        # Could also do sum(item["product"].price * item["quantity"] for item in self.items)
        # But the code below is more readable for beginners.
        for item in self.items:
            total += item["product"].price * item["quantity"]
        # 19d. - Return `total`
        return total
    
    # 20a. Define a `display_cart` method that takes the object as an argument and does the following:
    def display_cart(self):
        # 20b. Iterate through the `items` in the cart and print out a string in the format `"[PRODUCT_NAME] - Quantity: [QUANTITY]')"`
        for item in self.items:
            print(f'{item["product"]} - Quantity: {item["quantity"]}')
        # 20c. When the iteration is complete, print the total cost of all the items in the format `"Total: $[TOTAL]"`.
        print(f"Total: ${self.get_total():.2f}")