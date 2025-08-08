# Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
# Tasks: 
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
# Calculate the 75th percentile of the rainfall data and identify values above it. (help : use numpy.percentile())
import numpy as np

rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

rainfallArray = np.array(rainfall)

print('rainfall', rainfallArray)
print('total', np.sum(rainfallArray))
print('average', np.mean(rainfallArray))
print('count of days has no rain', np.where(rainfallArray == 0)[0].__len__())
print('days more than 5', np.where(rainfallArray > 5)[0])
print('75th percentile', np.percentile(rainfallArray, 75))