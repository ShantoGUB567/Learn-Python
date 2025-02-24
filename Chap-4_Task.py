# 1. Write a program to store seven fruits in a list entered by the user. 
fruits = []
for fruit in range(7):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)

print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner. 
Marks = []
for i in range(6):
    mark = int(input("Enter mark: "))
    Marks.append(mark)
Marks.sort()
print("Marks: ", Marks)

# 3. Check that a type cannot be changed in python. 
a = 10
print(type(a))
a = float(a)
print(type(a))

# 4. Write a program to sum a list with 4 numbers. 
numbers = [69, 85, 90, 78]
print("Sum of the numbers in the list is: ", sum(numbers))

# 5. Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)
a = (7, 0, 8, 0, 0, 9)
print("Number of zeros in the tuple is: ", a.count(0))