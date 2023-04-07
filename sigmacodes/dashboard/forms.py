from django import forms
from .utility import get_variables_names
import pandas as pd

# Read in demo data set
df = pd.read_csv('employee_data.csv')

# Convert data set to html for rendering using iframe html tag
df_table = df.to_html(col_space=80)
text_file = open('static/dataframe.html', 'w')
text_file.write(df_table)
text_file.close

# Classify dataframe variables into nominal and numerical
nominal_variables, numerical_variables, numerical_with_none = get_variables_names(df)


class DataSource(forms.Form):
    """Form for selecting data set to use"""

    DATA_CHOICES = (('Option 1', 'Choose one...'),
                    ('Use demo data', 'Use demo data'),
                    ('Upload data', 'Upload data'))

    data = forms.CharField(label="Select data to visualize",
                           widget=forms.Select(choices=DATA_CHOICES))


class UploadData(forms.Form):
    """Form for uploading file"""
    upload_data = forms.FileField(
        allow_empty_file=False, label="Upload data (csv or excel)")


class ChartSpecs(forms.Form):
    """For for selecting visualization options"""

    CHART_CHOICES = (('Bar chart', 'Bar chart'),
                     ('Pie chart', 'Pie chart'),
                     ('Scatter plot', 'Scatter plot'),
                     ('Histogram', 'Histogram'),
                     ('Line plot', 'Line plot'),
                     ('Box plot', 'Box plot'))

    chart_options = forms.CharField(label="Select chart type to use",
                                    widget=forms.Select(choices=CHART_CHOICES))
    nominal_x = forms.CharField(label="X axis (Nominal)",
                                widget=forms.Select(choices=nominal_variables))
    numerical_x = forms.CharField(label="X axis (Numerical)",
                                  widget=forms.Select(choices=numerical_variables))
    numerical_y = forms.CharField(label="Y axis (Numerical)",
                                  widget=forms.Select(choices=numerical_variables))
    numerical_none = forms.CharField(label="Y axis (Numerical)",
                                  widget=forms.Select(choices=numerical_with_none))
    color_by = forms.CharField(label="Color by",
                               widget=forms.Select(choices=numerical_with_none))
    bins = forms.ChoiceField(choices=[(x, x) for x in range(1, 21)],
                             label='Number of bins')
