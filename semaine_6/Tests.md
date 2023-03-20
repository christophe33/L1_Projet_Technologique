# Tester votre Projet

## Plusieurs niveaux de tests
### Tests de validation

Un test de validation est un type de test informatique qui permet de vérifier si toutes les exigences client, décrites dans le document de spécification du logiciel, sont respectées.

### Tests d'intégration

Un test d'intégration valide les résultats des interactions entre plusieurs composants et permet de vérifier que leur assemblage s'est produit sans défaut. Il peut être manuel ou automatisé.

### Tests unitaires

Un test unitaire est une procédure permettant de vérifier le bon fonctionnement d'une partie précise d'un logiciel ou d'une portion d'un programme (classe, méthode, fonction).

## Pourquoi écrire des tests

Une application dont le code est correctement couvert par les tests permettra de repérer précisément les erreurs et donc de les corriger.

Les tests permettent de s'assurer que votre code fonctionne correctement pour un ensemble de conditions données.

Les tests obligent à réfléchir au code dans des conditions inhabituelles.

Les tests permettent de s'assurer que les changements apportés au code ne cassent pas les fonctionnalités existantes.

Un bon test nécessite un **code modulaire**, on veut une **cohérence forte** (des petits objets) avec un **couplage faible**, ce qui est la marque d'une bonne conception d'architecture du projet.

## Quand faire les tests

Le plus tôt possible. Il ne faut pas attendre la fin du projet pour faire les tests.

## Déterminer ce qu'il faut tester

Nous allons adopter une stratégie qui consiste à vérifier que les méthodes de notre projet produisent bien les résultats attendus. C'est le principe des **tests unitaires**. 

Il n'est pas utile de tester toutes les méthodes, en programmation orientée objet une bonne pratique consiste à tester uniquement les méthodes publiques, c'est-à-dire les méthodes qui vont permettre de communiquer avec d'autres objets. En d'autres termes, nous allons **tester les interfaces** de notre projet. Nous n'avons pas besoin de savoir comment sont effectués les traitements internes à un objet. Nous devons juste vérifier que les traitements externes envoient les bonnes informations. 

Tester uniquement l'interface offre une **plus grande flexibilité** à la fois dans les tests et dans l'implémentation des interfaces. On peut changer le code sans avoir à modifier les tests. On ne cherche pas à savoir comment sont traitées les données en interne du moment que l'information renvoyée est conforme aux attentes de l'utilisateur.

Un plan de test unitaire relativement simple est de définir : 

* la partie de code à tester,
* les inputs à tester,
* les outputs à tester.

En général il y a autant de tests que de possibilités de sortie que fournira la méthode publique.

## Organisation des tests

Les tests doivent être séparés de l'implémentation de notre application. Il est donc nécessaire de créer un **répertoire tests** dans l'arborescence de votre projet.

## Exemples de test unitaire

* Prenons la classe FileRepo et posons nous les questions:  

	1. Que pouvons-nous tester ? Nous pouvons par exemple vérifier que le fichier CSV que nous obtenons est conforme à nos attente. 
	1. Comment faire cela ? C'est toute la difficulté....

* Un exemple très complet avec le module **unittest** de Python : [vidéo](https://www.youtube.com/watch?v=apgReCCAQr4).

# Tests et couverture de code

La couverture du code est une mesure (métrique) du nombre de lignes de votre code exécutées pendant l'exécution des tests automatisés.

Parler du taux de couverture implique de comprendre cet indicateur, ce qui n'est pas si simple... On distingue plusieurs types de taux de couverture, en voici quelques-uns :

* La couverture de lignes : les tests sont lancés, chaque ligne sur laquelle un test passe est considérée comme couverte ;
* La couverture de branches : les tests sont lancés, chaque branche du code dans laquelle un test passe est considérée comme couverte. Par exemple, un **if(valeurA and valeurB)** contient 4 branches 
	* false and false, 
	* false and true, 
	* true and false,
	* true and true. 
	
... mais la première et la seconde sont identiques en terme d'exécution ;
* La couverture de mutation : Un changement est fait dans le code (changement d'une condition, d'une valeur, …) et on lance les tests passants dans le code modifié. Si les tests passent encore, alors le cas n'est pas couvert.

Quand on parle de taux de couverture, on parle des deux premiers types : dans quelles parties de mon code passent mes tests ?

Bien qu'étant un indicateur intéressant, le taux de couverture ne permet pas de mesurer :
* La pertinence des tests : il est tout à fait possible de faire des tests qui n'ont aucune valeur,
* La qualité des tests : de manière générale, le taux de couverture ne donne aucune indication sur la qualité des tests qui ont été écrits.
