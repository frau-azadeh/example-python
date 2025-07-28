product = {
    "product": "bag",
    "price": 26500,
    "stock": 120,
    "company": "zara"
}

print("first information")
for key , value in product.items():
    print(f"{key}:{value}")

# change stock
product["stock"] = 95

print("\n Change stock")

print("\n update information")
for key, value in product.items():
    print(f"{key}:{value}")