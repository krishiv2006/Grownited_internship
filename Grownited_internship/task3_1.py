import pandas as pd

with open("employee.csv", "w") as f:
    f.write("""EmpID,Name,Department,Salary
1,Raj,IT,50000
2,Neha,HR,45000
3,Amit,IT,65000
4,Priya,HR,55000
5,Rahul,Sales,70000""")

df = pd.read_csv("employee.csv")

print("===== ALL EMPLOYEES =====")
print(df)

print("\n===== HIGHEST PAID EMPLOYEE =====")
highest_salary = df["Salary"].max()
print(df[df["Salary"] == highest_salary])

print("\n===== LOWEST PAID EMPLOYEE =====")
lowest_salary = df["Salary"].min()
print(df[df["Salary"] == lowest_salary])

print("\n===== AVERAGE SALARY =====")
average_salary = df["Salary"].mean()
print("Average Salary:", average_salary)

print("\n===== EMPLOYEES EARNING ABOVE AVERAGE SALARY =====")
print(df[df["Salary"] > average_salary])

print("\n===== DEPARTMENT-WISE AVERAGE SALARY =====")
dept_avg_salary = df.groupby("Department")["Salary"].mean()
print(dept_avg_salary)

print("\n===== EMPLOYEE COUNT PER DEPARTMENT =====")
dept_count = df.groupby("Department")["EmpID"].count()
print(dept_count)

print("\n===== EMPLOYEES SORTED BY SALARY =====")
sorted_df = df.sort_values(by="Salary", ascending=False)
print(sorted_df)