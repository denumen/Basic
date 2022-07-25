from bokeh.plotting import figure, output_file, show
import pandas as pd
import numpy as np
output_file('Bokeh_test.html')

x1 = np.array([1, 5, 7, 9, 22, 45, 86])
x2 = np.array([7, 5, 29, 31, 6, 12, 5])

p = figure()
p.line(x1, x2, color='Blue', legend_label='Line')
p.circle(x1, x2, color='Red', legend_label='Circle')
p.legend.click_policy = 'hide'
show(p)