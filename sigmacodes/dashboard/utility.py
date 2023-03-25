import plotly.express as px
from plotly.offline import plot
import numpy as np
from matplotlib import pyplot
from io import BytesIO, StringIO
import base64

def get_chart(selected_chart, df, x_axis, y_axis=None, color=None):
    pyplot.switch_backend('AGG')
    pyplot.style.use('seaborn')
    fig = pyplot.figure(figsize=(10, 4))
    if selected_chart == 'Bar chart':
        if y_axis:
            pyplot.bar(df[x_axis], df[y_axis])
            pyplot.xlabel(f'{x_axis}'.capitalize())
            pyplot.ylabel(f'{y_axis}'.capitalize())
            pyplot.title(f'A simple bar chart comparing {x_axis} with {y_axis} ')
            pyplot.tight_layout()        
    elif selected_chart == 'Pie chart':
        pyplot.pie(df[x_axis].groupby(x_axis))
    elif selected_chart == 'Scatter plot':
        if color != 'None':
            pyplot.scatter(df[x_axis],
                        df[y_axis], 
                        c=df[color],
                        edgecolors='black', 
                        linewidths=1,
                        cmap='Blues',
                        alpha=0.75)
            cbar = pyplot.colorbar()
            cbar.set_label(f'{color}')
        else:
            pyplot.scatter(df[x_axis],
                        df[y_axis],
                        edgecolors='black', 
                        linewidths=1,
                        alpha=0.75)
        pyplot.xlabel(f'{x_axis}'.capitalize())
        pyplot.ylabel(f'{y_axis}'.capitalize())
        pyplot.title(f'A scatter plot comparing {x_axis} with {y_axis} ')
        pyplot.tight_layout()        

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    chart = imgdata.getvalue()
    return chart

def get_variables_names(df):
    nominal_variables = []
    numerical_variables = []
    for key in df.keys():
        if df[key].dtypes == 'object':
            nominal_variables.append(tuple([key, key]))
        elif df[key].dtypes == 'float64' or df[key].dtypes == 'int64':
            numerical_variables.append(tuple([key, key]))
        
    return tuple(nominal_variables), tuple(numerical_variables)