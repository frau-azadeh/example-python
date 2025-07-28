import csv
with open("products.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    print("لیست محصولات فایل")
    for row in reader:
        print(f"نام: {row['name']}, قیمت: {row['price']}, موجودی: {row['stock']} ")