import statistics

# Input numbers
numbers = [10, 20, 30, 40, 50]

print("Numbers:", numbers)

# Arithmetic calculations
total = sum(numbers)
average = total / len(numbers)
avg = statistics.mean(numbers)
minimum = min(numbers)
maximum = max(numbers)

print("\n--- Arithmetic Calculations ---")
print("Sum :", total)
print("Average :", average)
print("Minimum :", minimum)
print("Maximum :", maximum)

# Statistical calculations
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
std_deviation = statistics.stdev(numbers)

print("\n--- Statistical Calculations ---")
print("Mean :", mean_value)
print("Median :", median_value)
print("Standard Deviation :", round(std_deviation, 2))