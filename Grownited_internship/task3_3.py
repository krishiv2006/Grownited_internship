import pandas as pd

with open("ecom_sales.csv", "w") as f:
    f.write("""OrderID,Customer,City,Product,Category,Quantity,Price
1001,Amit,Ahmedabad,Laptop,Electronics,1,50000
1002,Neha,Surat,Mobile,Electronics,2,20000
1003,Rahul,Ahmedabad,Chair,Furniture,4,3000
1004,Priya,Vadodara,Table,Furniture,2,8000
1005,Jay,Rajkot,Printer,Electronics,1,15000
1006,Riya,Ahmedabad,Mobile,Electronics,1,20000
1007,Karan,Surat,Laptop,Electronics,1,50000
1008,Sneha,Vadodara,Chair,Furniture,3,3000
1009,Amit,Ahmedabad,Printer,Electronics,2,15000
1010,Neha,Surat,Table,Furniture,1,8000""")

df = pd.read_csv("ecom_sales.csv")

df["Revenue"] = df["Quantity"] * df["Price"]

print("=" * 50)
print("TASK 1: DATASET SUMMARY")
print("=" * 50)
print("Total Records :", len(df))
print("Total Columns :", len(df.columns))
print("\nColumns:")
for col in df.columns[:-1]:
    print(col)

print("\nData Types:")
print(df.dtypes)

total_revenue = df["Revenue"].sum()
average_revenue = df["Revenue"].mean()

print("\n" + "=" * 50)
print("TASK 2: TOTAL REVENUE")
print("=" * 50)
print("Total Revenue =", total_revenue)

print("\n" + "=" * 50)
print("TASK 3: AVERAGE ORDER REVENUE")
print("=" * 50)
print("Average Revenue =", average_revenue)

print("\n" + "=" * 50)
print("TASK 4: HIGHEST REVENUE ORDER")
print("=" * 50)
highest_order = df.loc[df["Revenue"].idxmax()]
print("OrderID :", highest_order["OrderID"])
print("Customer :", highest_order["Customer"])
print("Revenue :", highest_order["Revenue"])

print("\n" + "=" * 50)
print("TASK 5: LOWEST REVENUE ORDER")
print("=" * 50)
lowest_order = df.loc[df["Revenue"].idxmin()]
print("OrderID :", lowest_order["OrderID"])
print("Revenue :", lowest_order["Revenue"])

print("\n" + "=" * 50)
print("TASK 6: PRODUCT WISE REVENUE")
print("=" * 50)
product_revenue = df.groupby("Product")["Revenue"].sum()
print(product_revenue)

print("\n" + "=" * 50)
print("TASK 7: CATEGORY WISE REVENUE")
print("=" * 50)
category_revenue = df.groupby("Category")["Revenue"].sum()
print(category_revenue)

print("\n" + "=" * 50)
print("TASK 8: CUSTOMER WISE REVENUE")
print("=" * 50)
customer_revenue = df.groupby("Customer")["Revenue"].sum()
print(customer_revenue)

print("\n" + "=" * 50)
print("TASK 9: TOP CUSTOMER")
print("=" * 50)
top_customer = customer_revenue.idxmax()
print("Top Customer :", top_customer)
print("Revenue :", customer_revenue.max())

print("\n" + "=" * 50)
print("TASK 10: TOP PRODUCT")
print("=" * 50)
top_product = product_revenue.idxmax()
print("Top Product :", top_product)
print("Revenue :", product_revenue.max())

print("\n" + "=" * 50)
print("TASK 11: CITY WISE REVENUE")
print("=" * 50)
city_revenue = df.groupby("City")["Revenue"].sum()
print(city_revenue)

print("\n" + "=" * 50)
print("TASK 12: ORDERS ABOVE AVERAGE REVENUE")
print("=" * 50)
above_avg = df[df["Revenue"] > average_revenue]
print(above_avg[["OrderID", "Revenue"]])

print("\n" + "=" * 50)
print("TASK 13: SORT ORDERS BY REVENUE DESCENDING")
print("=" * 50)
sorted_orders = df.sort_values(by="Revenue", ascending=False)
print(sorted_orders[["OrderID", "Revenue"]])

print("\n" + "=" * 50)
print("TASK 14: EXPORT REPORTS")
print("=" * 50)

customer_report = customer_revenue.reset_index()
customer_report.columns = ["Customer", "Total Revenue"]
customer_report.to_csv("customer_report.csv", index=False)

product_report = product_revenue.reset_index()
product_report.columns = ["Product", "Revenue"]
product_report.to_csv("product_report.csv", index=False)

print("customer_report.csv generated")
print("product_report.csv generated")

print("\n" + "=" * 50)
print("TASK 15: FINAL BUSINESS REPORT")
print("=" * 50)

top_category = category_revenue.idxmax()
top_city = city_revenue.idxmax()

print("E-COMMERCE SALES REPORT")
print("=" * 50)
print("Total Orders :", len(df))
print("Total Revenue :", total_revenue)
print("Average Revenue :", average_revenue)
print("Top Customer :", top_customer)
print("Customer Revenue :", customer_revenue.max())
print("Top Product :", top_product)
print("Product Revenue :", product_revenue.max())
print("Top Category :", top_category)
print("Category Revenue :", category_revenue.max())
print("Top City :", top_city)
print("City Revenue :", city_revenue.max())
print("=" * 50)
print("END OF REPORT")
print("=" * 50)

print("\n" + "=" * 50)
print("BONUS: REVENUE PERCENTAGE CONTRIBUTION")
print("=" * 50)

percentage = (product_revenue / total_revenue * 100).round(2)

for product, pct in percentage.sort_values(ascending=False).items():
    print(f"{product} = {pct}%")