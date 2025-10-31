import pandas as pd

# Chargement du fichier réseau 
network_df = pd.read_excel("reseau_en_arbre.xlsx")

#  Sélection des tronçons à remplacer 
broken_network_df = network_df[network_df["infra_type"] == "a_remplacer"]

#  Création des ensembles d'identifiants 
set_id_batiments = set(network_df["id_batiment"].values)
set_id_broken_batiments = set(broken_network_df["id_batiment"].values)

#  Création des listes pour les états des bâtiments 
list_id_batiment = []
state_batiment = []

for id_batiment in set_id_batiments:
    list_id_batiment.append(id_batiment)
    if id_batiment in set_id_broken_batiments:
        state_batiment.append("à_reparer")
    else:
        state_batiment.append("intact")

#  Construction du DataFrame final 
state_df = pd.DataFrame({
    "id_batiment": list_id_batiment,
    "state_batiment": state_batiment
})

#  Export vers Excel 
state_df.to_excel("data/etat_batiment.xlsx", index=False, columns=["id_batiment", "state_batiment"])

print("Fichier 'etat_batiment.xlsx' généré avec succès !")