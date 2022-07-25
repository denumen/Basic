import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


#taghire style nemoodar ha
sb.set_style('darkgrid')

data = pd.read_csv('D:\Datasets\Titanic\Titanic.csv')

#histogram baraye data
#print(data['Age'].hist())

#taghire default 10ghesmat baraye histogram be n digei
#print(data['Age'].hist(bins=30))

#raveshe dovom baraye plot kardan
#data['Age'].plot(kind='hist',bins=10)

#plot khati
#print(data['Age'].plot(kind='line'))

#plot khati ba 2moteghayer
#data.plot.line(x='Age',y='Pclass')

#taghire size plot va taghir data
#data[:1000].plot.line(x='Age',y='Pclass',figsize=(10,10))

#sort kardane data bar asase column
data22=data.sort_values('Age')
#print([data22['Age'].iloc[30:60]])
#data22.plot.line(x='Age', y='Pclass')
#data.sort_values('Age').plot.line(x='Age', y='Pclass', figsize=(10, 10))

#plote parakandegi noghtei
#data.sort_values('Age').plot.scatter(x='Age', y='Pclass', figsize=(10,10))

#plot hexbin
#data.sort_values('Age').plot.hexbin(x='Age', y='Pclass', gridsize=20 ,figsize=(10,10))

#nemoodare density ba ghelzat
#data['Fare'].plot.kde()

#nemoodare jabei
#data.drop(['PassengerId','Fare'], axis=1).plot.box(figsize=(20,12))


#mohasebe charak ha
print(pd.DataFrame([data['Age'].quantile([0.25, 0.5, 0.75])]))
# rasme nemodar haye bala
plt.show()
