import string
from collections import Counter

excluded_words = {
    "and", "but", "or", "nor", "for", "so", "yet", 
    "a", "an", "the", 
    "of"
}

def process_string(input_str):
    words = input_str.split()
    words = [word.strip(string.punctuation).lower() for word in words]
    filtered_words = [word for word in words if word not in excluded_words]

    word_count = Counter(filtered_words)
    sorted_word_count = sorted(word_count.items())

    for word, count in sorted_word_count:
        print(f"{word.capitalize()}       - {count}")

    print(f"Total words filtered: {sum(word_count.values())}")

input_statement = input("Enter a string statement: ")
process_string(input_statement)
