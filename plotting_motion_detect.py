import pandas
from bokeh.plotting import figure,show,output_file
from motion_detection import df

p=figure(width=500,height=300,x_axis_type='datetime',title="Motion Graph")
p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="green")

output_file("Make.html")
show(p)


