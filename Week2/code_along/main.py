# 7. Import the `Product` class into the file. 
# 16. Import the `ShoppingCart` class into the file.
from app import Product, ShoppingCart

# 8. Create `main()` function that will hold all of our program runs.  Call the function.

def main():
    # 9. Create two instances of the `Product` class and print out the attributes. To see the output run `python3 main.py` in the command line.
    laptop = Product("MacBook Pro", 1299.99, "123456")
    headphones = Product("AirPods", 159.99, "789012")
    print(laptop.name)
    print(headphones.price)

    # 10. Print out the object. You should see something like `<app.Product object at 0x1007e2e40>`.
    print("\nUsing __str__ method:")
    print(laptop)
    print(headphones)
    # Go to app.py to see next steps

    # 17. Create an instance of the shopping cart and print it to the console.
    cart = ShoppingCart()
    print("\nUsing __str__ method:")
    print(cart)
    # Go to app.py to see next steps

    # 21. Add each of the `Product` objects you created in step 9 to the `ShoppingCart` instance using the `add_items` method. 
    cart.add_items(laptop)
    cart.add_items(headphones, 2) # Add 2 pairs of headphones


    # 22. Display the cart contents using the `display_cart` method.
    print("\nUsing display_cart method:")
    cart.display_cart()

    # 23. Call `get_total` to see the total cost of everything that you added to the cart.
    print("\nUsing get_total method:")
    print(f'TOTAL: ${cart.get_total()}')

# Call the main() function. See bash.sh for directions on how to run in your terminal.
main()