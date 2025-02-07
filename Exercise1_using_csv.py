import csv
import math
# Open the original CSV file for reading
with open('/home/nineleaps/Python_training/data/Sales_24.csv', mode='r', newline='') as infile:
    reader = csv.DictReader(infile)
    # Get the fieldnames (column headers) from the original file
    fieldnames = reader.fieldnames
    # Open a new CSV file to write the updated data
    with open('sales_updated.csv', mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # Write the header to the new file
        writer.writeheader()
        # Iterate through each row in the original CSV
        for row in reader:
            # Check if 'Amount' exists and is a valid number, otherwise leave it as is
            if row['Amount']:
                try:
                    # Round down the value in the 'Amount' column to the nearest integer
                    row['Amount'] = math.floor(float(row['Amount']))
                except ValueError:
                    pass  # If conversion fails, skip modification
            # Write the modified row to the new file
            writer.writerow(row)
print("Sales data has been updated and saved in 'sales_updated.csv'.")