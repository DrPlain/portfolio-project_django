from django import forms
from .utility import get_variables_names
import pandas as pd


df = pd.read_csv('employee_data.csv')
df_table = df.head(101).to_html(col_space=80)
nominal_variables, numerical_variables = get_variables_names(df)
    
class DataSource(forms.Form):
    DATA_CHOICES = (('Option 1', 'Choose one...'),
                    ('Use demo data', 'Use demo data'),
                    ('Upload data', 'Upload data'))
    
    data = forms.CharField(label="Select data to visualize",
                                  widget = forms.Select(choices=DATA_CHOICES))
    

class UploadData(forms.Form):
    upload_data = forms.FileField(allow_empty_file=False, label="Upload data (csv or excel)")

class SelectChart(forms.Form):
    CHART_CHOICES = (('Bar chart', 'Bar chart'),
                     ('Pie chart', 'Pie chart'),
                     ('Scatter plot', 'Scatter plot'),
                     ('Histogram', 'Histogram'),
                     ('Line plot', 'Line plot'),
                     ('Box plot', 'Box plot'))

    chart_options = forms.CharField(label="Select chart type to use",
                                  widget = forms.Select(choices=CHART_CHOICES))
    
class NominalNumerical(forms.Form):
    new_numerical = list(numerical_variables)
    new_numerical.insert(0, ('None', 'None'))
    x_axis = forms.CharField(label="X axis (Nominal)",
                                  widget = forms.Select(choices=nominal_variables))
    y_axis = forms.CharField(label="Y axis (Numerical)",
                                  widget = forms.Select(choices=new_numerical))
    
class NominalForm(forms.Form):
    x_axis = forms.CharField(label="X axis (Nominal)",
                                  widget = forms.Select(choices=nominal_variables))
    
class NumericalForm(forms.Form):
    y_axis = forms.CharField(label="Y axis (Numerical)",
                                  widget = forms.Select(choices=numerical_variables))
    
class ScatterForm(forms.Form):
    new_numerical = list(numerical_variables)
    new_numerical.insert(0, ('None', 'None'))
    x_axis = forms.CharField(label="X axis (Numerical)",
                                  widget = forms.Select(choices=numerical_variables))
    y_axis = forms.CharField(label="Y axis (Numerical)",
                                  widget = forms.Select(choices=numerical_variables))
    color_by = forms.CharField(label="Color by",
                                  widget = forms.Select(choices=new_numerical))
    
class HistogramForm(forms.Form):
    x_axis = forms.CharField(label="X axis (Numerical)",
                                  widget = forms.Select(choices=numerical_variables))
    bins = forms.ChoiceField(choices=[(x, x) for x in range(1, 21)],
                             label='Number of bins')
    
class LineplotForm(forms.Form):
    new_nominal = list(numerical_variables)
    new_nominal.insert(0, ('None', 'None'))
    x_axis = forms.CharField(label="X axis (Numerical)",
                                  widget = forms.Select(choices=numerical_variables))
    y_axis = forms.CharField(label="Y axis (Numerical)",
                                  widget = forms.Select(choices=numerical_variables))
    label = forms.CharField(label="Label",
                                  widget = forms.Select(choices=new_nominal))

class BoxplotForm(forms.Form):
    x_axis = forms.CharField(label="X axis (Numerical)",
                                  widget = forms.Select(choices=numerical_variables))