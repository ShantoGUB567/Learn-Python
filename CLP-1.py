# Write a python program to find the second highest number from a set of numbers.
# numbers = list(map(int, input("Enter a list of numbers: ").split()))
# print("List :" + str(numbers))
# highest = secondHighest = float('-inf')
# for num in numbers:
#     if num > highest:
#         secondHighest, highest = highest, num
#     elif secondHighest < num < highest:
#         secondHighest = num

# print("Second highest number is: ", secondHighest)


# [34,45,56,34,75,34,67,34,56,24,56,86,78] 


# 1. Write a program that takes an input string of parentheses ()[]{} and determines whether the expression is balanced or not.
# Input: [{[()]}]
# Output: Balanced
# Input: [{({}])}
# Output: Not balanced

expression = input("Enter a string of parentheses: ")
print(expression)

stack = []
matching_parentheses = {')': '(', '}': '{', ']': '['}
balanced = True

for char in expression:
    if char in "({[":
        stack.append(char)
    elif char in ")}]": 
        if stack and stack[-1] == matching_parentheses[char]:
            stack.pop()
        else:
            balanced = False
            break

if balanced and not stack:
    print("Balanced")
else:
    print("Not balanced")
