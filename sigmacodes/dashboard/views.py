from django.shortcuts import render, redirect
from .forms import (DataSource,
                    UploadData, df,
                    text_file,
                    ChartSpecs)
from .utility import get_variables_names, get_chart


def data(request):
    """View to select data set"""

    if request.method == 'POST':
        form = DataSource(request.POST)
        if form.is_valid():
            data_source = form.cleaned_data['data']
            if data_source == "Use demo data":
                return redirect('dashboard-charts')
            elif data_source == "Upload data":
                return redirect('dashboard-upload_file')
    return render(request, 'dashboard/data.html', {'form': DataSource()})


def chart_specs(request):
    """View that handles different chart options and displays dataframe and chart
    as output"""

    if request.method == 'POST':
        form = ChartSpecs(request.POST)
        if form.is_valid():
            selected_chart = form.cleaned_data.get('chart_options')
            nominal_x = form.cleaned_data.get('nominal_x')
            numerical_x = form.cleaned_data.get('numerical_x')
            numerical_y = form.cleaned_data.get('numerical_y')
            numerical_none = form.cleaned_data.get('numerical_none')
            color_by = form.cleaned_data.get('color_by')
            bin = form.cleaned_data.get('bins')

            if selected_chart == 'None':
                return render(request, 'dashboard/chart.html', {'form': ChartSpecs()})
            elif selected_chart == 'Bar chart':
                chart = get_chart('Bar chart', df, nominal_x,
                                  y_axis=numerical_none)
            elif selected_chart == 'Pie chart':
                chart = get_chart('Pie chart', df, nominal_x)
            elif selected_chart == 'Scatter plot':
                chart = get_chart('Scatter plot', df, numerical_x,
                                  y_axis=numerical_y, color=color_by)
            elif selected_chart == 'Histogram':
                chart = get_chart('Histogram', df, numerical_x, bin=int(bin))
            elif selected_chart == 'Line plot':
                chart = get_chart('Line plot', df, numerical_x,
                                  y_axis=numerical_y, color=nominal_x)
            elif selected_chart == 'Box plot':
                chart = get_chart('Box plot', df, numerical_x)

            context = {
                'chart': chart,
                'df_table': text_file
            }

            return render(request, 'dashboard/view_chart.html', context)
        else:
            return render(request, 'dashboard/chart.html', {'form': ChartSpecs()})
    else:
        return render(request, 'dashboard/chart.html', {'form': ChartSpecs()})


def upload_file(request):
    """View to enable user upload data set"""

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

        return render(request, 'dashboard/fix-upload.html', {'form': DataSource()})
        # return render(request, 'dashboard/chart_specs.html', {'form': form})
    return render(request, 'dashboard/upload.html', {'form': UploadData()})
