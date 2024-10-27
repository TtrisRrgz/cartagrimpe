"""
URL configuration for cartagrimpe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AjoutEvenement import views as ajout_views  # Importez vos vues ici

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ajout_views.index, name='index'),
    path('ajouter/', ajout_views.ajouter_evenement, name='ajouter_evenement'),
    path('calendrier/', ajout_views.afficher_evenements, name='calendrier_evenement'),  # Utilisez afficher_evenements ici
    path('mentions/', ajout_views.mentions_legales, name='mentions_legales'),
    path('a_propos/', ajout_views.a_propos, name='a_propos'),  
]
