from django.shortcuts import render, redirect
import plotly.express as px
import pandas as pd
from .forms import DataSource, ChartSpecs, UploadData
from .utility import barchart

def data(request):
    if request.method == 'POST':
        form = DataSource(request.POST)
        if form.is_valid():
            data_source = form.cleaned_data['data']
            if data_source == "Use demo data":
                return redirect('dashboard-demo_chart')
            elif data_source == "Upload data":
                return redirect('dashboard-upload_file')
    return render(request, 'dashboard/data.html', {'form':DataSource()})

def upload_file(request):
    context = {
        'form': UploadData()
    }
    return render(request, 'dashboard/chart_specs.html', context)

def demo_chart(request):
    if request.method == 'POST':
        form = ChartSpecs(request.POST)
        if form.is_valid():
            selected_chart = form.cleaned_data['chart_options']
            x_axis = form.cleaned_data['x_axis']
            y_axis = form.cleaned_data['y_axis']
    
            df = pd.read_csv('demo_data.csv')                
        
            if selected_chart == 'Bar chart':
                figure = barchart(df, x_axis, y_axis)
            elif selected_chart == 'Pie chart':
                pass
            elif selected_chart == 'Scatter plot':
                pass
            elif selected_chart == 'Histogram':
                pass
            elif selected_chart == 'Line plot':
                pass

                   
            context = {
                'plot_div': figure,
                'form': form
            }
            return render(request, 'dashboard/chart_specs.html', context)
    else:
        return render(request, 'dashboard/chart_specs.html', {'form': ChartSpecs()})


