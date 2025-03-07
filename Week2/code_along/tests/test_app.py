from app import Product, ShoppingCart

# This is a test function that checks if the Product class is working as expected.
def test_can_create_product():
    product1 = Product("Widget", 25.00, 12345)
    # check that it is a Product instance
    assert isinstance(product1, Product)
    # check that the properties are set correctly
    assert product1.name == "Widget"
    assert product1.price == 25.00
    assert product1.sku == 12345

# This is a test function that checks if the __str__ method in the Product class is working as expected.
def test_product_str():
    product1 = Product("Widget", 25.00, 12345)
    assert str(product1) == "Widget (SKU: 12345) - $25.00"

# Test function that checks if the ShoppingCart class is working as expected.
def test_can_create_shoppingcart():
    cart = ShoppingCart()
    # check that it is an instance of the ShoppingCart class
    assert isinstance(cart, ShoppingCart)

# Test function that checks if the __str__ method in the ShoppingCart class is working as expected.
def test_shoppingcart_str():
    cart = ShoppingCart()
    assert str(cart) == "Shopping Cart with 0 items."
    product1 = Product("Widget", 25.00, 12345)
    cart.add_items(product1)
    assert str(cart) == "Shopping Cart with 1 items."
    product2 = Product("Gadget", 50.00, 54321)
    cart.add_items(product2, 2)
    assert str(cart) == "Shopping Cart with 2 items."

# Test function that checks if the add_items method in the ShoppingCart class is working as expected.
def test_shoppingcart_add_items():
    cart = ShoppingCart()
    product1 = Product("Widget", 25.00, 12345)
    cart.add_items(product1)
    assert len(cart.items) == 1
    assert cart.items[0]["product"] == product1
    assert cart.items[0]["quantity"] == 1
    product2 = Product("Gadget", 50.00, 54321)
    cart.add_items(product2, 2)
    assert len(cart.items) == 2
    assert cart.items[1]["product"] == product2
    assert cart.items[1]["quantity"] == 2