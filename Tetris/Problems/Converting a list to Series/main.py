import pandas as pd

def create_series(foods, calories):
    ages_series = pd.Series(calories, index=foods, name='Calorie content')
    return ages_series
