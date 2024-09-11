# Ingest from a few simple sources (i.e. xlsx, csv, txt)

import os
import pandas as pd

def read_csv_files(directory):
    """
    Reads all csv files in the specified directory and returns a list of DataFrames.
    """
    # List all files in the directory
    files = os.listdir(directory)

    # Filter out only csv files (with .csv extension)
    csv_files = [file for file in files if file.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the directory.")
        return []

    dataframes = []  # List to hold DataFrames

    # Loop through each csv file and read into a pandas DataFrame
    for file in csv_files:
        print(f"\nReading file: {file}")
        try:
            # Read csv file
            df = pd.read_csv(file)
            
            # Append DataFrame to the list
            dataframes.append(df)
            
            # Print the first few rows of the DataFrame
            print(df.head())
        except Exception as e:
            print(f"Error reading {file}: {e}")

    return dataframes

if __name__ == "__main__":
    # Specify the current directory
    current_directory = os.getcwd()

    # Call the function to read csv files
    read_csv_files(current_directory)
