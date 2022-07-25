import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv('D:\Datasets\Apple Finance\AAPL.csv')

# Tabdile column be Time
data['Date'] = data['Date'].apply(pd.to_datetime)

#taghire index data
data.set_index('Date', inplace=True)

#plot data bar asasde volume
#data['Volume'].plot()

#jodasazi ba shart baraye mah ya daghighe ya fasl o ...
#print(data.resample(rule='M').mean())

#plot kardane dade sharti shode
#print(data.resample(rule='M').mean().plot())
#print(data.resample(rule='M').mean()['Volume'].plot())
#print(data.resample(rule='Q').mean()['Open'].plot(kind='bar'))

plot.show()

