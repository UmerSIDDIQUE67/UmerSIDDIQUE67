import pandas as pd
df = pd.read_csv('E:\ai lab task 9\Marvel_Movies_Dataset.csv')
print(df.head())
print("Shape of the dataset:", df.shape)
print("Column information:")
print(df.info())
print("Summary statistics:")
print(df.describe())
print("Missing values in each column:")
print(df.isnull().sum())
print("Unique values in a column:")
print(df['your_column_name'].unique())
print("Value counts for a column:")
print(df['your_column_name'].value_counts())
print("Random sample:")
print(df.sample(5))
