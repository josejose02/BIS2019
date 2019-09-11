import math
print("Hello {}!".format(input("Input your name, please: ")))

print("\nEnter two numbers.")
number_one = float(input("Number one: "))
number_two = float(input("Number two: "))
division = number_one / number_two
print("The rounded up division is: {}".format(math.ceil(division)))

radius = float(input("\nPlease enter a radius: "))
print("The area is {} m2".format(math.pi * radius ** 2))

print("\nCalculator 2: Electric Boogaloo")
operation = input(">> ")
print(eval(operation))