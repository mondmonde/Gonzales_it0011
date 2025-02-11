import os

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_numbers_file(filename):
    try:
        print("Current Working Directory:", os.getcwd())

        if not os.path.exists(filename):
            print("Error: File not found.")
            return

        with open(filename, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(",")))
            total_sum = sum(numbers)
            result = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
            print(f"Line {i}: {line.strip()} (sum {total_sum}) - {result}")

    except Exception as e:
        print(f"An error occurred: {e}")

file_path = r"C:\Users\ADMIN\Documents\GitHub\Gonzales_it0011\MIDTERM TECHNICAL\numbers.txt"
process_numbers_file(file_path)
