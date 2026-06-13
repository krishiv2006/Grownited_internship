import pandas as pd

with open("inventory.csv", "w") as f:
    f.write("""Product,Category,Stock
Laptop,Electronics,10
Mobile,Electronics,15
Printer,Electronics,5
Chair,Furniture,20
Table,Furniture,8""")

df = pd.read_csv("inventory.csv")

print("===== ALL PRODUCTS =====")
print(df)

print("\n===== TOTAL STOCK =====")
total_stock = df["Stock"].sum()
print("Total Stock:", total_stock)

print("\n===== PRODUCT WITH HIGHEST STOCK =====")
highest_stock = df["Stock"].max()
print(df[df["Stock"] == highest_stock])

print("\n===== PRODUCT WITH LOWEST STOCK =====")
lowest_stock = df["Stock"].min()
print(df[df["Stock"] == lowest_stock])

print("\n===== CATEGORY-WISE STOCK =====")
category_stock = df.groupby("Category")["Stock"].sum()
print(category_stock)

print("\n===== PRODUCTS WITH STOCK LESS THAN 10 =====")
print(df[df["Stock"] < 10])

print("\n===== PRODUCTS SORTED BY STOCK =====")
sorted_df = df.sort_values(by="Stock", ascending=False)
print(sorted_df)

print("\n===== INVENTORY REPORT =====")
print("Total Products :", len(df))
print("Total Stock    :", total_stock)
print("Highest Stock  :", highest_stock)
print("Lowest Stock   :", lowest_stock)

print("\nCategory-wise Stock:")
print(category_stock)

print("\nLow Stock Products:")
print(df[df["Stock"] < 10][["Product", "Stock"]])