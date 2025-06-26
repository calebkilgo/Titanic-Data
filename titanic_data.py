import numpy as np

passengers = np.array([
   [1, 0, 3, 22],
   [2, 1, 1, 38],
   [3, 1, 3, 26],
   [4, 1, 1, 35],
   [5, 0, 3, 35],
   [6, 0, 3, 18],
   [7, 0, 1, 54],
   [8, 0, 3, 2],
   [9, 1, 3, 27],
  [10, 1, 2, 14],
  [11, 1, 3, 4],
  [12, 1, 1, 58],
  [13, 0, 3, 20],
  [14, 0, 3, 39],
  [15, 0, 3, 14],
  [16, 1, 2, 55],
  [17, 0, 3, 2],
  [18, 1, 2, 12],
  [19, 0, 3, 31],
  [20, 1, 3, 8],
  [21, 0, 2, 35],
  [22, 1, 2, 34],
  [23, 1, 3, 15],
  [24, 1, 1, 28],
  [25, 0, 3, 8],
  [26, 1, 3, 38],
  [27, 0, 3, 2],
  [28, 0, 1, 1],
  [29, 1, 3, 5],
  [30, 0, 3, 18],
  [31, 0, 1, 40],
  [32, 1, 1, 70],
  [33, 1, 3, 33],
  [34, 0, 2, 66],
  [35, 0, 1, 28],
  [36, 0, 1, 42],
  [37, 1, 3, 5],
  [38, 0, 3, 18],
  [39, 0, 3, 18],
  [40, 1, 3, 14],
  [41, 0, 3, 40],
  [42, 0, 2, 27],
  [43, 0, 3, 29],
  [44, 1, 2, 0],
  [45, 1, 3, 19],
  [46, 0, 3, 33],
  [47, 0, 3, 14],
  [48, 1, 3, 22],
  [49, 0, 3, 41],
  [50, 0, 3, 18]
])

# Extracting columns from the array.
# Columns: [Passenger ID, Survived (0 = No, 1 = Yes), Passenger Class, Age]
passenger_ids = passengers[:, 0]
survived = passengers[:, 1]
passenger_class = passengers[:, 2]
ages = passengers[:, 3]

# Finding the shape of the array.
shape = np.shape(passengers)

# Calculating the average age of passengers.
avg_age = np.average(ages)

# Finding the oldest and youngest passengers by index.
oldest_passenger_index = np.argmax(ages)
youngest_passenger_index = np.argmin(ages)

# Extracting the IDs and ages of the oldest and youngest passengers.
oldest_passenger_id = passenger_ids[oldest_passenger_index]
youngest_passenger_id = passenger_ids[youngest_passenger_index]

# Extracting the ages of the oldest and youngest passengers.
oldest_age = ages[oldest_passenger_index]
youngest_age = ages[youngest_passenger_index]   

# Calculating the survival rate of all classes.
survival_rate = np.sum(survived) / shape[0] * 100

# Printing the results.
print('Shape of Array: ', shape)
print('')
print('Average Age: ', avg_age)
print('')
print('Oldest Passenger\'s ID: ', oldest_passenger_id, '\nOldest Passenger\'s Age: ', oldest_age)
print('')
print('Youngest Passenger\'s ID: ', youngest_passenger_id, '\nYoungest Passenger\'s Age: ', youngest_age)
print('')
print('Ship\'s Survival Rate: ', survival_rate, '%', sep='')
print('')

# Calculating and Printing the survival rate for each passenger class.
for cls in [1, 2, 3]:
    in_class = passenger_class == cls

    total_in_class = np.sum(in_class)
    survivors_in_class = np.sum(survived[in_class])

    if total_in_class > 0:
        survival_rate_in_class = survivors_in_class / total_in_class * 100
        print(f"Survival Rate in Class {cls}: {survival_rate_in_class:.2f}%")
        print('')
    else:
        print(f"No Passengers in Class {cls}.")
        print('')