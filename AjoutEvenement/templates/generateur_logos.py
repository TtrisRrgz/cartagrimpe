import requests
from PIL import Image
from io import BytesIO

def hex_to_rgba(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b, 255)

def Creer_icone(lien, Ev):
    Icon = Image.new(mode="RGBA", size=(80, 100))
    L, H = Icon.size
    NewIcon = Icon.load()  # Récupération des pixels

    # Application des couleurs basées sur l'événement
    color_map = {
        'Contest': '#850606',
        'Rassemblement': '#0a5c1f',
        'Compétition': '#fcdc12',
        'Film': '#000000',
        'Autre':'#FFFFFF'  
    }
    color = hex_to_rgba(color_map.get(Ev, '#FFFFFF'))  # Default to white

    # Dessiner l'icône colorée
    for l in range(L):
        for h in range(H):
            if (40 - l) ** 2 + (40 - h) ** 2 < 1200 or (h < 1.5 * l + 30 and h < -1.5 * l + 150 and h > 40):
                NewIcon[l, h] = (255, 255, 255, 255)
            elif (40 - l) ** 2 + (40 - h) ** 2 < 1600 or (h < 1.5 * l + 40 and h < -1.5 * l + 160 and h > 40):
                NewIcon[l, h] = color

    # Charger l'image externe à ajouter sur l'icône
    try:
        response = requests.get(lien)
        response.raise_for_status()  # Lève une exception pour les réponses d'erreur
        Im1 = Image.open(BytesIO(response.content)).convert(mode='RGBA')
    except requests.exceptions.HTTPError as http_err:
        print(f"Erreur lors de la récupération de l'image: {http_err}")
        return Icon  # Retourne l'icône vide
    except Exception as e:
        print(f"Erreur lors de la création de l'icône pour l'image: {e}")
        return Icon  # Retourne l'icône vide

    # Redimensionner l'image
    Newx = int(Im1.size[0] * 52 / max(Im1.size[0], Im1.size[1]))
    Newy = int(Im1.size[1] * 52 / max(Im1.size[0], Im1.size[1]))
    Im1 = Im1.resize((Newx, Newy))
    pix_origine = Im1.load()  # Récupérer les pixels

    # Ajouter l'image à l'icône
    for l in range(L):
        for h in range(H):
            if 40 - Newx // 2 < l < 40 + Newx // 2 and 40 - Newy // 2 < h < 40 + Newy // 2 and pix_origine[l - (40 - Newx // 2), h - (40 - Newy // 2)][3] > 200:
                NewIcon[l, h] = pix_origine[l - (40 - Newx // 2), h - (40 - Newy // 2)]

    return Icon

# Liste des enseignes et leurs liens
# Liste des enseignes et leurs liens
enseignes = {
    'FFME': "https://www.ffmeaura.fr/assets/images/logo-ffme-square.png",
    # 'IFSC': "https://upload.wikimedia.org/wikipedia/fr/1/19/Ifsc-logo2015.png",
    #  'arkose': 'https://koust.net/wp-content/uploads/2020/06/logo-arkose-noir.png',  # Remplacez par l'URL correcte
    #  'vertical art': 'https://www.salon-escalade.com/pictures/exhibitors/c962b8za96-bc69-2b.jpg',  # Remplacez par l'URL correcte
     # 'climb up': 'https://pitchoun-sorties.fr/wp-content/uploads/2022/09/logo-climb-up.png',  # Assurez-vous que ce lien est valide aussi
}


# Créer les logos
for enseigne, lien in enseignes.items():
    for Ev in ['Contest', 'Rassemblement', 'Compétition', 'Film', 'Autre']:
        try:
            # Utiliser la fonction pour les autres enseignes
            Icon = Creer_icone(lien, Ev)
            Icon.save(f"Image/{enseigne}_{Ev}.png")
            print(f"Logo créé pour {enseigne} - {Ev}: Image/{enseigne}_{Ev}.png")
        except Exception as e:
            print(f"Erreur lors de la création de l'icône pour {enseigne} - {Ev}: {e}")
