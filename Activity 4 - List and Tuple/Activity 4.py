import os
import pickle
from typing import List, Tuple

StudentRecord = Tuple[int, Tuple[str, str], float, float]

class StudentManager:
    def __init__(self):
        self.records = []
        self.folder_name = "Activity 4 - List and Tuple"
        self.current_file = "Student Records"
        
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)
    
    def get_file_path(self, filename=None):
        if filename is None:
            filename = self.current_file
        return os.path.join(self.folder_name, filename)
    
    def open_file(self, filename=None):
        if filename is None:
            filename = self.current_file
        
        file_path = self.get_file_path(filename)
            
        if os.path.exists(file_path):
            try:
                with open(file_path, 'rb') as file:
                    self.records = pickle.load(file)
                self.current_file = filename
                print(f"Opened file with {len(self.records)} records.")
                return True
            except Exception as e:
                print(f"Error opening file: {e}")
                return False
        else:
            print(f"File {filename} not found. Creating a new file.")
            self.records = []
            self.current_file = filename
            return True
    
    def save_file(self):
        try:
            file_path = self.get_file_path()
            with open(file_path, 'wb') as file:
                pickle.dump(self.records, file)
            print(f"Saved {len(self.records)} records to {self.current_file}")
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def save_as_file(self, filename):
        try:
            file_path = self.get_file_path(filename)
            with open(file_path, 'wb') as file:
                pickle.dump(self.records, file)
            self.current_file = filename
            print(f"Saved {len(self.records)} records to {filename}")
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def show_all_records(self):
        if not self.records:
            print("No records to display.")
            return
        
        print("\nAll Student Records:")
        print("-" * 80)
        print(f"{'ID':<12} {'Name':<30} {'Class Standing':<15} {'Major Exam':<12} {'Final Grade':<10}")
        print("-" * 80)
        
        for record in self.records:
            student_id, (first_name, last_name), class_standing, major_exam = record
            final_grade = self.calculate_grade(class_standing, major_exam)
            print(f"{student_id:<12} {first_name} {last_name:<25} {class_standing:<15.2f} {major_exam:<12.2f} {final_grade:<10.2f}")
        print("-" * 80)
    
    def order_by_last_name(self):
        if not self.records:
            print("No records to display.")
            return
        
        sorted_records = sorted(self.records, key=lambda x: x[1][1])
        
        print("\nStudent Records Ordered by Last Name:")
        print("-" * 80)
        print(f"{'ID':<12} {'Name':<30} {'Class Standing':<15} {'Major Exam':<12} {'Final Grade':<10}")
        print("-" * 80)
        
        for record in sorted_records:
            student_id, (first_name, last_name), class_standing, major_exam = record
            final_grade = self.calculate_grade(class_standing, major_exam)
            print(f"{student_id:<12} {first_name} {last_name:<25} {class_standing:<15.2f} {major_exam:<12.2f} {final_grade:<10.2f}")
        print("-" * 80)
    
    def order_by_grade(self):
        if not self.records:
            print("No records to display.")
            return
        
        sorted_records = sorted(
            self.records, 
            key=lambda x: self.calculate_grade(x[2], x[3]),
            reverse=True
        )
        
        print("\nStudent Records Ordered by Grade (Highest to Lowest):")
        print("-" * 80)
        print(f"{'ID':<12} {'Name':<30} {'Class Standing':<15} {'Major Exam':<12} {'Final Grade':<10}")
        print("-" * 80)
        
        for record in sorted_records:
            student_id, (first_name, last_name), class_standing, major_exam = record
            final_grade = self.calculate_grade(class_standing, major_exam)
            print(f"{student_id:<12} {first_name} {last_name:<25} {class_standing:<15.2f} {major_exam:<12.2f} {final_grade:<10.2f}")
        print("-" * 80)
    
    def show_student_record(self):
        student_id = self.get_student_id("Enter student ID to display: ")
        if student_id is None:
            return
        
        record = self.find_record_by_id(student_id)
        if record:
            student_id, (first_name, last_name), class_standing, major_exam = record
            final_grade = self.calculate_grade(class_standing, major_exam)
            
            print("\nStudent Record:")
            print("-" * 50)
            print(f"Student ID: {student_id}")
            print(f"Name: {first_name} {last_name}")
            print(f"Class Standing: {class_standing:.2f}")
            print(f"Major Exam: {major_exam:.2f}")
            print(f"Final Grade: {final_grade:.2f}")
            print("-" * 50)
        else:
            print(f"No student found with ID {student_id}")
    
    def add_record(self):
        try:
            student_id = self.get_student_id("Enter student ID (9 digits): ")
            if student_id is None:
                return
                
            if self.find_record_by_id(student_id):
                print("This student ID already exists. Please use a different ID.")
                return
            
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            
            class_standing = self.get_grade("Enter class standing (0-100): ")
            if class_standing is None:
                return
                
            major_exam = self.get_grade("Enter major exam grade (0-100): ")
            if major_exam is None:
                return
            
            record = (student_id, (first_name, last_name), class_standing, major_exam)
            self.records.append(record)
            print(f"Added record for {first_name} {last_name}")
                
        except Exception as e:
            print(f"Error adding record: {e}")
    
    def edit_record(self):
        student_id = self.get_student_id("Enter student ID to edit: ")
        if student_id is None:
            return
            
        record = self.find_record_by_id(student_id)
        if not record:
            print(f"No student found with ID {student_id}")
            return
            
        old_id, (old_first, old_last), old_class, old_exam = record
        
        print(f"\nEditing record for {old_first} {old_last}")
        print("(Press Enter to keep current values)")
        
        first_name = input(f"Enter first name [{old_first}]: ") or old_first
        last_name = input(f"Enter last name [{old_last}]: ") or old_last
        
        class_standing_str = input(f"Enter class standing [{old_class}]: ")
        if class_standing_str:
            class_standing = self.get_grade("", class_standing_str)
            if class_standing is None:
                return
        else:
            class_standing = old_class
            
        major_exam_str = input(f"Enter major exam grade [{old_exam}]: ")
        if major_exam_str:
            major_exam = self.get_grade("", major_exam_str)
            if major_exam is None:
                return
        else:
            major_exam = old_exam
        
        index = self.records.index(record)
        self.records[index] = (student_id, (first_name, last_name), class_standing, major_exam)
        print(f"Updated record for {first_name} {last_name}")
    
    def delete_record(self):
        student_id = self.get_student_id("Enter student ID to delete: ")
        if student_id is None:
            return
            
        record = self.find_record_by_id(student_id)
        if not record:
            print(f"No student found with ID {student_id}")
            return
            
        student_id, (first_name, last_name), _, _ = record
        confirm = input(f"Are you sure you want to delete the record for {first_name} {last_name}? (y/n): ")
        
        if confirm.lower() == 'y':
            self.records.remove(record)
            print(f"Deleted record for {first_name} {last_name}")
    
    def find_record_by_id(self, student_id):
        for record in self.records:
            if record[0] == student_id:
                return record
        return None
    
    def get_student_id(self, prompt):
        while True:
            student_id = input(prompt)
            if student_id.isdigit() and len(student_id) == 9:
                return int(student_id)
            else:
                print("Student ID must be a 9-digit number.")
                retry = input("Try again? (y/n): ")
                if retry.lower() != 'y':
                    return None
    
    def get_grade(self, prompt, value=None):
        while True:
            try:
                if value is None:
                    grade = float(input(prompt))
                else:
                    grade = float(value)
                    
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
                
            if value is not None:
                return None
                
            retry = input("Try again? (y/n): ")
            if retry.lower() != 'y':
                return None
    
    @staticmethod
    def calculate_grade(class_standing, major_exam):
        return (class_standing * 0.6) + (major_exam * 0.4)

def main():
    manager = StudentManager()
    
    manager.open_file()
    
    while True:
        print("\n===== Student Record Management System =====")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-10): ")
        
        if choice == '1':
            filename = input("Enter filename to open: ")
            manager.open_file(filename)
            
        elif choice == '2':
            manager.save_file()
            
        elif choice == '3':
            filename = input("Enter filename to save as: ")
            manager.save_as_file(filename)
            
        elif choice == '4':
            manager.show_all_records()
            
        elif choice == '5':
            manager.order_by_last_name()
            
        elif choice == '6':
            manager.order_by_grade()
            
        elif choice == '7':
            manager.show_student_record()
            
        elif choice == '8':
            manager.add_record()
            
        elif choice == '9':
            manager.edit_record()
            
        elif choice == '10':
            manager.delete_record()
            
        elif choice == '0':
            save_prompt = input("Save changes before exiting? (y/n): ")
            if save_prompt.lower() == 'y':
                manager.save_file()
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()