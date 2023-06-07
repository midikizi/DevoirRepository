[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/qCAmzLi7)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11300921&assignment_repo_type=AssignmentRepo)
# API-Gestion-Flotte

La congrégation des sœurs clarisses dispose d’une importante police flotte d’assurance. Dans cette flotte, il y a des voitures et des motos. Elles appartiennent soit à la congrégation, soit aux communautés religieuses, soit aux sœurs à titre individuel. L’assurance donne une cotation pour chaque engin. L’économat qui gère la flotte majore la cotation et facture le/la propriétaire.

On décide de mettre en place un logiciel de gestion de la flotte d'assurance. 

Pour l’outil, voici les attentes :

-	Une liste des engins sur la base des immatriculations avec la possibilité de faire des requêtes : 
o	par propriétaire
o	par catégorie (voiture ou moto)

Quand on consulte un propriétaire, que l’outil affiche les immatriculations de tous les engins qui lui appartiennent :
-	la cotation de l’assurance, la majoration de l’économat (ce que l’économat gagne) et le montant total de la facture que l’économat transmet aux propriétaires d’engins
-	la possibilité de générer les factures pour les propriétaires d’engins
-	la possibilité de suivre les règlements (par tranche ou total) par les propriétaires d’engins


## Travail à faire :
Vous mettrez en place une API avec FastAPI satisfaisant les spécifications suivantes :
-	Faites la modélisation du système en créant dans un fichier `models.py` les modèles Pydantic ;
-	Créer un endpoint `/category/<category>` où `<category>` est la catégorie d’engin et qui renvoie la liste des engins de cette catégorie (ici on enverra une liste vide)
-	Créer un endpoint `/owner/<owner>` où `<owner>` est le propriétaire de l’engin et qui renvoie la liste des engins du propriétaire
-	Créer un endpoint `/bills/<owner>` qui renvoie la facture imputée à `<owner>` sur la base des immatriculations qui sont les siennes

Enfin, déployez cette application en ligne et fournissez son lien dans le dépôt en ligne (le champ site web du dépôt).

NB : Vous vous assurerez que les validations des données sont bien effectives.
