# Code Demo Instructions

## Overview

This week we’ll be finishing our e-commerce store by implementing polymorphism and encapsulation for the store. This week we'll be implementing public and private properties, creating polymorphic functions, and creating getter and setter methods for some of our private properties.

![Week 4 Class Diagram](./E-Store_W3.png)

By the end of this code along, our e-commerce store will have increased specialization so that we can handle a much wider variety of products.

## Local Terminal - bash.sh has syntax instructions
1. Navigate to the folder that was created last week. There should be two files in the folder: `app.py` and `main.py`. Go to the `app.py` file.

## VS Code - app.py has syntax instructions
2. In `ClothingProduct`, change the `clothing_info` method to a `__str__` method.
3. In `ElectronicsProduct`, change the `clothing_info` method to a `__str__` method.

## VS Code - main.py has syntax instructions
4. Create instances of `Product`, `ClothingProduct`, and `ElectronicsProduct`. Log the values using a `print()` statement and show how the `__str__` method is different due to polymorphism.

## VS Code - app.py has syntax instructions
5. In `Product`, change `sku` to be a private attribute.
6. In `ClothingProduct`, change `color` and `size` to be private attributes.

## VS Code - main.py has syntax instructions
7. Run the code in `main.py` again. Show that it now throws an error since our `__str__` methods are trying to access private attributes. We need getter and setter methods in order to interact with these now.

## VS Code - app.py has syntax instructions
8. In `Product`, do the following:
    - Declare a `get_sku` method that takes the object as an argument and returns the the value contained in `__sku`.
    - Declare a `set_sku` method that takes the object and a `new_sku` as an argument and sets the value of `__sku` to the provided new value.
    - Update the `__str__` method so that anytime you are trying to access `__sku` it now calls `get_sku()` instead.
9. In `ElectronicsProduct`, update the `__str__` method so that anytime you are trying to access `__sku` it now calls `get_sku()` instead.
10. In `ClothingProduct`, do the following:
    - Declare a `get_color` method that takes the object as an argument and returns the the value contained in `__color`.
    - Declare a `get_size` method that takes the object as an argument and returns the the value contained in `__size`.
    - Declare a `set_color` method that takes the object and a `new_color` as an argument and sets the value of `__color` to the provided new value.
    - Declare a `set_size` method that takes the object and a `new_size` as an argument and sets the value of `__size` to the provided new value.
    - Update the `__str__` method so that anytime you are trying to access `__sku`, `__size`, and `__color`, it now calls `get_sku()`, `get_size()`, and `get_color()` instead.

## VS Code - main.py has syntax instructions
11. Run the code in `main.py` again to verify the new outputs.
12. Change the size and color using the new setter methods that were created.