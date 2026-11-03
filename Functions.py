# Introduction to Python Functions

# Function 1: Display a welcome message

def welcome():
    print("Welcome to Python Programming!")
    print("Learning functions is exciting.")


# Calling the function
welcome()


# Function 2: Add two numbers

def add_numbers(a, b):
    result = a + b
    return result


answer = add_numbers(10, 20)

print("The sum is:", answer)


# Function 3: Calculate the average

def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average


result = calculate_average(70, 80, 90)

print("The average is:", result)


# Function 4: Check whether a number is even or odd

def check_number(number):

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


check_number(10)
check_number(7)
