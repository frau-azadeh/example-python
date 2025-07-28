import pandas as pd

# 1. read products.csv
df = pd.read_csv("products.csv", encoding="utf-8-sig")

# 2. filter
filtered_df = df[
    (df["price"] < 27000) & (df["stock"] > 60)
]

# 3. show result
print("📦 محصولات فیلترشده:")
print(filtered_df)

# 4. save in filter_products.csv
filtered_df.to_csv("filtered_products.csv", index=False, encoding="utf-8-sig")
