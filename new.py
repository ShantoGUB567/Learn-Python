import sys
print("Hello Shahriar Shanto")

print(sys.version)  #python version

# Variable
x = 5
y = "Shanto"
z = 10
print(x)
print(y)
print(x,y)
print(type(x))
print(type(y))

x = str(3) # convert integer to string. x = "3"
print(type(x))

a = 567
print(a)
a = 555
print(a) # variable can be changed

# Multiple Assign
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
print(a,b,c)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("shanto")

print(x,y,z)
print(x + y + z)

a = 230
b = 320
print(a + b)

# Without walrus operator
n = 10
if n > 5:
    print(n)

# With walrus operator
if (n := 1) > 5:
    print(n)  # Output: 10

