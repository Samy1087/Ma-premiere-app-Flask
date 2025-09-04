Documentation du projet : Ma Première Application Flask

1️⃣ Introduction

Ce projet est une application web simple développée avec Flask en Python 3.12.3.

Il permet de :

- Créer des routes dynamiques

- Interagir avec l’utilisateur via l’URL

- Effectuer des calculs simples (somme de deux nombres)


Objectif pédagogique : pratiquer le développement web en Python, la création de routes, la gestion des entrées utilisateur et la structuration de projet.


---

2️⃣ Structure du projet

Ma-premiere-app-Flask/
│
├── .gitignore              # Ignorer venv et fichiers temporaires
├── app.py                  # Fichier principal de l'application Flask
├── docs/                   # Documentation officielle
├── README.md               # Présentation rapide du projet
├── requirements.txt        # Dépendances Python
├── templates/              # Fichiers HTML pour l'interface
├── venv/                   # Environnement virtuel (ne pas versionner)
└──__pycache__              # Dossier contenant des fichiers temporaire 


---

3️⃣ Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/Samy1087/Ma-premiere-app-Flask.git
```
```bash
cd Ma-premiere-app-Flask
```

2. Créer un environnement virtuel :
```bash
python3.12 -m venv venv
```

3. Activer l’environnement :
```bash
source venv/bin/activate   # Linux/macOS
```
```bash
venv\Scripts\activate      # Windows
```

4. Installer les dépendances :
```bash
pip install -r requirements.txt
```
---

4️⃣ Utilisation détaillée

a) Route message personnalisé

URL : /prenom

Exemple : http://127.0.0.1:5000/Samy

Fonctionnalité : affiche "Bienvenue Samy sur mon application Flask !"


b) Route calculatrice

URL : /Nombre1/Nombre2

Exemple : http://127.0.0.1:5000/3/5

Fonctionnalité : affiche "La somme de 3 et 5 est 8"

c) Route date et heure

URL : /date_heure

Exemple : http://127.0.0.1:5000/date_heure

Fonctionnalité : affiche l'heure actuelle

d) Route principal

URL : /

Exemple : http://127.0.0.1:5000/

Fonctionnalité : affiche la page d'accueil du système 

---

5️⃣ Architecture du code

app.py : contient toutes les routes Flask

Routes principales :

/prenom : route pour le message 

/<nombre1>/<nombre2> : route pour la somme


Chaque route est gérée par une fonction distincte pour plus de clarté.


💡 Astuce : chaque fonction peut être étendue pour ajouter de nouvelles fonctionnalités (ex : soustraction, multiplication, validation des entrées).


---

6️⃣ Améliorations futures

Ajouter une interface HTML/CSS pour rendre l’application interactive

Implémenter la gestion des erreurs (ex : entrées non numériques)

Ajouter des tests unitaires pour chaque route

Stocker les résultats ou historiques des utilisateurs dans une base de données



---

7️⃣ Compétences développées

Création et gestion de routes Flask

Manipulation des entrées utilisateur

Installation et gestion d’un environnement virtuel Python

Documentation et structuration de projet





