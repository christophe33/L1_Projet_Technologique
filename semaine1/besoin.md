# Conduite de projet (Génie Logiciel)



* Définition logiciel ? 
* Participants (rôles)
	* L'utilisateur
	* Le développeur
	* Le propriétaire (celui qui payer et qui va recevoir l'arget)

## Quels sont les étapes permettant de produire un logiciel ?

Trois grande étapes

### Commencement : Naissance du logiciel
   * Utilisateur --> besoin
   * Propriétaire va comprendre le besoin de l'utilisateur et demander au développeur de réaliser un travail
   * Propriétaire + développeur --> début du cycle de développement 
   
### Exploitation
   * Le propriétaire va fournir le logiciel aux utilisateurs
   * L'utilisateur utilise le logiciel qui entraîne des anomalies et demande des évolutions. Boucle de rétroaction entre développeur et propriétaire
   
### Fin de vie du logiciel
   * Plus d'utilisateur
   * La maintenance du logiciel est trop élevée --> trop cher pour le propriétaire

### Cycle de vie

Cycle de vie = Cycle de dev + PréProd + Prod/Maintenance

Différents types de projet:
* Projet de mise en prod (tout le cycle de vie)
* Projet de developpement (cycle de dev)

## Et pour nous ?

Essentiellement : Projet de developpement

* Cahier des charges : expression du besoin c'est le propriétaire qui est repsonsable 
* Le développeur spécifie ce qu'il est capable de produire dans le cahier des charges
* Si le propriétaire accepte on entre dans le cycle de dev
* Livraison

### Taxonomie

* MOA : maitrise d'ouvrage: le propriétaire
* MOE : maitrise d'oeuvre : le développeur (une équipe de plusieurs développeurs pour les gros projets)
* L'utilisateur n'apparait pas, il est représenté par le propriétaire

## Les besoins

Un besoin est une demande de la maîtrise d'ouvrage. Le besoin est rédigée par le propriétaire ou l'utilisateur du logiciel (ils savent ce qu'ils veulent avoir). Pour autant, le besoin est à destination des développeurs qui vont devoir les comprendre pour les réaliser.
Un besoin doit être exprimé clairement. La maîtrise d'ouvrage doit prendre une attention toute particulière à la rédaction des besoins.

### Lecture du cahier des charges 

Projet VideoTracker : Un logiciel destiné à l'étude cinématique du mouvement d'un objet à partir d'une vidéo.

### Exemple tiré du cahier des charges : 
* Besoin : À partir d’un menu Fichier proposer un menu *Quitter*
* Exigence : 
	* Dans la fenêtre principale du logciel il y aura un bandeau situé en haut de la fenêtre. 
  	* Ce bandeau contiendra un menu déroulant nommé Fichier qui propose deux items dont l'item **Quitter**.
  	* cliquer sur *Quitter* aura pour effet de fermer l'application
  	
**Remarque** Nous avons à faire ici à une exigence fonctionnelle, c'est à dire directement en lien avec l'utilisateur. 
Il est recommandé de la rédiger comme un scénario et d'y ajouter si nécessaire un schéma

### Rédiger le besoin concernant le chargement de la vidéo:
* Besoin : À partir d’un menu Fichier proposer un menu *Charger une vidéo*
* Exigence : 
	* Le menu déroulant Fichier propose également un item **Charger une vidéo**
	* Cet item est placé au dessus de l'item **Quitter**
	* Cliquer sur cet item ouvre un explorateur de fichier permettant de naviguer dans les répertoires de l'ordinateur.
	* Le répertoire de départ pour la navigation sera un répertoire par défaut du logiciel : *vidéos*
	* Les types des fichiers vidéos acceptés seront : .mp4, .avi, wmv (Il faut se poser la question : c'est quoi une vidéo ?)
	

## Liste des bonnes pratiques :

**Rédaction**
* préciser les besoins -> description précise
* identifier les besoins de manière unique -> donner un identifiant unique


**Gestion des modifications**
* qualifier le type des besoins, leur importance et leur difficulté
* planifier les besoins dans le temps
* clore un besoin


