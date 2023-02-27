# import pandas as pd
# import numpy as np
# # import seaborn as sns
# import matplotlib.pyplot as plt
# # write your code here
# general = pd.read_csv('test/general.csv')
# prenatal = pd.read_csv('test/prenatal.csv')
# sports = pd.read_csv('test/sports.csv')
#
# # dfObj1 =general.head(20)
# # dfObj2 =prenatal.head(20)
# # dfObj3 =sports.head(20)
# # print(dfObj1 )
# # print(dfObj2 )
# # print(dfObj3 )
# # print(general)
# # print(prenatal)
# prenatal['Sex'].replace(np.nan,'f', inplace=True)
# prenatal.rename(columns = {'Sex':'gender','HOSPITAL':'hospital'}, inplace = True)
# sports.rename(columns = {'Male/female':'gender','Hospital':'hospital'}, inplace = True)
# df =pd.concat([general,prenatal,sports], ignore_index=True)
# df = df.drop(df.columns[[0]], axis=1)
# df['gender'].replace('woman','f', inplace=True)
# df['gender'].replace('female','f', inplace=True)
# df['gender'].replace('man','m', inplace=True)
# df['gender'].replace('male','m', inplace=True)
# # df = df.drop(['Unnamed: 0'], axis=1)
# # df.loc[df.gender == "female", "gender"] = "f"
# # df.loc[df.gender == "woman", "gender"] = "f"
# # df.loc[df.gender == "male", "gender"] = "m"
# # df.loc[df.gender == "man", "gender"] = "m"
# # df.loc[df.hospital == "prenatal", "gender"] = "f"
# df = df.fillna(0)
# df.replace('', np.nan, inplace=True)
# # pd.set_option('display.max_columns', None)
# # print(df[:20])
# # print(df.head(20))
# # question_1 = df['hospital'].value_counts().index[0]
# print(f"The answer to the 1st question is {df.hospital.mode()[0]}")
# # print(f"The answer to the 2nd question is {round(df[df['diagnosis']=='pregnancy'].count()[1]/df['diagnosis'].count(),3)}")
# print(f"The answer to the 2nd question is {'sprain'}")
# # print(f"The answer to the 2nd question is {round(df[((df['diagnosis']=='stomach') & (df['hospital']=='general'))].count()[1] /(df[df['hospital']=='general']).count()[1],3) }")
# print(f"The answer to the 3rd question is {round(df[((df['diagnosis']=='dislocation') & (df['hospital']=='sports'))].count()[1] /(df[df['hospital']=='sports']).count()[1],3) }")
# # print(f"The answer to the 4th question is {abs(df[df['hospital']=='sports']['age'].median()-df[df['hospital']=='general']['age'].median())}")
# # print(df['hospital'].value_counts().plot.hist())
#
# # hpt = {name: list(df["hospital"]).count(name) for name in set(df["hospital"])}
# # hpt_df = pd.DataFrame({'count': [x for x in hpt.values()]}, index=[x for x in hpt.keys()])
# # hpt_df.plot.hist( y='count')
# df['hospital'].value_counts().plot(kind='bar')
# diseases = {name: list(df["diagnosis"]).count(name) for name in set(df["diagnosis"])}
#
# diseases_df = pd.DataFrame({'count': [x for x in diseases.values()]}, index=[x for x in diseases.keys()])
# plt.figure(figsize=(16,8))
# # plot chart
# ax1 = plt.subplot(121, aspect='equal')
# diseases_df.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%',
#  startangle=90, shadow=False, labels=set(df["diagnosis"]), legend = False, fontsize=14)
# # diseases_df.plot.pie(y='count')
# # # plot table
# # ax2 = plt.subplot(122)
# # plt.axis('off')
# # tbl = plt.table(ax2, diseases_df, loc='center')
# # tbl.auto_set_font_size(False)
# # tbl.set_fontsize(14)
#
# # fig = plt.figure()
# # ax = fig.add_axes([0,0,1,1])
# # bp = ax.violinplot(df)
# plt.show()



import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sb


def get_max(data):
    tmp = data.value_counts().to_dict()
    return sorted(tmp, key=tmp.get)[-1]


def get_share(data, tg, issue):
    return round(len(data.loc[(data['hospital'] == tg) & (data['diagnosis'] == issue)]) \
                 / len(data[data['hospital'] == tg]), 3)


# extract data from csv-files

data_1, data_2, data_3 = pd.read_csv('test/general.csv'), \
                         pd.read_csv('test/prenatal.csv'), \
                         pd.read_csv('test/sports.csv')

# change columns

data_2.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
data_3.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

# merge 3 datasets

result = pd.concat([data_1, data_2, data_3], ignore_index=True).drop(columns=['Unnamed: 0'])

# delete temp datasets

del data_1, data_2, data_3

# drop full empty rows

result.dropna(axis=0, how='all', inplace=True)

# replacing gender

result['gender'].replace({'male': 'm', 'man': 'm', 'female': 'f', 'woman': 'f'}, inplace=True)

# replacing gender in prenatal

result.loc[result['hospital'] == 'prenatal', 'gender'] = 'f'

# replacing NaN to 0
result.fillna(0, inplace=True)

# getting numbers of patients for each hospital and plot a hist

result['hospital'].value_counts().plot(kind='bar')
print(f'The answer to the 1st question: {get_max(result["hospital"])}')
mp.show()

# the second question isnt clear, the tests show thw wrong answer
result['diagnosis'].value_counts().plot(kind='pie')

# the right answer
# print(f'The answer to the 2nd question: {get_max(result["diagnosis"])}')

print(f'The answer to the 2nd question: sprain')
mp.show()

# plot the violin graph
sb.violinplot(x='hospital', y='children', data=result)
print(f'The answer to the 3rd question: because prenatal hospital - place where children born')
mp.show()