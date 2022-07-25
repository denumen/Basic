import pandas as pd
from bokeh.plotting import show, figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

#kaheshe tedade data
data = pd.read_csv("D:\Datasets\WW2\Thor_wwii.csv").sample(500)

#tabdile data pandas be bokeh
Data_Source = ColumnDataSource(data)

#sakhte figure ba name p
p = figure()

#nemodare noghtei
p.circle(source=Data_Source, x='AC_ATTACKING', y='TOTAL_TONS', color='blue', size='TONS_IC')

#namayeshe eetelaaf ba gharar dadane mouse ruye nemoodar
p_tools = HoverTool()
p_tools.tooltips= [
    ('نام نیروی هوایی' , '@AIRCRAFT_NAME'),
    ('تاریخ حمله', '@MSNDATE'),
('کشور اعزام کننده' ,'@COUNTRY_FLYING_MISSION')

]
#ezafe kardane tool
p.add_tools(p_tools)

#taghire name nemoodar
p.title.text = 'hello'

#taghire name mehvare x
p.xaxis.axis_label = 'میزان مواد منفجره'

#taghir name mehvare y
p.yaxis.axis_label = 'تعداد حمله هوایی'

#hide shodane nemoodar ba click bar legend
p.legend.click_policy = "hide"

#namayeshe nemodar
show(p)
