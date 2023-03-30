from django.shortcuts import render, redirect
from .forms import (DataSource,
                    SelectChart,
                    UploadData, df,
                    df_table,
                    NominalNumerical,
                    NominalForm,
                    ScatterForm,
                    HistogramForm,
                    LineplotForm,
                    BoxplotForm)
from .utility import get_variables_names, get_chart

def data(request):
    if request.method == 'POST':
        form = DataSource(request.POST)
        if form.is_valid():
            data_source = form.cleaned_data['data']
            if data_source == "Use demo data":
                return redirect('dashboard-select_chart')
            elif data_source == "Upload data":
                return redirect('dashboard-upload_file')
    return render(request, 'dashboard/data.html', {'form':DataSource()})

def upload_file(request):
    if request.method == 'POST':
        data = request.FILES.get('upload_data')
        # df = pd.read_csv(data)
        VARIABLE_NAMES = get_variables_names(df)
        CHART_CHOICES = (('Option 1', 'Choose one...'),
                        ('Bar chart', 'Bar chart'),
                        ('Pie chart', 'Pie chart'),
                        ('Scatter plot', 'Scatter plot'),
                        ('Histogram', 'Histogram'),
                        ('Line plot', 'Line plot'))

        form = SelectChart(initial={'chart_options': CHART_CHOICES,
                           'x_axis': VARIABLE_NAMES,
                           'y_axis': VARIABLE_NAMES})
        return render(request, 'dashboard/fix-upload.html', {'form':DataSource()})
        # return render(request, 'dashboard/chart_specs.html', {'form': form})
    return render(request, 'dashboard/upload.html', {'form': UploadData()})

def select_chart(request):
    if request.method == 'POST':
        form = SelectChart(request.POST)
        if form.is_valid():
            selected_chart = form.cleaned_data['chart_options']
            if selected_chart == 'Bar chart':
                return redirect('dashboard-barchart')
            elif selected_chart == 'Pie chart':
                return redirect('dashboard-piechart')
            elif selected_chart == 'Scatter plot':
                return redirect('dashboard-scatter')
            elif selected_chart == 'Histogram':
                return redirect('dashboard-histogram')
            elif selected_chart == 'Line plot':
                return redirect('dashboard-lineplot')
            elif selected_chart == 'Box plot':
                return redirect('dashboard-boxplot')
    else:
        return render(request, 'dashboard/chart_specs.html', {'form': SelectChart()})


def pie_chart(request):
    if request.method == 'POST':
        form = NominalForm(request.POST)
        if form.is_valid():
            x_axis = form.cleaned_data.get('x_axis')
            chart = get_chart('Pie chart', df, x_axis)                   
            context = {
                'chart': chart,
                'form': form
            }
            return render(request, 'dashboard/piechart.html', context)
    else:
        return render(request, 'dashboard/piechart.html', {'form': NominalForm()})

def bar_chart(request):
    if request.method == 'POST':
        form = NominalNumerical(request.POST)
        if form.is_valid():
            x_axis = form.cleaned_data.get('x_axis')
            y_axis = form.cleaned_data.get('y_axis')
            chart = get_chart('Bar chart', df, x_axis, y_axis=y_axis)                   
            context = {
                'chart': chart,
                'form': form,
                'df_table': df_table
            }
            return render(request, 'dashboard/barchart.html', context)
    else:
        return render(request, 'dashboard/barchart.html', {'form': NominalNumerical()})

def scatter_plot(request):
    if request.method == 'POST':
        form = ScatterForm(request.POST)
        if form.is_valid():
            x_axis = form.cleaned_data.get('x_axis')
            y_axis = form.cleaned_data.get('y_axis')
            color_by = form.cleaned_data.get('color_by')
            chart = get_chart('Scatter plot', df, x_axis, y_axis=y_axis, color=color_by)                   
            context = {
                'chart': chart,
                'form': form
            }
            return render(request, 'dashboard/scatter_plot.html', context)
    else:
        return render(request, 'dashboard/scatter_plot.html', {'form': ScatterForm()})

def histogram(request):
    if request.method == 'POST':
        form = HistogramForm(request.POST)
        if form.is_valid():
            x_axis = form.cleaned_data.get('x_axis')
            bins = form.cleaned_data.get('bins')
            chart = get_chart('Histogram', df, x_axis, bin=int(bins))                   
            context = {
                'chart': chart,
                'form': form
            }
            return render(request, 'dashboard/histogram.html', context)
    else:
        return render(request, 'dashboard/histogram.html', {'form': HistogramForm()})

def line_plot(request):
    if request.method == 'POST':
        form = LineplotForm(request.POST)
        if form.is_valid():
            x_axis = form.cleaned_data.get('x_axis')
            y_axis = form.cleaned_data.get('y_axis')
            label = form.cleaned_data.get('label')
            chart = get_chart('Line plot', df, x_axis, y_axis=y_axis, color=label)                   
            context = {
                'chart': chart,
                'form': form
            }
            return render(request, 'dashboard/lineplot.html', context)
    else:
        return render(request, 'dashboard/lineplot.html', {'form': LineplotForm()})

def boxplot(request):
    if request.method == 'POST':
        form = BoxplotForm(request.POST)
        if form.is_valid():
            x_axis = form.cleaned_data.get('x_axis')
            chart = get_chart('Box plot', df, x_axis)                   
            context = {
                'chart': chart,
                'form': form
            }
            return render(request, 'dashboard/boxplot.html', context)
    else:
        return render(request, 'dashboard/boxplot.html', {'form': BoxplotForm()})

def view_data(request):
    if request.method == 'POST':
        print('I am post')
        context = {
                'df_table': df_table
            }
        return render(request, 'dashboard/view_data.html', context)