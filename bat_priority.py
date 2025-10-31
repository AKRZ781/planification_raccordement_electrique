import pandas as pd

#  Charger les deux fichiers sources
df = pd.read_excel("data/reseau_en_arbre.xlsx")
df_etat = pd.read_excel("data/etat_batiment.xlsx")

# 🔹 Supprimer tous les doublons sur id_batiment (ou sur toutes les colonnes si tu préfères)
df = df.drop_duplicates()


#  Jointure externe gauche pour ramener la colonne 'state_batiment'
df_merge = pd.merge(
    df,
    df_etat[['id_batiment', 'state_batiment']],
    on='id_batiment',
    how='left'
)

#  Filtrer uniquement les lignes correspondant à la condition
df_filtered = df_merge[
    (df_merge["state_batiment"] == "à_reparer") &
    (df_merge["infra_type"] == "a_remplacer")
].copy()

#  Créer la colonne "difficulté"
df_filtered["difficulté"] = df_filtered["longueur"] / df_filtered["nb_maisons"]

#  Regrouper par id_batiment et sommer la difficulté
df_grouped = (
    df_filtered.groupby("id_batiment", as_index=False)
    .agg({
        "nb_maisons": "first",      # garde la première valeur
        "difficulté": "sum"         # somme des difficultés
    })
)

#  Trier par difficulté croissante
df_grouped = df_grouped.sort_values(by="difficulté", ascending=True)

#  Ajouter une colonne d'index (rang)
df_grouped["index"] = range(1, len(df_grouped) + 1)

#  Supprimer la colonne difficulté
df_grouped = df_grouped.drop(columns=["difficulté"])

#  Export final
df_grouped.to_excel("outputs/priorité_chantier.xlsx", index=False)

print(" Fichier final créé : outputs/priorité_chantier.xlsx")
