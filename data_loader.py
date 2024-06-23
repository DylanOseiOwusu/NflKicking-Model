import os
import pandas as pd

def load_excel_file(file_path):
    """
    Load an Excel file and return an ExcelFile object.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.ExcelFile(file_path)

def read_sheets_to_dfs(xls):
    """
    Read all sheets of an Excel file into a dictionary of DataFrames.
    """
    return {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}





     
