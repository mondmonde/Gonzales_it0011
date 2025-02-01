#A program that will count the sum of the digits from a given input string digits. (use for loop and some operators under module 1 and 2)
def sum_of_digits(input_string):
    total_sum = 0

    for char in input_string:
        if char.isdigit():
            total_sum += int(char)
    
    return total_sum

input_string = input("Enter a string containing digits: ")


sum_digits = sum_of_digits(input_string)


print(f"The sum of the digits in the input string is: {sum_digits}")
