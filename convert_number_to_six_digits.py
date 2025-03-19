# Input number 1-1000.
user_num = int(input("Enter number 1-1000: "))

# Add zeros at beginning of number to make it 6 digits.
num_count = len(str(user_num))
if num_count == 1:
    print(f"00000{user_num}")
elif num_count == 2:
    print(f"0000{user_num}")
elif num_count == 3:
    print(f"000{user_num}")
elif num_count == 4:
    if user_num <= 1000:
        print(f"00{user_num}")
    else:
        print("Number inputted should be 1-1000")

# Print 6-digit number.