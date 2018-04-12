# Constants, Variables and Literals

In this "lesson" will show how to declare and handle variables, constants and literals.
What is the difference between them? I will explain that.

The constants are inmutables references that always has the same value which was assigned in its declaration.
Variables are mutable references that can change the its value through the execution of the program.
Literals are values written directly in the code.

## Variables

To declare a variable you will use the "=" operator and then put the value that you want to assign.

```python
# Declaring and assigning value to a variable
fruit = "Orange"

print(fruit)

# Changing the value of the variable
fruit = "Apple"

print(fruit)
```

To declare multiple variables you must to write first the names of the variables splitted by "," then the "=" operator and finally the values of the variables splitted by ","

```python
# Declaring and assigning values to multiple variables
tool, meat, animal = "Chain", "Ribeye", "Dog"

print(tool)
print(meat)
print(animal)
```

You can change assign whatever type of value to a variable since python has a dynamic typing

```python
# Declaring and assigning value to a variable
fruit = "Orange"

print(fruit)

# Changing the value of the variable
fruit = "Apple"

print(fruit)
```

```python
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
```

## Constants

Python doesn't have a mechanism to create constants so the python developers use the capitalization to recognize a constant.

So if you have to declare a constant you will declare it in the same way that you declare a variable. Just you have to write the name of the constant in uppercase and if it has more than one word you have to split them by low dash "_".

```python
# Definition and assignation of constant value
WATER_BOILING_POINT = "100 C"
print(WATER_BOILING_POINT)

# You can change the value of a "constant" since python doesn't have
# a mechanism to declare them. So you have to keep in mind you 
# must not change the values of the variables declared as "constants"
WATER_BOILING_POINT = "50 C"
print(WATER_BOILING_POINT)
```

Literals

We don't have a lot to explain about this type of declaration. Just is write the value of something directly in the code.