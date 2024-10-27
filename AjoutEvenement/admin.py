from django.contrib import admin
from .models import Evenement

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    # Spécifiez les champs à afficher dans la liste des événements
    list_display = ('nom', 'date_debut', 'date_fin', 'type_evenement', 'enseigne', 'commentaire')
    
    # Ajoutez des filtres pour faciliter la recherche
    list_filter = ('date_debut', 'date_fin', 'type_evenement', 'enseigne')

    # Champs de recherche
    search_fields = ('nom', 'adresse', 'enseigne')

    # Affichez les champs dans l'ordre souhaité lors de l'ajout ou de la modification d'un événement
    fields = ('nom', 'lien', 'adresse', 'date_debut', 'date_fin', 'type_evenement', 'enseigne', 'lien_logo')
