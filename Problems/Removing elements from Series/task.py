import pandas as pd

def drop_record(olympics):
    olympics.drop(index=2020, inplace=True)
    return olympics