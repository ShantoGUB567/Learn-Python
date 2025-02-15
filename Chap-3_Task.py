# 1. Write a program to display a user name followed by Good Afternoon using input() function. 
name = input("Enter your name: ")
print("Good Afternoon, " + name) 

# 2. Write a program to fill in a letter template given bellow wint name and date.
'''Letter = Dear <Name>,
you are selected !
<Date>'''
name = input("Enter your name: ")
date = input("Enter date (dd-mm-yyyy): ")
print(f"""
Dear {name},
you are selected !
{date}""")

# 3. Write a program to detect double space in a sting.
input = input("Input a string: ")
if "  " in input:
    print("Double space found")
else: 
    print("No double space found")

# 4. Replace the double space from problem 3 with single space.
print(input.replace("  ", " "))

# 5. Write a program to formate the following letter using escape sequence charachters. 
print("Dear Shanto, \nthis python course is nice. \n\t\tThanks! ")
