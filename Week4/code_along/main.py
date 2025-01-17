from app import Product, ShoppingCart, ClothingProduct, ElectronicsProduct

def main():
    # Code from previous 2 weeks code along
    laptop = Product("MacBook Pro", 1299.99, "123456")
    headphones = Product("AirPods", 159.99, "789012")
    shirt = ClothingProduct("T-Shirt", 9.99, "345678", "M", "Red")
    pants = ClothingProduct("Jeans", 19.99, "901234", "32x32", "Blue")
    phone = ElectronicsProduct("iPhone 12", 799.99, "567890", 12)
    tv = ElectronicsProduct("Samsung TV", 999.99, "345678", 24)

    print('\nItem Info:')
    print(laptop)
    print(headphones)
    print(shirt)
    print(pants)
    print(phone)
    print(tv)

    #Update Clothing Info:
    shirt.set_size("L")
    shirt.set_color("Green")

    print('\nUpdated Item Info:')
    print(shirt)

# Call the main() function. See bash.sh for directions on how to run in your terminal.
main()