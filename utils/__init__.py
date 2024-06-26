import re
import pandas as pd


def replace_datetime(row):
    if len(re.findall(r'\d{4}\-\d{2}\-\d{2}\s\d{2}:\d{2}:\d{2}', f'{row}')):
        return pd.to_datetime(row).strftime('%d/%m/%Y')
    return row


def filter_word_in_content(word, df: pd.DataFrame, case = True):
    return df.apply(lambda row: row.astype(str).str.contains(word, case=case).any(), axis=1)
