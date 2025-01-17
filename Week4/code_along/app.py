class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self.price = price
        # Change this property to a private value
        self.__sku = sku
    
    # Update with getter method for sku
    def __str__(self):
        return f"{self.name} (SKU: {self.get_sku()}) - ${self.price:.2f}"
     
    # Create a getter for the sku property
    def get_sku(self):
        return self.__sku
    
    # Create a setter for the sku property
    def set_sku(self, new_sku):
        self.__sku = new_sku

class ShoppingCart:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Shopping Cart with {len(self.items)} items."
    
    def add_items(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})
    
    def get_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
    
    def display_cart(self):
        for item in self.items:
            print(f'{item["product"]} - Quantity: {item["quantity"]}')
        print(f"Total: ${self.get_total():.2f}")

class ClothingProduct(Product):
    def __init__(self, name, price, sku, size, color):
        Product.__init__(self, name, price, sku)
        # Change these properties to private values
        self.__size = size
        self.__color = color
    
    # Change to be a __str__ method to implement polymorphism. Update with getter methods for private properties
    def __str__(self):
        return f"{self.name} (SKU: {self.get_sku()}) - ${self.price:.2f} - Size: {self.get_size()}, Color: {self.get_color()}"
    
    def get_size(self):
        return self.__size
    
    def get_color(self):
        return self.__color
    
    def set_size(self, new_size):
        self.__size = new_size
    
    def set_color(self, new_color):
        self.__color = new_color

class ElectronicsProduct(Product):
    def __init__(self, name, price, sku, warranty_months):
        Product.__init__(self, name, price, sku)
        self.warranty_months = warranty_months

    # Change to be a __str__ method to implement polymorphism
    def __str__(self):
        return f"{self.name} (SKU: {self.get_sku()}) - ${self.price:.2f} - Warranty: {self.warranty_months} months"
    
    def under_warranty(self, months):
        if self.warranty_months > months:
            return True
        else:
            return False