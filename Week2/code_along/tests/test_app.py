from app import Product, ShoppingCart

def test_product():
    product1 = Product("Widget", 25.00, 12345)
    assert product1.name == "Widget"
    assert product1.price == 25.00
    assert product1.sku == 12345
    assert str(product1) == "Widget (SKU: 12345) - $25.00"

def test_shopping_cart():
    cart = ShoppingCart()
    assert str(cart) == "Shopping Cart with 0 items."
    product1 = Product("Widget", 25.00, 12345)
    cart.add_items(product1)
    assert str(cart) == "Shopping Cart with 1 items."
    assert cart.get_total() == 25.00
    product2 = Product("Gadget", 50.00, 54321)
    cart.add_items(product2, 2)
    assert str(cart) == "Shopping Cart with 2 items."
    assert cart.get_total() == 125.00
    cart.display_cart()
    # Expected Output:
    # Widget (SKU: 12345) - $25.00 - Quantity: 1
    # Gadget (SKU: 54321) - $50.00 - Quantity: 2
    # Total: $125.00