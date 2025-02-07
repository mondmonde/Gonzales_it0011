import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "students.txt")

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    print("Reading Student Information:")
    for line in lines:
        print(line.strip())
except FileNotFoundError:
    print(f"Error: The file 'students.txt' was not found in {script_dir}. Please check the file location.")
