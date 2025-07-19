from django import forms
from django.core.exceptions import ValidationError
from .models import Employee

# Validation pour le fichier Excel
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 Mo

def validate_excel_file(file):
    
    if not file.name.endswith('.xlsx'):
        raise ValidationError("fichier non valide.")

    if file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        raise ValidationError("fichier incorrect .")

    if file.size > MAX_FILE_SIZE:
        raise ValidationError("Fichier trop volumineux (max 10 Mo).")

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label="Fichier Excel (.xlsx)",
        validators=[validate_excel_file],
        widget=forms.FileInput(attrs={'accept': '.xlsx'})
    )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nom', 'email', 'salaire']