from pandas import DataFrame
import re

def correct_data(df: DataFrame) -> None:
    """
    Perform data correction operations on the DataFrame.

    Parameters:
        df (DataFrame): The input DataFrame to be corrected.
    """
    drop_data(df)
    fill_data(df)
    filter_data(df)

def fix_description(text: str, pattern: str) -> str:
    """
    Fix the description column by applying a regular expression pattern.

    Parameters:
        text (str): The input text to be fixed.
        pattern (str): The regular expression pattern.

    Returns:
        str: The fixed text.
    """
    match = re.search(pattern, text)
    if match:
        return match.group('phrase')
    else:
        return text

def drop_data(df: DataFrame) -> None:
    """
    Drop duplicates, replace multiple whitespaces with a single space, and apply a fix to the 'description' column.

    Parameters:
        df (DataFrame): The input DataFrame.
    """
    # Group by 'description' and take the first row from each group
    df = df.groupby('description').first().reset_index()

    df.drop_duplicates(
        subset=['name', 'description', 'type', 'events_count',
                'crit_rate', 'assets_id', 'vulnerabilities_id',
                'start_time', 'end_time'],
        inplace=True,
        ignore_index=True)

    # Replace multiple whitespaces with a single space and strip leading/trailing whitespaces
    df['description'] = df['description'].str.replace(r'\s+', ' ').str.strip()

    # Remove duplicates in the 'description' column
    df['description'] = df['description'].drop_duplicates()

    # Apply the fix_description function with the specified pattern to the 'description' column
    pattern0 = r'^(?P<phrase>Обнаружена активность "[a-zA-Zа-яА-Я ]+" с уязвимостями [0-9,]+)$'
    df['description'] = df['description'].apply(fix_description, pattern=pattern0)

def fill_data(data: DataFrame) -> None:
    """
    Fill missing values in the DataFrame using the forward fill method.

    Parameters:
        data (DataFrame): The input DataFrame to be filled.
    """
    filled_df = data.copy()
    filled_df.iloc[:, 1:] = filled_df.iloc[:, 1:].fillna(method='ffill')

def filter_data(df: DataFrame) -> DataFrame:
    """
    Filter rows based on the presence of specified characters in selected columns.

    Parameters:
        df (DataFrame): The input DataFrame.

    Returns:
        DataFrame: The filtered DataFrame.
    """
    # List of columns to filter
    columns_to_filter = ['name', 'description', 'type']

    # Create regex for finding rows with specified characters in selected columns
    regex_to_search = r'[\@|\!|\?|\$|\^|\<|\>|\{|\[|\*|\#|\&|\~|\_|\%|\]|\}]'

    # Use str.contains with inversion (~) to select rows not containing specified characters in selected columns
    filtered_df = df[~df[columns_to_filter].apply(lambda col: col.astype(str).str.contains(regex_to_search).any(), axis=1)]

    return filtered_df