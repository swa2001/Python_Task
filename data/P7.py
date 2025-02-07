import pandas as pd
import sys

# Check if city name is provided
if len(sys.argv) < 2:
    print("Error: Please provide a city name as a command-line argument.")
    print("Usage: python script.py <CityName>")
    sys.exit(1)

# Get the city name from command-line argument
city_name = sys.argv[1]

# Load the dataset (Ensure the file exists in the same folder)
df = pd.read_excel("cleaned_data.xlsx")

# Convert city column to lowercase for case-insensitive matching
df["City"] = df["City"].str.lower()
city_name = city_name.lower()

# Filter data for the given city
city_df = df[df["City"] == city_name]

# Check if any data exists for the city
if city_df.empty:
    print(f"No data found for city: {sys.argv[1]}")
    sys.exit(1)

# Best type of room based on highest reviews
best_room = city_df.loc[city_df["Reviews"].idxmax(), "PType"]

# Cheapest room
cheapest_room = city_df.nsmallest(1, "PPN").iloc[0]

# Costliest room
costliest_room = city_df.nlargest(1, "PPN").iloc[0]

# Average price per night
average_price = city_df["PPN"].mean()

# Display the results
print(f"\nCity: {sys.argv[1]}")
print(f"Best type of Room based on Reviews: {best_room}")
print(f"Cheapest Room: Type - {cheapest_room['PType']}, Location - {cheapest_room['Location ']}, Price - {cheapest_room['PPN']}")
print(f"Costliest Room: Type - {costliest_room['PType']}, Location - {costliest_room['Location ']}, Price - {costliest_room['PPN']}")
print(f"Average Price Per Night: {average_price:.2f}")
