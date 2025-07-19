from django.urls import path
from . import views

urlpatterns = [
    
    path('import/', views.import_file, name='import_file'),
    path('employees/', views.employee_list, name='employee_list'),
    path('edit/edit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('export/', views.export_file, name='export_file'),
]