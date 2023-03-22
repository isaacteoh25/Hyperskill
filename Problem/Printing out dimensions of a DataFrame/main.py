import pandas as pd


def print_dim(df):
    students = pd.DataFrame(df)
    var = students.shape
    print(f'This DataFrame contains {var[0]} rows and {var[1]} columns')