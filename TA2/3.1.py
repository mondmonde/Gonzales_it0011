first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

full_name = f"{first_name} {last_name}"


sliced_name = first_name[:3]

greeting_message = f"Hello, {sliced_name}! Welcome. You are {age} years old."

print(f"Full Name: {full_name}")
print(f"Sliced Name: {sliced_name}")
print(f"Greeting Message: {greeting_message}")