# Input number 1-1000.
user_num = int(input("Enter number 1-1000: "))

# Add zeros at beginning of number to make it 6 digits. Print 6-digit number.
if 1 <= user_num <= 1000:
    print(str(user_num).zfill(6))

# Remind user if inputted number is greater than 1000.
else:
    print("Number inputted should be 1-1000")