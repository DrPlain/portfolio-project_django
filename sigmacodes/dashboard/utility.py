import plotly.express as px
from plotly.offline import plot
import numpy as np
from matplotlib import pyplot
from io import BytesIO, StringIO
import base64

def get_chart(selected_chart, df, x_axis, y_axis=None):
    pyplot.switch_backend('AGG')
    fig = pyplot.figure(figsize=(10, 4))
    if selected_chart == 'Bar chart':
        if y_axis:
            pyplot.bar(df[x_axis], df[y_axis])
    elif selected_chart == 'Pie chart':
        if y_axis == 'None':
            pyplot.pie(df[x_axis])
    # elif selected_chart == 'Scatter plot':
    #     print("Line graph")
    #     pyplot.plot(d[key], d['total_price'], color='gray', marker='o', linestyle='dashed')
    # else:
    #     print("Apparently...selected_chart not identified")

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

def barchart(df, x_axis, y_axis):
    if y_axis == 'None':
        if x_axis != 'None':
            fig = px.bar(df,
                        x=x_axis,
                        color_discrete_sequence=['blue'],
                        title='A simple bar chart',
                        width=1000,
                        height=600,
                        )
        else:
            return None
    else:
        if x_axis != 'None':
            fig = px.bar(df,
                        x=x_axis,
                        y=y_axis,
                        color = np.random.randn(111438),
                        title='A simple bar chart',
                        width=1000,
                        height=600,
                        )
        else:
            return None
    # fig.update_traces(marker_color='green',
    #                 textposition='outside')
    fig.update_layout(title_x=0.5, # center title
                    bargap=0.05, # space bars
                    xaxis_titlefont_size=16,
                    yaxis=dict(titlefont_size=16,
                                tickfont_size=14)
                    )
    figure = plot(fig, output_type='div', include_plotlyjs=False)
    return figure

        