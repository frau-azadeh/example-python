products = [
    {"name":"bag1", "price": 26500, "stock":120},
    {"name": "bag2", "price": 24500, "stock":80},
    {"name":"bag3","price":2850, "stock":98 }
]

print("Product list:\n")

for index, product in enumerate(products, start=1):
    print(f"product {index} :")
    print(f"Name: {product['name']}")
    print(f"price: {product['price']}")
    print(f"stock:{product['stock']}")
    print("-"*30)
