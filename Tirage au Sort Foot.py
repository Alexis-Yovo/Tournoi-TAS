import random

# Définition des chapeaux avec les équipes
chapeau_1 = ["Maroc", "Egypte", "Algérie", "Côte d’Ivoire", "Nigeria"]
chapeau_2 = ["Tunisie", "Cameroun", "Mali", "Rd Congo", "Afrique du Sud", "Burkina Faso"]
chapeau_3 = ["Gabon", "Angola", "Zambie", "Ouganda", "Guinée Equatoriale", "Bénin"]
chapeau_4 = ["Mozambique", "Comores", "Tanzanie", "Soudan", "Zimbabwe", "Botswana"]

# Création des groupes
groupes = {f"Groupe {i+1}": [] for i in range(6)}

# Ajout du Maroc dans le groupe 1
groupes["Groupe 1"].append("Maroc")

# Fonction pour tirer une équipe d'un chapeau sans répétition
def tirer_equipe(chapeau, equipes_deja_tirees):
    equipe = random.choice(chapeau)
    while equipe in equipes_deja_tirees:
        equipe = random.choice(chapeau)
    return equipe

# Tirage au sort pour les autres groupes
equipes_tirees = {"Maroc"}  # On commence avec le Maroc déjà tiré

for i in range(6):
    if i == 0:  # Groupe 1
        # On tire les autres équipes pour le groupe 1
        groupes[f"Groupe {i+1}"].append(tirer_equipe(chapeau_2, equipes_tirees))
        groupes[f"Groupe {i+1}"].append(tirer_equipe(chapeau_3, equipes_tirees))
        groupes[f"Groupe {i+1}"].append(tirer_equipe(chapeau_4, equipes_tirees))
    else:
        # Tirage pour les autres groupes
        groupes[f"Groupe {i+1}"].append(tirer_equipe(chapeau_1, equipes_tirees))
        groupes[f"Groupe {i+1}"].append(tirer_equipe(chapeau_2, equipes_tirees))
        groupes[f"Groupe {i+1}"].append(tirer_equipe(chapeau_3, equipes_tirees))
        groupes[f"Groupe {i+1}"].append(tirer_equipe(chapeau_4, equipes_tirees))

    # Ajout des équipes tirées à l'ensemble des équipes déjà tirées
    equipes_tirees.update(groupes[f"Groupe {i+1}"])

# Affichage des groupes
for groupe, equipes in groupes.items():
    print(f"{groupe}: {', '.join(equipes)}")
