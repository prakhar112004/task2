import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Read the CSV file
data = pd.read_csv("C:\\Users\\Siddharth\\Downloads\\01.Data Cleaning and Preprocessing.csv")

# Print the type of the data
print(type(data))

# Print information about the DataFrame
print(data.info())

# Print descriptive statistics of the DataFrame
print(data.describe())

# Drop duplicate rows
data = data.drop_duplicates()

# Print the updated DataFrame after dropping duplicates
print("DataFrame after dropping duplicates:")
print(data)

# Print a DataFrame indicating if values are null
print(data.isnull())

# Print the sum of null values for each column
print(data.isnull().sum())

# Print a DataFrame indicating if values are not null
print(data.notnull())

# Print the total number of null values in the DataFrame
print(data.isnull().sum().sum())

# Fill NaN values with 222222 and assign to data2
data2 = data.fillna(value=222222)

# Print the updated DataFrame with NaN values filled
print(data2)

# Print the total number of null values in the updated DataFrame
print(data2.isnull().sum().sum())

# Fill NaN values using the 'pad' method and assign to data3
data3 = data.fillna(method='pad')

# Print the updated DataFrame with NaN values filled using 'pad' method
print(data3)

# Fill NaN values using the 'bfill' method and assign to data4
data4 = data.fillna(method='bfill')

# Print the updated DataFrame with NaN values filled using 'bfill' method
print(data4)

# Print the columns of data2 before dropping a column
print("Columns before dropping 'observation':", data2.columns)

# Drop the 'observation' column from data2
data2.drop(['BlowFlow'], axis=1, inplace=True)

# Print the columns of data2 after dropping a column
print("Columns after dropping 'observation':", data2.columns)

# Select only numeric columns for quantile calculations
numeric_data2 = data2.select_dtypes(include=[np.number])

# Calculate the first and third quartiles (Q1 and Q3)
Q1 = numeric_data2.quantile(0.25)
Q3 = numeric_data2.quantile(0.75)

# Calculate the interquartile range (IQR)
IQR = Q3 - Q1

# Print the IQR
print("Interquartile Range (IQR):", IQR)

outliers = numeric_data2[((numeric_data2 < (Q1 - 1.5 * IQR)) | (numeric_data2 > (Q3 + 1.5 * IQR))).any(axis=1)]

# Print the rows with outliers
print("Rows with outliers:")
print(outliers)

print(outliers.describe)
