# Define function with parameters
def product_info(product_name, price):
    print("Product Name: " + product_name)
    print("Price: " + str(price))


# Call function with parameters assigned as above
product_info("White T-Shirt", 15)

# Call function with keyword arguments
product_info(product_name="Jeans", price=45)
