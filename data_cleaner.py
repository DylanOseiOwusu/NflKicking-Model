import pandas as pd

from team_mappings import team_name_mapping

def standardize_team_names(df, column, mapping):
    """
    Standardize team names in a DataFrame column using the provided mapping.
    """
    df[column] = df[column].apply(lambda x: mapping.get(x, x))
    return df

def clean_data(df, columns_to_rename, team_column):
    """
    Clean the given DataFrame by renaming columns.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    columns_to_rename (dict): Dictionary mapping old column names to new column names.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    df.columns = df.iloc[0]
    df = df.drop(0).reset_index(drop=True)
    df = df.rename(columns=columns_to_rename)
    df = standardize_team_names(df, team_column, team_name_mapping)
    print("Columns after cleaning:", df.columns)  # Debug print
    return df
