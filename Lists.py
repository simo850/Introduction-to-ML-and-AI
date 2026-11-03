# Introduction to Python Lists

# Creating a list
languages = ["Python", "Java", "C++", "JavaScript", "C"]

# Display the entire list
print("Programming languages:", languages)

# Accessing list items
print("First language:", languages[0])
print("Second language:", languages[1])

# Adding an item
languages.append("PHP")
print("After adding PHP:", languages)

# Removing an item
languages.remove("Java")
print("After removing Java:", languages)

# Changing an item
languages[0] = "Python 3"
print("Updated list:", languages)

# Finding the number of items
print("Total languages:", len(languages))

# Looping through a list
print("Available programming languages:")

for language in languages:
    print(language)
