# Print the information of ride_sharing.
# Use .describe() to print the summary statistics of the user_type column from ride_sharing.

import pandas as pd
import os

main_root_path = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(main_root_path, 'Dataset', 'ride_sharing_new.csv')

ride_sharing = pd.read_csv(dataset_path)
print(ride_sharing.head())

print(ride_sharing.info())

print(ride_sharing['user_type'].describe())

# Convert user_type into categorical by assigning it the 'category' data type and store it in the user_type_cat column.
# Make sure you converted user_type_cat correctly by using an assert statement.

ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

assert ride_sharing['user_type_cat'].dtype == 'category'



# Use the .strip() method to strip duration of "minutes" and store it in the duration_trim column.
# Convert duration_trim to int and store it in the duration_time column.
# Write an assert statement that checks if duration_time's data type is now an int.
# Print the average ride duration.

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])

print(ride_sharing['duration_time'].mean())

# Convert the tire_sizes column from category to 'int'.
# Use .loc[] to set all values of tire_sizes above 27 to 27.
# Reconvert back tire_sizes to 'category' from int.
# Print the description of the tire_sizes.


# Convert tire_sizes to integer
# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

# Convert ride_date to a datetime object using to_datetime(), then convert the datetime object into a date and store it in ride_dt column.
# Create the variable today, which stores today's date by using the dt.date.today() function.
# For all instances of ride_dt in the future, set them to today's date.
# Print the maximum date in the ride_dt column.

# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())