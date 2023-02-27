import pandas as pd

def create_series(capitals):
    ages_series = pd.Series(capitals, name='Capitals of the world')
    # print(ages_series)
    return ages_series
# capitals = {'Czech Republic': 'Prague',
#             'Russia': 'Moscow',
#             'Australia': 'Canberra'}
#
# create_series(capitals)