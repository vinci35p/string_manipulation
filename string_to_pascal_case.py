# Input full name in incorrect casing
user_name = str(input("Enter your full name in incorrect casing: "))

# Turn inputted name into pascal case
pascal_name = user_name.title().replace(" ", "")

# Print pascal cased name
print(pascal_name)