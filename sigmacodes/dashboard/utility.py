import plotly.express as px
from plotly.offline import plot

def get_variables_names(df):
    variable_names = [('None', 'None')]
    for key in df.keys():
        variable_names.append(tuple([key, key]))
        
    return tuple(variable_names)

def barchart(df, x_axis, y_axis):
    if y_axis == 'None':
        fig = px.bar(df,
                    x=x_axis,
                    color_discrete_sequence=['blue','green','orange'],
                    title='A simple bar chart',
                    width=1000,
                    height=600,
                    )
    else:
        fig = px.bar(df,
                    x=x_axis,
                    y=y_axis,
                    color_discrete_sequence=['blue','green','orange'],
                    title='A simple bar chart',
                    width=1000,
                    height=600,
                    )
    fig.update_traces(marker_color='green',
                    textposition='outside')
    fig.update_layout(title_x=0.5, # center title
                    bargap=0.05, # space bars
                    xaxis_titlefont_size=16,
                    yaxis=dict(titlefont_size=16,
                                tickfont_size=14)
                    )
    figure = plot(fig, output_type='div', include_plotlyjs=False)
    return figure

        