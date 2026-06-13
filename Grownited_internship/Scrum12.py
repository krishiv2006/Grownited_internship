temperatures = []

with open("temperature.txt", "r") as file:
    for line in file:
        temperatures.append(float(line.strip()))

highest_temp = max(temperatures)
hottest_day = temperatures.index(highest_temp) + 1

print("Hottest Day:", hottest_day)
print("Temperature:", highest_temp)