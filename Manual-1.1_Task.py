# Write a python program to find the sum of odd and even numbers from a set of numbers.
print("")
oddSum = evenSum = 0
for num in range(1,101):
    if num % 2 == 0:
        evenSum += num
    else : 
        oddSum += num
    
print("Sum of odd numbers: ", oddSum)
print("Sum of even numbers: ", evenSum)
print("")


# Write a python program to find the smallest number from a set of numbers.
numbers = [34,45,56,34,75,34,67,34,56,24,56,86,78]
small = numbers[1]
for num in numbers:
    if num < small:
        small = num

print("Smallest number is: ", small)
print("")


# Write a python program to find the sum of all numbers between 50 and 100, which are divisible by 3 and not divisible by 5.
sum = 0
for i in range(50, 100):
    if i % 3 == 0 and i % 5 != 0:
        sum += i
print("Sum: ", sum)
print("")


# Write a python program to find the second highest number from a set of numbers.
numbers = [34,45,56,34,75,34,67,34,56,24,56,86,78]
highest = secondHighest = numbers[1]
for num in numbers:
    if num > highest:
        secondHighest = highest
        highest = num

print("Second highest number is: ", secondHighest)
print("")


# Write a python program to find the factorial of a number using for loop.
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)
print("")


# Write a python program to generate Fibonacci series.
num1= 0
num2 = 1
fib_series = []
for i in range(10):
    fib_series.append(num1)
    num1, num2 = num2, num1 + num2
print("Fibonacci series: ", fib_series)

print("")
