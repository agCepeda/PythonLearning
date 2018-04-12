# Declaring and assigning value to a variable
fruit = "Orange"

print(fruit)

# Changing the value of the variable
fruit = "Apple"

print(fruit)


# Declaring and assigning values to multiple variables
tool, meat, animal = "Chain", "Ribeye", "Dog"

print(tool)
print(meat)
print(animal)

# You can assign whichever type of value to a variable
tool, meat, animal = 1, "rojo", 4.45

print(tool)
print(meat)
print(animal)

# Definition and assignation of constant value
WATER_BOILING_POINT = "100 C"
print(WATER_BOILING_POINT)

# You can change the value of a "constant" since python doesn't have
# a mechanism to declare them. So you have to keep in mind you 
# must not change the values of the variables declared as "constants"
WATER_BOILING_POINT = "50 C"
print(WATER_BOILING_POINT)