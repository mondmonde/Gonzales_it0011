#1. A program that will display the number of vowels, consonants, spaces, and other characters given an input string. (use for loop and some operators under module 1 and 2)
def count_characters(input_string):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    consonant_count = 0
    space_count = 0
    other_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    return vowel_count, consonant_count, space_count, other_count


input_string = input("Enter a string: ")

vowel_count, consonant_count, space_count, other_count = count_characters(input_string)

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
print(f"Number of spaces: {space_count}")
print(f"Number of other characters: {other_count}")

