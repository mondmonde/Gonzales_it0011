import csv

def load_currency_data(file_path):
    currency_data = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                currency_data[row['code']] = {
                    'name': row['name'],
                    'rate': float(row['rate'])
                }
        return currency_data
    except Exception as e:
        print(f"Error loading currency data: {e}")
        return {}

def convert_currency(amount, currency_data, target_code):
    if target_code not in currency_data:
        return None
    return amount * currency_data[target_code]['rate']

def main():
    file_path = r"C:\Users\ADMIN\Documents\GitHub\Gonzales_it0011\Laboratory Activity 4B - Set and Dictionary\currency.csv"
    currency_data = load_currency_data(file_path)
    
    if not currency_data:
        print("Failed to load currency data. Please check if the file exists.")
        return
    
    try:
        amount = float(input("How much dollar do you have\? "))
        target_code = input("What currency you want to have? ").upper()
        
        if target_code in currency_data:
            converted_amount = convert_currency(amount, currency_data, target_code)
            print(f"\nDollar: {amount} USD")
            print(f"{currency_data[target_code]['name']}: {converted_amount}")
        else:
            print(f"Currency code {target_code} not found.")
            
    except ValueError:
        print("Please enter a valid number for the dollar amount.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()