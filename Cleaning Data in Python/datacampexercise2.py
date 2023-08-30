# Print the information of ride_sharing.
# Use .describe() to print the summary statistics of the user_type column from ride_sharing.

import pandas as pd
import os

main_root_path = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(main_root_path, 'Dataset', 'ride_sharing_new.csv')

ride_sharing = pd.read_csv(dataset_path)

# Find duplicated rows of ride_id in the ride_sharing DataFrame while setting keep to False.
# Subset ride_sharing on duplicates and sort by ride_id and assign the results to duplicated_rides.
# Print the ride_id, duration and user_birth_year columns of duplicated_rides in that order.

# Find duplicates
duplicates = ride_sharing.duplicated(subset = ['ride_id'], keep = False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])

# ---------------------------------------------------------------------------------------

# Drop complete duplicates in ride_sharing and store the results in ride_dup.
# Create the statistics dictionary which holds minimum aggregation for user_birth_year and mean aggregation for duration.
# Drop incomplete duplicates by grouping by ride_id and applying the aggregation in statistics.
# Find duplicates again and run the assert statement to verify de-duplication.

# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0
