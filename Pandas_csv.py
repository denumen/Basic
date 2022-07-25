import pandas as pd

data = pd.read_csv('D:\Datasets\Melbourne Housing Market\Melbourne_housing_FULL.csv')
#print(data)


#moshahede name sotoon ha
#print(data.columns)

#moshahede tedad satr ha ya sotoon haye gheyre null
#print(len(data))
#print(data.count())

# moshahede kole dataframe
pd.set_option('display.max_columns', None)

#moshahede satr haye daraye vizhegi khas
#print(data[data['Price']>100000])
#print(data[data['Price'] == 705000])
data_price705000 = data[data['Price'] == 705000]
data_price705000_2 = data_price705000['Price'] *2
#print(data_price705000_2)
#print(data.loc[34854])
#print(data_price705000_2.loc[34854])

#moshahede 5taye aval ya 5taye akhar
#print(data.head())
#print(data.tail())

#pak kardane value haye NaN ya NULL baraye sotoon ha
#print(data['YearBuilt'].dropna())

#jostojoo ba chand shart
#print(data[(data['Price'] == 705000) & (data['YearBuilt'] > 2000)])

#etelaate koli mesle miangin enheraf meyar va charak ha
#print(data.describe())

#etelaate data tedade null , memory usage o etelaat koli
#print(data.info())

#jame sotoon ha baham ya miangin
#print(data_price705000_2.sum())
#print(data_price705000_2.mean())
#print(data_price705000.std())
#print(data_price705000.var())

#ezafe kardane ye sotoon be data va meghdar dehi jam 2sotoon ya zarbeshon baham
data['price+built'] = data['Suburb'] + ' - ' + data['Address']
#print(data.head())

#moshahede azaye unique va tedade harkodoom
#print(data['Car'].unique())
#print(data['Car'].value_counts())

#miangin az ye moshakhase khas va ye sotoone dige
#print(data[data['Car']==6] ['Price'].mean())

#group bandi va anjame amaliat
#print(data.groupby('Car')['Price'].mean())

