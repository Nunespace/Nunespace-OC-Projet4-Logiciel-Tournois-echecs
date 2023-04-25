# Logiciel Centre échecs
***
_Outil de gestion des tournois d'échecs _




## Fonctionnalités de l'application

Cette application est destinée au club d'échecs local pour l'aider à organiser ses tournois d'échecs.

Elle permet de créer un tournoi et de générer les paires (matchs) selon les scores des joueurs et sans créer de paire identique. Les résultats des tournois sont sauvegardés et les rapports suivants peuvent être affichés dans le programme :
- liste des joueurs,
- liste des tournois,
- nom et dates d'un tournoi donné,
- liste des joueurs du tournoi par odre aplhabétique,
- liste de tous les tours du tournoi et de tous les matchs du tour.

Les données sont enregistrés dans 2 fichiers json : * *tournaments_data.json* * pour les données des tournois, et * *players_data.json* * pour les joueurs. 



## Prérequis

**Python** doit être préalablement installé.

Si vous travaillez dans un environnement Linux ou MacOS : Python est en principe déjà installé. Pour le vérifier, ouvrez votre terminal et tapez : `python --version` ou `python3 --version`


Si Python n'est pas installé, vous pouvez le télécharger à l'adresse suivante : 
[Télécharger Python3](https://www.python.org/downloads)

Vous aurez aussi besoin de l'installateur de paquets de Python **pip** qui est compris par défaut si vous disposez d'une version de Python >= 3.4. Vous pouvez vérifier qu'il est disponible via votre ligne de commande, en saisissant : `pip --version`



## Installation

1. Ouvrez le terminal et tapez :


```
$ git clone https://github.com/Nunespace/Nunespace-OC-Projet4-Logiciel-Tournois-echecs.git
```


2. Placez-vous dans le répertoire où se trouve le projet :

```
$ CD Projet
ou
$ CD chemin .../Projet
```


3. Créez votre environnement virtuel : 

```
python3 -m venv env 
```

ou[^1]

```
python -m venv env 
```

> sous mac ou Linux :

```
$ source env/bin/activate  
```

> sous Windows, la commande sera :

```
$ env\Scripts\activate.bat
```
Si vous utilisez PowerShell, il faut exécuter la commande sans  *.bat* :
```
$ env/Scripts/activate
```


5. Puis installez les paquets Python répertoriés dans le fichier requirements.txt :

```
$ pip install -r requirements.txt
```


6. Enfin, **lancez le programme** en tapant : 

```
$ python3 main.py
ou
$ python main.py
```



[^1]: selon la version de Python installée sur votre PC.



## Génération d'un nouveau fichier flake8-html.  

1. Installer Flake8 

```
$ pip install flake8-html
```

2. Exécuter Flake8 

```
$ flake8 --format=html --htmldir=flake-report
```

Le rapport *flake-report* est enregistré automatiquement dans le répertoire du projet.