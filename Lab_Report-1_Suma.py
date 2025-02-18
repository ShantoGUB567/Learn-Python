# numbers = [10, 20, 4, 45, 99, 99, 5]
# unique_numbers = list(set(numbers))
# unique_numbers.sort(reverse=True)  
# if len(unique_numbers) > 1:
#     print("Second highest number:", unique_numbers[1])
# else:
#     print("No second highest number")


# Example Usage
expressions = ["[{[()]}]", "[{({}])}"]

for expression in expressions:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    balanced = True
    
    for char in expression:
        if char in bracket_map.values():  # If opening bracket, push to stack
            stack.append(char)
        elif char in bracket_map.keys():  # If closing bracket, check matching
            if not stack or stack.pop() != bracket_map[char]:
                balanced = False
                break
    
    if stack:
        balanced = False
    
    print(f"Input: {expression}\nOutput: {'Balanced' if balanced else 'Not Balanced'}\n")