import pandas as pd
from bokeh.plotting import show, figure, output_file
from bokeh.models import ColumnDataSource

data = pd.read_csv("D:\Datasets\WW2\Thor_wwii.csv")

#tabdile series date time be index
data['MSNDATE'] = pd.to_datetime(data['MSNDATE'],format='%m/%d/%Y')

#group bandi bar asase zaman va besoorate mahane va mohasebe jam
data_group = data.groupby(pd.Grouper(key='MSNDATE', freq='M'))[['TOTAL_TONS', 'TONS_FRAG','TONS_IC', 'TONS_HE']].sum()

#tabdile data pandas be bokeh
data_source = ColumnDataSource(data_group)

#jaigozarie date time baraye mehvare x ha
p = figure(x_axis_type='datetime')

#sakhte 4 nemoodare mokhtalef ba legend haye mokhtalef
p.line(x='MSNDATE', y='TOTAL_TONS',source=data_source, color='blue', line_width=2, legend_label='T_tons')
p.line(x='MSNDATE', y='TONS_FRAG',source=data_source, color='red', line_width=2, legend_label='T_FRAG')
p.line(x='MSNDATE', y='TONS_IC',source=data_source, color='green', line_width=2, legend_label='T_IC')
p.line(x='MSNDATE', y='TONS_HE',source=data_source, color='pink', line_width=2, legend_label='T_HE')

#hide shodane nemoodar ba click bar legend
p.legend.click_policy = "hide"

show(p)

