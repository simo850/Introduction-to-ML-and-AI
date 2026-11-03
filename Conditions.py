# Introduction to Python Conditions

# Example 1: Simple if statement

age = 20

if age >= 18:
    print("You are an adult.")


# Example 2: if and else

number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Example 3: if, elif and else

marks = 75

if marks >= 70:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade E")


# Example 4: User input

temperature = float(input("Enter temperature: "))

if temperature > 30:
    print("It is hot.")
elif temperature >= 20:
    print("The temperature is moderate.")
else:
    print("It is cold.")


# Example 5: Comparing two numbers

num1 = 25
num2 = 40

if num1 > num2:
    print("First number is greater.")
elif num1 < num2:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")
