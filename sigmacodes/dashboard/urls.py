from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.data, name='dashboard-data'),
    path('demo', views.demo_chart, name='dashboard-demo_chart'),
    path('upload', views.upload_file, name='dashboard-upload_file')
] + static(settings.STATIC_URL, 
           document_root=settings.STATIC_ROOT)