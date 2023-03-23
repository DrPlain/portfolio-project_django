from django import forms
from .utility import get_variables_names
import pandas as pd

class DataSource(forms.Form):
    DATA_CHOICES = (('Option 1', 'Choose one...'),
                    ('Use demo data', 'Use demo data'),
                    ('Upload data', 'Upload data'))
    
    data = forms.CharField(label="Select data to visualize",
                                  widget = forms.Select(choices=DATA_CHOICES))
    

class UploadData(forms.Form):
    upload_data = forms.FileField(allow_empty_file=False)

class ChartSpecs(forms.Form):
    df = pd.read_csv('demo_data.csv')
    VARIABLE_NAMES = get_variables_names(df)
    
    CHART_CHOICES = (('Option 1', 'Choose one...'),
                        ('Bar chart', 'Bar chart'),
                        ('Pie chart', 'Pie chart'),
                        ('Scatter plot', 'Scatter plot'),
                        ('Histogram', 'Histogram'),
                        ('Line plot', 'Line plot'))

    chart_options = forms.CharField(label="Select chart type to use",
                                  widget = forms.Select(choices=CHART_CHOICES))
    x_axis = forms.CharField(label="Select X axis value",
                                  widget = forms.Select(choices=VARIABLE_NAMES))
    y_axis = forms.CharField(label="Select Y axis if chart is not Pie",
                                  widget = forms.Select(choices=VARIABLE_NAMES))
