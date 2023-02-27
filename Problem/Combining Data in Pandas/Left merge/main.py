import pandas as pd

def merge_data(user_info, emails):
    return pd.merge(user_info, emails, how="left")