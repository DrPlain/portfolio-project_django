from django.shortcuts import render, redirect
import plotly.express as px
import pandas as pd
from .forms import DataSource, SelectChart, UploadData, df, NominalNumerical, NominalForm, NumericalForm
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
        return redirect('dashboard-select_chart')
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
            # x_axis = form.cleaned_data['x_axis']
            # y_axis = form.cleaned_data['y_axis']
            # chart = get_chart(selected_chart, df, x_axis, y_axis)                   
            # context = {
            #     'chart': chart,
            #     'form': form
            # }
            # return render(request, 'dashboard/chart_specs.html', context)
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
            chart = get_chart('Bar chart', df, x_axis, y_axis)                   
            context = {
                'chart': chart,
                'form': form
            }
            return render(request, 'dashboard/barchart.html', context)
    else:
        return render(request, 'dashboard/barchart.html', {'form': NominalNumerical()})
