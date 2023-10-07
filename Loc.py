import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami'],
        'Salary': [60000, 70000, 80000, 90000, 75000]}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Select rows using iloc
subset1 = df.iloc[1:3]  # Select rows 1 to 2 (exclusive of 3)
subset2 = df.iloc[[0, 3, 4]]  # Select rows with indices 0, 3, and 4
print("\nSubsets using iloc:")
print(subset1)
print(subset2)

# Select specific columns using iloc
selected_columns = df.iloc[:, [0, 2]]  # Select columns at indices 0 and 2
print("\nSelected columns using iloc:")
print(selected_columns)

# Add a new column 'Department'
df['Department'] = ['HR', 'Finance', 'IT', 'Marketing', 'Sales']

# Display the DataFrame with the new column
print("\nDataFrame with 'Department' column added:")
print(df)

# Delete a column 'Age'
df = df.drop(columns=['Age'])

# Display the DataFrame with 'Age' column removed
print("\nDataFrame with 'Age' column removed:")
print(df)

# Add a new row
new_row = {'Name': 'Frank', 'City': 'Seattle', 'Salary': 72000, 'Department': 'Engineering'}
df = df.append(new_row, ignore_index=True)

# Display the DataFrame with the new row
print("\nDataFrame with a new row added:")
print(df)

# Filter data using loc
marketing_data = df.loc[df['Department'] == 'Marketing']
print("\nEmployees in the Marketing Department:")
print(marketing_data)

# Set 'Name' column as the index
df.set_index('Name', inplace=True)

# Display the DataFrame with 'Name' as the index
print("\nDataFrame with 'Name' as the index:")
print(df)

# Select a specific row by label using loc
specific_row = df.loc['Bob']
print("\nData for 'Bob' using loc:")
print(specific_row)
