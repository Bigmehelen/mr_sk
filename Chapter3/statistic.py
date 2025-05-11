import statistics

data = [9, 11, 22, 34, 17, 22, 34, 22, 40]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("The mean is %.2f" %mean)
print(f"The median is {median}")
print(f"The mode is {mode}")