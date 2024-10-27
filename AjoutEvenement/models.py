from django.db import models
from django.core.exceptions import ValidationError

class Evenement(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    lien = models.URLField(max_length=200, help_text="(https://www.MonEvenement.com)", null=True)
    adresse = models.CharField(max_length=255, help_text="(Vérifier l'adresse sur <a href='https://www.openstreetmap.org/'>OpenStreetMap</a>)")
    date_debut = models.DateTimeField()  # Champ pour la date de début
    date_fin = models.DateTimeField()  # Champ pour la date de fin
    type_evenement = models.CharField(
        max_length=50, 
        choices=[
            ('Film', 'Film'),
            ('Compétition', 'Compétition'),
            ('Rassemblement', 'Rassemblement'),
            ('Contest', 'Contest'),
            ('Autre', 'Autre'),
        ], 
        default='Autre'  # Valeur par défaut
    )
    # Liste d'enseignes pour le champ `enseigne`
    L_enseigne = [
        ("Autre", "Autre"),
        ("Arkose", "Arkose"),
        ("climbup", "Climb'Up"),
        ("FFME", "FFME"),
        ("Blocout", "Bloc'Out"),
        ("FFME", "FFME"),
        ("IFSC", "IFSC"),
    ]
    
    enseigne = models.CharField(max_length=50, choices=L_enseigne)  # Utilisation de CharField avec des choix
    lien_logo = models.URLField(max_length=2000, blank=True, null=True, help_text="(Obligatoire si l\'organisateur est Autre)")  # Permettre null pour le moment
    commentaire = models.TextField(default="Pas de commentaire", help_text="(Non vide, Description, doutes, ...)")  # Exemple de valeur par défaut
    
    def clean(self):
        super().clean()
        if self.enseigne == "Autre" and not self.lien_logo:
            raise ValidationError({'lien_logo': "Ce champ est obligatoire si l'organisateur n'est pas est identifié."})

    def __str__(self):
        return self.nom
    
