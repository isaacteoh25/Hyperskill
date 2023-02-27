import pandas as pd

# keyboard_instruments = pd.DataFrame({'cat_id': ['001', '002', '003'],
#                                      'Instrument': ['Acoustic piano', 'Electric piano', 'Synthesizer'],
#                                      'Average price': ['$10,000', '$5,000', '$1,200']},
#                                     index=[1, 2, 3])
#
# string_instruments = pd.DataFrame({'cat_id': ['004', '005', '006'],
#                                    'Instrument': ['Acoustic guitar', 'Cello', 'Violin'],
#                                    'Average price': ['$2,000', '$1,500', '$2,000']},
#                                   index=[1, 2, 3])

def concatenate_data(keyboard_instruments, string_instruments):
    return pd.concat([keyboard_instruments, string_instruments], ignore_index=True)

# print(concatenate_data(keyboard_instruments,string_instruments))