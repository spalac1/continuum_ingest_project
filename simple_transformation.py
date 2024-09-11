# Simple Pandas showcase. If there's time, create something for Pyspark and polars
# Do some simple df merging to combine data and some field generation (i.e. grouped sales numbers)
# Maybe add some simple filter

import os
import pandas as pd
from simple_ingest import read_csv_files  # Import the function from simple_ingest.py

def merge_dataframes(dataframes):
    """
    Merges a list of DataFrames into one DataFrame.
    """
    if not dataframes:
        print("No DataFrames to merge.")
        return pd.DataFrame()  # Return an empty DataFrame if the list is empty

    # Concatenate all DataFrames vertically, ignoring index for a simple append
    merged_df = pd.merge(dataframes, ignore_index=True)
    return merged_df

def main():
    # Specify the current directory (or specify another directory if needed)
    current_directory = os.getcwd()
    
    # Read Excel files and get DataFrames
    dataframes = read_csv_files(current_directory)
    
    # Merge all DataFrames into one
    # merged_df = merge_dataframes(dataframes)

    # Merge specific Dataframes


    # Check if the merged DataFrame is not empty
    if not merged_df.empty:
        # Display the first few rows of the merged DataFrame
        print("Merged DataFrame:")
        print(merged_df.head())

        # Perform some data manipulations
        # Example: Descriptive statistics
        print("\nDescriptive Statistics:")
        print(merged_df.describe())

        # Example: Filter rows where a certain column value is above a threshold (if a numeric column exists)
        # Replace 'age' with an actual column name from your Excel files
        if 'age' in merged_df.columns:
            filtered_df = merged_df[merged_df['age'] > 20]
            print("\nFiltered DataFrame (age > 20):")
            print(filtered_df.head())
    else:
        print("No data available to manipulate.")

if __name__ == "__main__":
    main()
