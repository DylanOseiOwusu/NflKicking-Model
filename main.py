#!/usr/bin/env python
# coding: utf-8

from data_loader import load_excel_file, read_sheets_to_dfs

def display_player_stats(df, rows=33, cols=25):
    """
    Display the first few rows and columns of the DataFrame.
    """
    print(df.iloc[:rows, :cols])  # Displaying the specified number of rows and columns



def read_sheets_to_dfs(xls):
    """
    Read all sheets in the Excel file into a dictionary of DataFrames.
    """
    # Initialize an empty dictionary to store DataFrames
    dfs = {}
    
    # Iterate over all sheet names in the Excel file
    for sheet_name in xls.sheet_names:
        # Read the current sheet into a DataFrame and store it in the dictionary
        dfs[sheet_name] = xls.parse(sheet_name)
    
    return dfs

# Now you can call this function without specifying the sheet name


def main():
    # Define the file path for the dataset
    file_paths = {'Data.xlsx': r'C:\Users\dylan\OneDrive\Desktop\NFL.Data\Data.xlsx'}

    # Load each Excel file and read the first sheet into a DataFrame
    for file_name, file_path in file_paths.items():
        xls = load_excel_file(file_path)
        print(f"Sheet names in {file_name}: {', '.join(xls.sheet_names)}")
        
        # Read the first sheet into a DataFrame
        sheet_name = 'Kicker-Stats'  # Assuming the first sheet is the one to be read
        df = read_sheets_to_dfs(xls)[sheet_name]
        
        # Display player stats and names
        display_player_stats(df)

if __name__ == "__main__":
    main()
