import pandas as pd
from bokeh.plotting import show, figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap

data = pd.read_csv('D:\Datasets\WW2\Thor_wwii.csv')

#joda kardane data haye makhsose 2keshvar faghat bejaye hame
#data_countries = data[data['COUNTRY_FLYING_MISSION'].isin(['USA', 'GREAT BRITAIN'])]

#group bandi baraye anjame amaliat
data_group = data.groupby('COUNTRY_FLYING_MISSION')[['TONS_FRAG', 'TONS_HE', 'TONS_IC', 'TOTAL_TONS']].apply(sum)
print(data_group)
#tabdile dataframe pandas be bokeh
datasource = ColumnDataSource(data_group)

#ijade list baraye mehvare x ha dar plot
countries = datasource.data['COUNTRY_FLYING_MISSION'].tolist()

#sakhte figure va countires baraye x ha
p = figure(x_range=countries)

#tanzimate range x ha
cm = factor_cmap('COUNTRY_FLYING_MISSION', palette=Spectral5, factors=countries)

#rasme nemoodare vbar
p.vbar(source= datasource,x='COUNTRY_FLYING_MISSION', color=cm, top='TOTAL_TONS', width=0.7)

#rasme nemodar
show(p)

#print(data_countries)
#print(data.info())
