#Assume that the user’s input will be formatted as "x y z", with one space between x and y and one space between y and z

# x is an integer
# y is +, -, *, or /
# z is an integer

# If the user inputs 1 + 1, your program should output 2.0
# Assume that, if y is /, then z will not be 0.
# Use x, y, z = expression.split(" ")

x,y,z = input("Expression: ").split() #splits into list
x,z = float(x),float(z) 

if y == "+": # + operation
    value = x + z 

elif y == "-": # - operation
    value = x - z 

elif y =="*": # * operation
    value = x * z

else:
    value = x / z


print(round(value,1))