from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.data, name='dashboard-data'),
    path('Bar-Chart', views.bar_chart, name='dashboard-barchart'),
    path('Pie-Chart', views.pie_chart, name='dashboard-piechart'),
    path('Scatter-Plot', views.scatter_plot, name='dashboard-scatter'),
    path('Histogram', views.histogram, name='dashboard-histogram'),
    path('Line-plot', views.line_plot, name='dashboard-lineplot'),
    path('Box-plot', views.boxplot, name='dashboard-boxplot'),
    path('chart', views.select_chart, name='dashboard-select_chart'),
    path('upload', views.upload_file, name='dashboard-upload_file')
] + static(settings.STATIC_URL, 
           document_root=settings.STATIC_ROOT)