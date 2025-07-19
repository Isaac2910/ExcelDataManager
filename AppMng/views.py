from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .forms import UploadFileForm
from .services import traiter_fichier_employes
from .models import Employee
from django.http import HttpResponse
import pandas as pd
from django.core.paginator import Paginator


#importation du fichier Excel
def import_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.cleaned_data['file']
            try:
                traiter_fichier_employes(fichier)
                return redirect('employee_list')
            except ValidationError as e:
                form.add_error('file', e)
    else:
        form = UploadFileForm()

    return render(request, 'employees/import.html', {'form': form})

# Affichage de la liste des employés avec pagination
def employee_list(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees, 10) #par 10 emp....
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.htmx:
        return render(request, 'employees/partials/employee_table.html', {'page_obj': page_obj})

    return render(request, 'employees/list.html', {'page_obj': page_obj})
# Exportation des employés vers un fichier Excel
def export_file(request):
    employees = Employee.objects.all()
    df = pd.DataFrame(list(employees.values('nom', 'email', 'salaire')))
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=les_employees.xlsx'
    df.to_excel(response, index=False)
    return response


# Home view for the application

def home(request):
    return render(request, 'home.html')
