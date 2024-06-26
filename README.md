# Air France Test Bench Management Application AI

## Description

Ce projet a été réalisé pour Air France dans le cadre d'un workshop. L'objectif est de développer une application pour les ingénieurs banc de test permettant de gérer des fichiers techniques sur les instruments, d'extraire automatiquement les informations pertinentes, et d'interagir avec un chatbot basé sur l'IA pour obtenir des informations sur les documents ou effectuer des recherches sur Internet.

## Fonctionnalités

- **Téléchargement et gestion de fichiers techniques** : Les utilisateurs peuvent télécharger des fichiers relatifs aux instruments techniques.
- **Extraction automatique des informations** : Utilisation de l'intelligence artificielle pour extraire et organiser les données techniques des documents téléchargés.
- **Chatbot interactif** : Permet aux utilisateurs de poser des questions sur les documents techniques ou de rechercher des informations sur Internet.

## Prérequis

- Docker
- Docker Compose
- key API https://tavily.com/
- key API OpenAI ou Azure OpenAI

## Installation

Clonez le dépôt du projet :

```sh
git clone https://github.com/MDS-WORKSHOP/CBA-PROJECT.git
cd CBA-PROJECT 
```

Créez un fichier .env à la racine du projet et configurez les variables d'environnement nécessaires (exemple ci-dessous) :

```sh
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=cba_database
MYSQL_USER=admin
MYSQL_PASSWORD=password
PMA_HOST=db
DJANGO_CORS_ALLOWED_ORIGINS=http://localhost:5173
DJANGO_ALLOWED_HOSTS=*
```
### Utilisation de Docker
Construisez et démarrez les conteneurs Docker :

```sh
docker-compose up --build
```

Une fois les conteneurs en cours d'exécution, ouvrez un nouveau terminal et exécutez les migrations de la base de données :


```sh
docker-compose exec server python manage.py makemigrations
docker-compose exec server python manage.py migrate
```

### Création d'un utilisateur avec une commande personnalisée

Vous pouvez créer un utilisateur en utilisant la commande personnalisée create_user. Par exemple :
```sh
docker-compose exec server python manage.py create_custom_user johndoe johndoe@example.com password123 --first_name=John --last_name=Doe --profile=CD --role=admin --site=CDG
```

## Accès à l'application

L'application sera accessible via http://localhost:5173.


## Auteurs

- Elton DOISY - Développeur full stack
- Lucas MALATCHOUMY - Développeur full stack
- Aminata DIARRA - UX/UI Design
- Chloë JAMES - Direction Artistique
