sales = []

with open("sales.txt", "r") as file:
    for line in file:
        sales.append(float(line.strip()))

q1 = sum(sales[0:3])
q2 = sum(sales[3:6])
q3 = sum(sales[6:9])
q4 = sum(sales[9:12])

quarters = [q1, q2, q3, q4]

highest_sales = max(quarters)
highest_quarter = quarters.index(highest_sales) + 1

print("Quarter with Highest Sales:", highest_quarter)
print("Sales:", highest_sales)