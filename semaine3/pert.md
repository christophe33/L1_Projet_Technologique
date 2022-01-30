# PERT c'est quoi ?

C'est une méthode permettant de mettre en ordre sous forme de **graphe** plusieurs tâches qui grâce à leur dépendance et à leur chronologie concourent toutes à l’obtention d’un produit fini.

Elle s’attache à mettre en évidence les liaisons qui existent entre les différentes tâches d’un projet et à définir le **chemin** dit  **critique** .

Avant de réaliser un diagramme PERT il faut avoir identifié les relations de dépendance entre les tâches. Cela peut se traduire par une ce que l'on appelle une **matrice des dépendances**

## Exemple:
Nous allons prendre une analogie avec le batiment. Considérons la construction d'une maison et les taches suivantes : 
1. Fondations et Murs
1. Charpente
1. Toiture
1. Plomberie
1. Électricité
1. Finition

La matrice des dépendances peut-être remplie avec les valeurs 0 et 1 : 
* 0 indique pas de dépendance direct
* 1 indique une dépendance direct

la matrice des dépendances de la construction de la maison peut alors s'écrire : 

|      | 1    | 2    | 3    | 4    | 5    | 6    |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1    | 0    | 0    | 0    | 0    | 0    | 0    |
| 2    | 1    | 0    | 0    | 0    | 0    | 0    |
| 3    | 0    | 1    | 0    | 0    | 0    | 0    |
| 4    | 0    | 1    | 0    | 0    | 0    | 0    |
| 5    | 0    | 1    | 0    | 0    | 0    | 0    |
| 6    | 0    | 0    | 1    | 1    | 1    | 0    |

