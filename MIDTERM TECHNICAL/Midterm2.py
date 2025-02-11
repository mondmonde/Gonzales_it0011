import datetime

def convert_date_format(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
        readable_date = date_obj.strftime("%B %d, %Y")
        print(f"Date Output: {readable_date}")
    except ValueError:
        print("Invalid date format. Please enter in mm/dd/yyyy format.")

date_input = input("Enter the date (mm/dd/yyyy): ")
convert_date_format(date_input)
