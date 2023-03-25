from django import forms
from .utility import get_variables_names
import pandas as pd

df = pd.read_csv('employee_data.csv')
nominal_variables, numerical_variables = get_variables_names(df)
    
class DataSource(forms.Form):
    DATA_CHOICES = (('Option 1', 'Choose one...'),
                    ('Use demo data', 'Use demo data'),
                    ('Upload data', 'Upload data'))
    
    data = forms.CharField(label="Select data to visualize",
                                  widget = forms.Select(choices=DATA_CHOICES))
    

class UploadData(forms.Form):
    upload_data = forms.FileField(allow_empty_file=False)

class SelectChart(forms.Form):
    CHART_CHOICES = (('Bar chart', 'Bar chart'),
                     ('Pie chart', 'Pie chart'),
                     ('Scatter plot', 'Scatter plot'),
                     ('Histogram', 'Histogram'),
                     ('Line plot', 'Line plot'))

    chart_options = forms.CharField(label="Select chart type to use",
                                  widget = forms.Select(choices=CHART_CHOICES))
    
class NominalNumerical(forms.Form):
    x_axis = forms.CharField(label="Select X axis value",
                                  widget = forms.Select(choices=nominal_variables))
    y_axis = forms.CharField(label="Select Y axis value",
                                  widget = forms.Select(choices=numerical_variables))
    
class NominalForm(forms.Form):
    x_axis = forms.CharField(label="Select X axis value",
                                  widget = forms.Select(choices=nominal_variables))
    
class NumericalForm(forms.Form):
    y_axis = forms.CharField(label="Select Y axis value",
                                  widget = forms.Select(choices=numerical_variables))