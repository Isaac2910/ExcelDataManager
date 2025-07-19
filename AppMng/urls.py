from django.urls import path
from . import views

urlpatterns = [
    
    path('import/', views.import_file, name='import_file'),
    path('employees/', views.employee_list, name='employee_list'),
    path('export/', views.export_file, name='export_file'),
]