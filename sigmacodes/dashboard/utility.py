from matplotlib import pyplot
from io import StringIO
import seaborn as sns

def get_chart(selected_chart, df, x_axis, y_axis=None, color=None, bin=None):
    pyplot.switch_backend('AGG')
    pyplot.style.use('seaborn')
    fig = pyplot.figure(figsize=(10, 4))
    if selected_chart == 'Bar chart':
        if y_axis != 'None':
            pyplot.bar(df[x_axis], df[y_axis])
            pyplot.xlabel(f'{x_axis}'.capitalize())
            pyplot.ylabel(f'{y_axis}'.capitalize())
            pyplot.title(f'A simple bar chart comparing {x_axis} with {y_axis} ')
        else:
            y = list(df[x_axis].value_counts())
            names = set()
            for name in df[x_axis]:
                names.add(name)
            x = list(names)
            pyplot.bar(x, y)
            pyplot.xlabel(f'{x_axis}'.capitalize())
            pyplot.ylabel('Count')
            pyplot.title(f'A simple bar chart showing the distribution of {x_axis}',
                         fontdict={'fontsize':16},
                         pad=20)
        pyplot.tight_layout()
        

    elif selected_chart == 'Pie chart':
        x = list(df[x_axis].value_counts())
        names = set()
        for name in df[x_axis]:
            names.add(name)
        label = list(names)
        
        # variable for adding spaces round the chart
        explode = []
        for _ in range(len(label)):
            explode.append(0.09)
        patches, texts, autotexts = pyplot.pie(x,
                   labels=label,
                   wedgeprops={'edgecolor': 'black'},
                   textprops={'fontsize': 14},
                   autopct='%1.2f%%',
                   colors=sns.color_palette('Set3'),
                   startangle=90,
                   explode=explode)
        # for text in texts:
        #     text.set_horizontalalignment('center')

        # Make the percentage italics
        for autotext in autotexts:
            autotext.set_horizontalalignment('center')
            autotext.set_fontstyle('italic')
        pyplot.title(f'A pie chart showing the distribution of {x_axis}',
                     fontdict={'fontsize': 16},
                     pad=20)
        pyplot.tight_layout()
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
        pyplot.title(f'A scatter plot comparing {x_axis} with {y_axis}',
                     fontdict={'fontsize': 16},
                     pad=20)
        pyplot.tight_layout()

    elif selected_chart == 'Histogram':
        pyplot.hist(df[x_axis],
                    bins=bin,
                    edgecolor='black')
        pyplot.xlabel(f'{x_axis}'.capitalize())
        pyplot.ylabel('Count')        
        pyplot.title(f'A histogram showing the distribution of {x_axis}',
                     fontdict={'fontsize': 16},
                     pad=20)
        pyplot.tight_layout()

    elif selected_chart == 'Line plot':
        pyplot.plot(df[x_axis],
                    df[y_axis])
        pyplot.xlabel(f'{x_axis}'.capitalize())
        pyplot.ylabel(f'{y_axis}'.capitalize())        
        pyplot.title(f'A Line graph comparing the distributions of {x_axis} and {y_axis}',
                     fontdict={'fontsize': 16},
                     pad=20)
        pyplot.tight_layout()

    elif selected_chart == 'Box plot':
        pyplot.boxplot(df[x_axis])
        pyplot.xlabel(f'{x_axis}'.capitalize())        
        pyplot.title(f'A box plot showing the distributions of {x_axis}',
                     fontdict={'fontsize': 16},
                     pad=20)
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