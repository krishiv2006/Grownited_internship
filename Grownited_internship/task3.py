import pandas as pd

with open("student.csv", "w") as f:
    f.write("""RollNo,Name,Department,Marks,Attendance
101,Amit,IT,75,90
102,Neha,CE,92,95
103,Rahul,IT,88,80
104,Priya,CE,65,72
105,Jay,IT,45,60
106,Riya,IT,95,98
107,Karan,CE,55,70
108,Sneha,IT,84,85""")

df = pd.read_csv("student.csv")

print("===== ALL STUDENTS =====")
print(df)

print("\n===== HIGHEST MARKS =====")
highest = df["Marks"].max()
print("Highest Marks:", highest)
print(df[df["Marks"] == highest])

print("\n===== LOWEST MARKS =====")
lowest = df["Marks"].min()
print("Lowest Marks:", lowest)
print(df[df["Marks"] == lowest])

print("\n===== AVERAGE MARKS =====")
average = df["Marks"].mean()
print("Average Marks:", round(average, 2))

print("\n===== STUDENTS SCORING ABOVE 80 =====")
print(df[df["Marks"] > 80])

print("\n===== STUDENTS SCORING BELOW AVERAGE =====")
print(df[df["Marks"] < average])

print("\n===== PASS AND FAIL COUNT =====")
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")
print(df["Result"].value_counts())

print("\n===== SORTED BY MARKS (DESCENDING) =====")
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)

print("\n===== DEPARTMENT-WISE AVERAGE MARKS =====")
dept_avg = df.groupby("Department")["Marks"].mean()
print(dept_avg)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== FINAL REPORT =====")
print("Total Students :", len(df))
print("Highest Marks  :", highest)
print("Lowest Marks   :", lowest)
print("Average Marks  :", round(average, 2))
print("Pass Students  :", (df["Result"] == "Pass").sum())
print("Fail Students  :", (df["Result"] == "Fail").sum())