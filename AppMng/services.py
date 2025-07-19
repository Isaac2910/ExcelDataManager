
import pandas as pd
from django.core.exceptions import ValidationError
from .models import Employee



def traiter_fichier_employes(fichier):
    try:
        df = pd.read_excel(fichier, engine='openpyxl')
    except Exception as e:
        raise ValidationError(f"Erreur de lecture Excel : {e}")

    # Nettoyage des noms de colonnes
    df.columns = [col.strip().lower() for col in df.columns]
    # Vérification des colonnes requises
    colonnes_requises = ['email', 'nom', 'salaire']
    for col in colonnes_requises:
        if col not in df.columns:
            raise ValidationError(f"Colonne manquante : {col}")
    # Enregistrer les employés
    for _, row in df.iterrows():
        if pd.isnull(row['email']):
            continue

        email = str(row['email']).strip().lower()
        nom = str(row['nom']).strip().title()
        salaire = row['salaire']

        Employee.objects.update_or_create(
            email=email,
            defaults={
                'nom': nom,
                'salaire': salaire
            }
        )
