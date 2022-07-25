import pandas as pd
from bokeh.plotting import show, figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3

data = pd.read_csv('D:\Datasets\WW2\Thor_wwii.csv')

#joda kardane data haye makhsose 2keshvar faghat bejaye hame
data_filtered = data[data['COUNTRY_FLYING_MISSION'].isin(('USA', 'GREAT BRITAIN'))]
data = data[data['COUNTRY_FLYING_MISSION'].isin(('USA', 'GREAT BRITAIN'))]

#group bandi va sum
data_group = data_filtered.groupby('COUNTRY_FLYING_MISSION')[['TOTAL_TONS', 'TONS_FRAG', 'TONS_IC', 'TONS_HE']].sum()

# tabdile pandas be bokeh data
data_source = ColumnDataSource(data_group)

#tabdile name group ha be list baraye x ha
countries = data_source.data['COUNTRY_FLYING_MISSION'].tolist()
print(countries)

#moshakhas kardane data mehvare x dar figure
p = figure(x_range=countries)

#sakhte nemoodar
p.vbar_stack(source=data_source, x='COUNTRY_FLYING_MISSION', width=0.7, color=Spectral3,
             stackers=['TONS_FRAG', "TONS_IC", 'TOTAL_HE'],
             legend_label=['تعداد قطعات', 'مجموع انفجار قوی', 'میزان اشتعال زا'])


#namayeshe plot
show(p)
