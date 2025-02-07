first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = f"{first_name} {last_name}"

full_name_upper = full_name.upper()
full_name_lower = full_name.lower()

name_length = len(full_name)

print(f"Full Name: {full_name}")
print(f"Full Name (Upper Case): {full_name_upper}")
print(f"Full Name (Lower Case): {full_name_lower}")
print(f"Length of Full Name: {name_length}")