# Write a python program to find the second highest number from a set of numbers.
numbers = list(map(int, input("Enter a list of numbers: ").split()))
print("List :" + str(numbers))
highest = secondHighest = numbers[1]
for num in numbers:
    if num > highest:
        secondHighest = highest
        highest = num

print("Second highest number is: ", secondHighest)


# [34,45,56,34,75,34,67,34,56,24,56,86,78] 