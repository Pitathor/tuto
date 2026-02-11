# Tutoriel d'introduction au radar et traitement du signal

Tu as soif de connaissances et tu veux apprendres les bases du radar ? Alors n'attends plus et plonges toi dans ce cours. Pour cela il te suffit d'un ordinateur avec un environnement Python et des quelques lignes de commandes ci-dessous.

## Installation

D'abord télécharges le fichier zip contenant le cours et crées un dossier sur ton bureau pour accueillir son contenu. Afin d'avoir la totalité du contenu, récupéres le dossier **Images** sur le NAS de l'unité, que tu placeras ensuite dans le dossier **Chapitres** du cours.

### Environnement Python

Pour pouvoir faire fonctionner correctement le tutoriel, quelques packages sont nécessaires. Ouvres une instance de commande python et rentres les commandes suivantes :

```sh
# On se place dans le bon répertoire de travail. Copies le chemin du dossier contenant le cours sur ton bureau et rentres la commande suivante
cd "le_dossier_où_se_trouve_le_Book"
# Installes les packages
pip install -r requirements.txt
```

### Création du Jupyter book

Une fois l'installation complétée, tu devrais pouvoir ouvrir le tutoriel avec : 

```sh
# Ouvre le jupyter book 
jupyter book start
```

### Compilation en temps réel

Tu as la possibilité de compiler les pages du cours en temps réel avec le bouton **ON** U+23FC. Pour cela il te faut créer une instance jupyter lab avec les commandes suivantes :

```sh
# Rebelotte, places toi dans le bon répertoire.
cd "path"
# Ouvre jupyter lab qui sera connecté à ton jupyter book 
jupyter lab --NotebookApp.token=tuto --NotebookApp.allow_origin='http://localhost:3000'
```

Une fois ceci fait, tu verras apparaître en haut de chaque page un bouton ON qui te permettra d'activer la compilation des cellules codes de la page. Tu peux même par la suite, ouvrir chaque page dans jupyter lab pour les modifier. 





