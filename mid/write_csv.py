import csv

products = [
    {"name": "میلگرد A3", "price": 26500, "stock": 120},
    {"name": "میلگرد A2", "price": 24500, "stock": 80},
    {"name": "میلگرد A4", "price": 28500, "stock": 50}
]

with open("products.csv", "w", newline='', encoding="utf-8-sig") as file:
    fieldnames = ["name", "price", "stock"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for product in products:
        writer.writerow(product)

print(" file product.csv is made")
