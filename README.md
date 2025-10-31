# Planification du Raccordement Électrique

##  Contexte  
Ce projet a été initié par la mairie d’une petite ville suite à des intempéries ayant détruit les connexions électriques. L’objectif est de proposer un plan de raccordement qui :  
- restaure la connexion pour le plus grand nombre de bâtiments,  
- minimise le coût global,  
- optimise la mutualisation des lignes (réutilisation, partage de tronçons).

##  Objectifs du dépôt  
- Modéliser les infrastructures à l’aide de données géospatiales (shapefiles) et d’un fichier réseau : `reseau_en_arbre.csv` / `.xlsx`.  
- Définir une **métrique de priorisation** pour classer les bâtiments selon coût + facilité de raccordement + mutualisation.  
- Produire un plan de raccordement avec ordre de priorité, estimation des coûts et des durées.  
- Générer des cartes (via QGIS) pour illustrer le plan proposé.

##  Structure du dépôt  
```
planification_raccordement_electrique/
│
├── data/                # fichiers sources : BATIMENTS, LIGNES, RESEAU
│   ├── batiments.shp
│   ├── lignes.shp
│   └── reseau_en_arbre.xlsx
│
├── src/                 # code Python / scripts d’analyse
│   └── main.py
│
├── outputs/             # résultats : cartes, rapports, fichiers finaux
│   └── rapport_planification.pdf
│
├── README.md            # ce fichier
├── .gitignore            # fichiers à ignorer
└── LICENSE              # licence du dépôt
```

## 🚀 Installation et exécution  
1. Clonez ce dépôt :  
   ```bash
   git clone https://github.com/AKRZ781/planification_raccordement_electrique.git
   cd planification_raccordement_electrique
   ```  
2. Installez les dépendances (exemple avec pip) :  
   ```bash
   pip install pandas geopandas networkx
   ```  
3. Lancez le script principal :  
   ```bash
   python src/main.py
   ```  
   Le script doit :  
   - fusionner les données, supprimer les doublons,  
   - calculer coûts & durée selon type de ligne (aérien / semi-aérien / fourreau),  
   - produire un classement de priorité des bâtiments,  
   - générer les cartes et exporter le rapport .


## 📄 Résultats attendus  
- Tableau de priorisation des bâtiments : estimation coût/prise + durée/prise.  
- Carte QGIS/PDF illustrant les phases de raccordement et les zones de mutualisation optimisées.  
- Rapport final au format PDF (`outputs/rapport_planification.pdf`) à déposer dans le dossier **outputs/**.




---
_Licence : MIT_  
