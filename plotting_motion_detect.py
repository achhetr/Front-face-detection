import pandas
from bokeh.plotting import figure,show,output_file
from motion_detection import df
from bokeh.models import HoverTool, ColumnDataSource

df["Start_str"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_str"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p=figure(width=500,height=300,x_axis_type='datetime',title="Motion Graph")

hover = HoverTool(tooltips=[("Start", "@Start_str"),("End", "@End_str")])
p.add_tools(hover)

p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

output_file("Make.html")
show(p)


