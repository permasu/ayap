from bokeh.plotting import figure, output_file, show
import numpy as np


x = np.linspace(-np.pi, np.pi, 12)
y= np.sin(x)
output_file('index.html')

p=figure(
    title= 'Simple SIN',
    x_axis_label='x',
    y_axis_label='y'
)
p.line(x,y,legend='Test', line_width=2)
show(p)

