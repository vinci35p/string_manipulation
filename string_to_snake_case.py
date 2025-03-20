# Input full name in incorrect casing
user_name = str(input("Enter your full name in incorrect casing: "))

# Turn inputted name into snake case
snake_case_name = user_name.lower().replace(" ", "_")

# Print snake cased name
print(snake_case_name)