import requests
from django import forms
from .models import Evenement
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

class EvenementForm(forms.ModelForm):
    accepter_cgu = forms.BooleanField(
        label="J'accepte les Conditions Générales d'Utilisation (CGU)",
        required=True
    )

    class Meta:
        model = Evenement
        fields = [
            'nom', 'lien', 'adresse', 'date_debut', 
            'date_fin', 'type_evenement', 'enseigne', 'lien_logo', 
            'commentaire'
        ]
        widgets = {
            'date_debut': DateInput(attrs={'type': 'date', 'placeholder': 'jj/mm/aaaa'}, format='%d/%m/%Y'),
            'date_fin': DateInput(attrs={'type': 'date', 'placeholder': 'jj/mm/aaaa'}, format='%d/%m/%Y'),
        }
        
        labels = {
            'nom': 'Nom de l\'événement',
            'lien': 'Lien Internet',
            'adresse': 'Adresse de l\'événement',
            'date_debut': 'Date de début',
            'date_fin': 'Date de fin',
            'type_evenement': 'Type d\'événement',
            'enseigne': 'Organisateur (Enseigne)',
            'lien_logo': 'Lien du logo',
            'commentaire': 'Commentaire ',
        }

    def __init__(self, *args, **kwargs):
        super(EvenementForm, self).__init__(*args, **kwargs)
        
        # Placeholders et styles pour augmenter la largeur des champs
        self.fields['nom'].widget.attrs.update({
            'placeholder': 'Entrer le nom de l\'événement', 
            'style': 'width: 300px;'
        })
        self.fields['lien'].widget.attrs.update({
            'placeholder': 'https://www.mon-evenement.com', 
            'style': 'width: 300px;'
        })
        self.fields['adresse'].widget.attrs.update({
            'placeholder': 'Entrer l\'adresse de l\'événement', 
            'style': 'width: 300px;'
        })
        self.fields['date_debut'].widget.attrs.update({
            'placeholder': 'jj/mm/aaaa', 
            'style': 'width: 150px;'
        })
        self.fields['date_fin'].widget.attrs.update({
            'placeholder': 'jj/mm/aaaa', 
            'style': 'width: 150px;'
        })
        self.fields['type_evenement'].widget.attrs.update({
            'placeholder': 'Type de l\'événement', 
            'style': 'width: 300px;'
        })
        self.fields['enseigne'].widget.attrs.update({
            'placeholder': 'Entrer le nom de l\'organisateur', 
            'style': 'width: 300px;'
        })
        self.fields['lien_logo'].widget.attrs.update({
            'placeholder': "https://www.example.com/logo.png", 
            'style': 'width: 300px;'
        })
        self.fields['commentaire'].widget.attrs.update({
            'placeholder': 'Ajouter un commentaire à Cartagrimpe', 
            'style': 'height: 50px;'
        })

    def clean(self):
        cleaned_data = super().clean()
        
        # Vérification des CGU
        accepter_cgu = cleaned_data.get('accepter_cgu')
        if not accepter_cgu:
            raise ValidationError("Vous devez accepter les Conditions Générales d'Utilisation pour soumettre ce formulaire.")

        # Vérification de l'adresse avec OpenStreetMap
        adresse = cleaned_data.get('adresse')
        valide, _, _ = self.valider_adresse(adresse)
        if not valide:
            self.add_error('adresse', "L'adresse n'est pas valide sur OpenStreetMap.")

        # Vérification des dates
        date_debut = cleaned_data.get("date_debut")
        date_fin = cleaned_data.get("date_fin")
        if date_fin and date_debut and date_fin < date_debut:
            self.add_error('date_fin', "La date de fin doit être égale ou supérieure à la date de début.")

        # Vérification de l'URL du lien internet
        lien_internet = cleaned_data.get('lien')
        if lien_internet:
            self.valider_url(lien_internet, 'lien', 'Le lien internet est inaccessible ou invalide.')

        # Vérification du lien du logo et du type de contenu
        lien_logo = cleaned_data.get('lien_logo')
        if lien_logo:
            self.valider_url(lien_logo, 'lien_logo', 'Le lien du logo est inaccessible.', verif_image=True)

        return cleaned_data

    def valider_adresse(self, adresse):
        geolocator = Nominatim(user_agent="mon_application")
        try:
            location = geolocator.geocode(adresse)
            if location:
                return True, location.latitude, location.longitude
            else:
                return False, None, None
        except GeocoderTimedOut:
            return self.valider_adresse(adresse)  # Réessaye si le géocodeur a échoué

    def valider_url(self, url, field_name, error_message, verif_image=False):
        try:
            response = requests.head(url, timeout=5)
            if response.status_code != 200:
                self.add_error(field_name, error_message)
            elif verif_image and 'image' not in response.headers.get('Content-Type', ''):
                self.add_error(field_name, 'Le lien du logo ne mène pas à une image.')
        except requests.RequestException:
            self.add_error(field_name, error_message)
