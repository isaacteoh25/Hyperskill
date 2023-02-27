import pandas as pd

wine_sample = {'variety': {26762: 'Cabernet Sauvignon', 15006: 'Pinot Noir', 25680: 'Pinot Noir', 16316: 'Bordeaux-style Red Blend', 2916: 'Pinot Noir', 13907: 'Cabernet Sauvignon', 21089: 'Pinot Noir', 21992: 'Chardonnay', 8788: 'Merlot', 11402: 'Pinot Noir', 10496: 'Pinot Noir', 16881: 'Red Blend', 26603: 'Bordeaux-style Red Blend', 15354: 'Chardonnay', 28061: 'Chardonnay', 12425: 'Chardonnay', 23541: 'Red Blend', 27393: 'Syrah', 9807: 'Red Blend', 7547: 'Pinot Noir', 10189: 'Red Blend', 12003: 'Pinot Noir', 145: 'Chardonnay', 2351: 'Syrah', 20913: 'Pinot Noir', 11005: 'Syrah', 26340: 'Syrah', 28306: 'Merlot', 28910: 'Red Blend', 1985: 'Cabernet Sauvignon', 24846: 'Bordeaux-style Red Blend', 13719: 'Chardonnay', 22748: 'Red Blend', 7295: 'Cabernet Sauvignon', 7574: 'Bordeaux-style Red Blend', 20836: 'Cabernet Sauvignon', 6692: 'Syrah', 13414: 'Bordeaux-style Red Blend', 26953: 'Chardonnay', 13925: 'Chardonnay', 25122: 'Cabernet Sauvignon', 8786: 'Bordeaux-style Red Blend', 10572: 'Chardonnay', 10648: 'Merlot', 28606: 'Red Blend', 16437: 'Pinot Noir', 5096: 'Red Blend', 4576: 'Syrah', 21004: 'Syrah', 19959: 'Syrah'}, 'price': {26762: 45.0, 15006: 41.0, 25680: 40.0, 16316: 32.0, 2916: 28.0, 13907: 23.0, 21089: 50.0, 21992: 50.0, 8788: 30.0, 11402: 25.0, 10496: 20.0, 16881: 42.0, 26603: 12.0, 15354: 36.0, 28061: 40.0, 12425: 29.0, 23541: 28.0, 27393: 50.0, 9807: 37.0, 7547: 38.0, 10189: 50.0, 12003: 39.0, 145: 37.0, 2351: 42.0, 20913: 28.0, 11005: 24.0, 26340: 45.0, 28306: 25.0, 28910: 50.0, 1985: 45.0, 24846: 40.0, 13719: 26.0, 22748: 35.0, 7295: 22.0, 7574: 22.0, 20836: 40.0, 6692: 36.0, 13414: 20.0, 26953: 35.0, 13925: 20.0, 25122: 41.0, 8786: 39.0, 10572: 28.0, 10648: 12.0, 28606: 19.0, 16437: 48.0, 5096: 40.0, 4576: 38.0, 21004: 24.0, 19959: 40.0}, 'points': {26762: 91, 15006: 94, 25680: 91, 16316: 88, 2916: 91, 13907: 88, 21089: 88, 21992: 90, 8788: 85, 11402: 89, 10496: 88, 16881: 83, 26603: 88, 15354: 91, 28061: 90, 12425: 91, 23541: 90, 27393: 88, 9807: 93, 7547: 88, 10189: 88, 12003: 90, 145: 92, 2351: 90, 20913: 87, 11005: 87, 26340: 91, 28306: 82, 28910: 87, 1985: 89, 24846: 89, 13719: 90, 22748: 90, 7295: 88, 7574: 91, 20836: 94, 6692: 90, 13414: 87, 26953: 92, 13925: 84, 25122: 90, 8786: 86, 10572: 87, 10648: 90, 28606: 84, 16437: 91, 5096: 93, 4576: 83, 21004: 88, 19959: 90}}

df = pd.DataFrame(wine_sample)

# your code here
print(df.pivot_table(index='variety',
                               columns=pd.cut(df.price, bins=[10, 20, 30, 40, 50]),
                               values='points',
                               aggfunc='mean'))

print(pd.crosstab(index=df.variety, columns=pd.cut(df.price, bins=[10, 20, 30, 40, 50])))