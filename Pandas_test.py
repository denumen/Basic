import pandas as pd

#import kardane dataset
data = pd.read_csv('D:\Datasets\Melbourne Housing Market\Melbourne_housing_FULL.csv')
#print(data)

#tabdile list be series pandas ,dtype zire series noesho neshon mide object,int64 , float64 , ...
list_animal= ['Tiger ', 'Goat', 'Cat', None]
#print(list_animal)
p_animals = pd.Series(list_animal)
#print(p_animals)
#joda kardane ye andise khas az pandas series
#print(p_animals[0])

#sakhte series kilid dar
list_animals_key = {
    'gorbe' : 'Cat',
    'sag' : 'Dog',
    'boz' : 'Goat'
}
p_list_animals_key = pd.Series(list_animals_key)
#print(p_list_animals_key)

# peyda kardane index ha ya klid haye har series ya maghadir
#print(p_list_animals_key.index)
#print((p_list_animals_key.values))

#type haye list pandas ke numpy hast
#print(type(p_list_animals_key.values))

#sakhte series besoorate mostaghim
p_animal_key = pd.Series(['cat', 'dog', 'goat'], index=(['n1','n2','n3']))
#print((p_animal_key))
#print(p_animal_key['n1'])
#print(p_animal_key[0])

#dastoore asli neshon dadane ye key ya meghdar
#print(p_animal_key.iloc[0])
#print(p_animal_key['n1'])

# for baraye index va value yekja
#for index , value in p_animal_key.iteritems():
 #   print('index is ' + index + ' and value is ' + value)

#sakhte dataframe ba chand satr va key yeksan
p_animal_key2 = pd.Series(['cat2', 'dog2', 'goat2'], index=(['n1','n2','n3']))
p_animal_key3 = pd.Series(['cat3', 'dog3', 'goat3'], index=(['n1','n2','n3']))
p_animal_frame = pd.DataFrame([p_animal_key,p_animal_key2,p_animal_key3])
#print(p_animal_frame)

# taghire name row ha dar DataFrame
p_animal_frame2 = pd.DataFrame([p_animal_key,p_animal_key2,p_animal_key3], index=['row1', 'row2', 'row3'])
#print(p_animal_frame2)

#jostojoo dar DataFrame
#print(p_animal_frame2.loc['row2'].loc['n1'])
#print(p_animal_frame2.loc['row1'])
#print(p_animal_frame2.loc[['row2','row3']])
#print(p_animal_frame2.loc[['row1', 'row2'],'n1'])
#print(p_animal_frame2['n1'])
#print(p_animal_frame2[['n1','n2']])

#jostojoo dar DataFrame bedoone ye satr
#print(p_animal_frame2.drop('row1'))

#jostojoo va jaigozini dataset bedoone ye satr bejaye asli
#p_animal_frame2.drop('row1', inplace=True)
#print(p_animal_frame2)

#transpose kardane dataframe
#print(p_animal_frame2.T)

# taghire value haye ye sotoon
p_animal_frame3 = p_animal_frame2
#print(p_animal_frame3)
p_animal_frame3['n1'] = 1
#print(p_animal_frame3)
p_animal_frame3['n1'] = p_animal_frame3['n1']*2
n3 = p_animal_frame3['n2']
n3 += '!'
#print(p_animal_frame3)

# copy kardane ye frame tuye ye frame dige bejaye copy kardane addressesh
n3 = p_animal_frame3[:]
#print(n3)
