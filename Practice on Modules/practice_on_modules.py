from datetime import datetime


#1. Getting the minimum and maximum representable DateTime object

# Minimum representable DateTime object
min_datetime = datetime.min
print("Minimum DateTime:", min_datetime)

# Maximum representable DateTime object
max_datetime = datetime.max
print("Maximum DateTime:", max_datetime)


#2. How to get today’s date using python module

# Getting Today's Datetime
today = datetime.now()
print("Getting Today's Datetime:", today)

# Accessing Attributes
print("Day: ", today.day)
print("Month: ", today.month)
print("Year: ", today.year)
print("Hour: ", today.hour)
print("Minute: ", today.minute)
print("Second: ", today.second)


#3. How to get DateTime from timestamp and ordinal

# Convert a timestamp to DateTime
timestamp = 1623765245  # Example timestamp
dt_from_timestamp = datetime.fromtimestamp(timestamp)
print("DateTime from timestamp:", dt_from_timestamp)

# Convert an ordinal to DateTime
ordinal = 737000  # Example ordinal value
dt_from_ordinal = datetime.fromordinal(ordinal)
print("DateTime from ordinal:", dt_from_ordinal)


#4. Write the Python code for getting a time object with the same specified hour, minute, second, microsecond, fold and tzinfo.

A = datetime(2023, 8, 3, 1, 2, 3, 500000)

B = A.timetz()

print("Original date time object:", A)

print("New time object:", B)


#5. How to replace the current date’s year with another year

# Get the current date
current_date = datetime.now().date()

# Specify the desired year
desired_year = 2025

# Replace the year with the desired year
updated_date = current_date.replace(year=desired_year)

# Print the updated date
print("Updated Date:", updated_date)


#6. Write a Python program to read datetime and get all time data using strptime


# Read the datetime string from user input
datetime_string = input("Enter the datetime (format: YYYY-MM-DD HH:MM:SS): ")

# Parse the datetime string using strptime
parsed_datetime = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")

# Extract and print the time data
print("Year:", parsed_datetime.year)
print("Month:", parsed_datetime.month)
print("Day:", parsed_datetime.day)
print("Hour:", parsed_datetime.hour)
print("Minute:", parsed_datetime.minute)
print("Second:", parsed_datetime.second)
print("Microsecond:", parsed_datetime.microsecond)
print("Timezone Offset:", parsed_datetime.utcoffset())


#7. Write a Python program to get UTC time stamp


A = datetime.now()

B = A.timetz()


#8. Write a Python program grabs the date using the DateTime module and tells the day of the date.

# Get the current date
current_date = datetime.now().date()

# Determine the day of the week
day_of_week = current_date.strftime("%A")

# Print the day of the week
print("Today is", day_of_week)


#9. Write gthe python program to get the current date using datetime.now()

# Get the current date
current_date = datetime.now().date()

# Print the current date
print("Current Date:", current_date)


#10. Consider a scenario in which we utilize a Christmas date.

# Create a datetime object for Christmas
christmas = datetime(2023, 12, 25)

# Get the properties of the Christmas datetime object
properties = (
    ('Year', christmas.year),
    ('Month', christmas.month),
    ('Day', christmas.day),
    ('Hour', christmas.hour),
    ('Minute', christmas.minute),
    ('Second', christmas.second),
    ('Microsecond', christmas.microsecond),
)

# Print the index and value of each property
for index, (property_name, property_value) in enumerate(properties):
    print(f"{index + 1}. {property_name}: {property_value}")