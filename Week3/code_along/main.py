# ShoppingCart and Product imported in last week's code along. 
# 6. Import the `ClothingProduct` class into the file.
# 14. Import the `ElectronicsProduct` class into the file.
from app import Product, ShoppingCart, ClothingProduct, ElectronicsProduct

def main():
    # Code from last week's code along
    laptop = Product("MacBook Pro", 1299.99, "123456")
    headphones = Product("AirPods", 159.99, "789012")

    cart = ShoppingCart()
    cart.add_items(laptop)
    cart.add_items(headphones, 2)
    # End code from last week's code along

    # # 7a. Create an instance of the `ClothingProduct` class. 
    shirt = ClothingProduct("T-Shirt", 9.99, "345678", "M", "Red")
    pants = ClothingProduct("Jeans", 19.99, "901234", "32x32", "Blue")
    # 7b.  Show how it inherited the `__str__` method from the `Product` class.
    print("\nClothing Info:")
    print(shirt)
    print(pants)
    # 8. Call the `clothing_info()` method to see the information about the items that you created. 
    print(shirt.clothing_info())
    # 9. Add both items the cart using `add_items`.
    cart.add_items(shirt)
    cart.add_items(pants)
    print('\nCart Info:')
    print(cart)

    # 15. Create an instance of the `ElectronicsProduct` class and `print()` out the object.
    phone = ElectronicsProduct("iPhone 12", 799.99, "567890", 12)
    tv = ElectronicsProduct("Samsung TV", 999.99, "345678", 24)
    print("\nElectronics Info:")
    # Show how it also inherited the `__str__` method from the `Product` class.
    print(phone)
    print(tv)
    # 16. Call `electronics_info()` to see the additional information about the object.
    print(phone.electronics_info())

    # 17. Call the `under_warranty()` method and print out the resulting boolean.
    print('\nWarranty Check:')
    print(phone.under_warranty(6))
    print(tv.under_warranty(25)) 

    # 18. Finally, add both items the cart using `add_items`. Print out the new cart info.
    cart.add_items(phone)
    cart.add_items(tv)
    print('\nCart Info:')
    print(cart)


# Call the main() function. See bash.sh for directions on how to run in your terminal.
main()