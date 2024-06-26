# Air France Test Bench Management Application AI

## Description

Ce projet a été réalisé pour Air France dans le cadre d'un workshop. L'objectif est de développer une application pour les ingénieurs banc de test permettant de gérer des fichiers techniques sur les instruments, d'extraire automatiquement les informations pertinentes, et d'interagir avec un chatbot basé sur l'IA pour obtenir des informations sur les documents ou effectuer des recherches sur Internet.

## Fonctionnalités

- **Téléchargement et gestion de fichiers techniques** : Les utilisateurs peuvent télécharger des fichiers relatifs aux instruments techniques.
- **Extraction automatique des informations** : Utilisation de l'intelligence artificielle pour extraire et organiser les données techniques des documents téléchargés.
- **Chatbot interactif** : Permet aux utilisateurs de poser des questions sur les documents techniques ou de rechercher des informations sur Internet.

## Prérequis

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- key API https://tavily.com/
- key API OpenAI ou Azure OpenAI

## Flexibilité des Modèles de Langage

L'application est conçue pour fonctionner avec différents modèles de langage (LLM) tels que Mistral, Llama 3, OpenAI, et d'autres. Étant donné que l'environnement de production ne comporte pas de carte graphique (GPU) nécessaire pour la gestion locale des LLM, le choix a été fait d'utiliser des API externes. Cela permet d'intégrer facilement des LLM via OpenAI ou Azure OpenAI. Pour utiliser l'application, une clé API OpenAI ou Azure OpenAI est nécessaire. Cependant, l'architecture de l'application permet de modifier facilement la configuration pour utiliser d'autres APIs, comme celles de Mistral ou Groq.

## Paiement Unique pour OpenAI

Pour répondre à la problématique de ne pas pouvoir prendre d'abonnement, il est possible de configurer un paiement unique sur OpenAI. Cela permet d'avoir accès à l'API sans besoin d'abonnement mensuel. Une fois que le crédit est épuisé, il suffit de recharger le montant souhaité pour continuer à utiliser l'API jusqu'à épuisement du nouveau crédit. Cette flexibilité permet une meilleure gestion des coûts et une utilisation adaptée aux besoins.

## Utilisation d'une IA 100% Locale
Pour ceux qui souhaitent utiliser une IA 100% locale, il est possible de configurer un serveur avec une ou deux cartes graphiques de dernière génération, comme la GeForce RTX 3090 Founders Edition. Voici les étapes à suivre :

1. **Monter un Serveur** :
    - Assurez-vous que votre serveur est équipé d'une ou deux cartes graphiques GeForce RTX 3090 Founders Edition par exemple.

2. **Télécharger le Modèle Open Source** :
    - Téléchargez le modèle Llama 3 depuis Hugging Face https://huggingface.co/ .

3. **Modifier le Code** :
    - Modifiez le code de l'application pour utiliser `llama.cpp` avec le modèle téléchargé https://python.langchain.com/v0.2/docs/integrations/llms/llamacpp/.
    - Assurez-vous que le code est configuré pour exécuter le modèle en local.

4. **Exécuter en Local** :
    - Démarrez l'application en utilisant les ressources GPU pour exécuter le modèle de langage.
    - Évitez d'utiliser le CPU pour exécuter le modèle, car cela pourrait ne pas fournir suffisamment de puissance et risque d'endommager le matériel à cause de la chaleur produite par les calculs intensifs.

## Installation

Clonez le dépôt du projet :

```sh
git clone https://github.com/MDS-WORKSHOP/CBA-PROJECT.git
cd CBA-PROJECT 
```

Créez un fichier .env à la racine du projet et configurez les variables d'environnement nécessaires (exemple ci-dessous) :

### Configuration MySQL

Ces variables configurent la connexion à la base de données MySQL.vous n'avez pas besoin de modifier le PMA_HOST

```sh
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=cba_database
MYSQL_USER=admin
MYSQL_PASSWORD=password
PMA_HOST=db
```

### Configuration Django

Ces variables configurent les paramètres de Django. En général, vous n'avez pas besoin de les modifier.

```sh
FRONTEND_URL=http://localhost:5173
DJANGO_CORS_ALLOWED_ORIGINS=http://localhost:5173
DJANGO_ALLOWED_HOSTS=*
DJANGO_DEBUG=true
ENVIROMENT=development
```

### Configuration Email 

Ces variables configurent le serveur mail (exemple).

```sh
EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_PORT=2525
EMAIL_HOST_USER=user-exemple
EMAIL_HOST_PASSWORD=f69aaapplf
EMAIL_USE_SSL=False
EMAIL_USE_TLS=True
```
### Configuration des Clés API

Pour OpenAI :
```sh
OPENAI_API_KEY=clef-api-exemple
```
Pour Azure OpenAI :
```sh
PROXY_URL=""
AZURE_OPENAI_DEPLOYMENT_NAME=""
AZURE_OPENAI_API_BASE=""
AZURE_OPENAI_API_VERSION=""
AZURE_OPENAI_API_KEY=""
```
Pour Tavily :
```sh
TAVILY_API_KEY=example-key
```
Note : Vous avez droit à 1,000 API calls par mois avec Tavily.

### Utilisation de Docker
Construisez et démarrez les conteneurs Docker :

```sh
docker-compose build

docker-compose up -d
```

Une fois les conteneurs en cours d'exécution, ouvrez un nouveau terminal et exécutez les migrations de la base de données :


```sh
docker-compose exec server python manage.py makemigrations

docker-compose exec server python manage.py migrate
```

### Création d'un utilisateur avec une commande personnalisée

Vous pouvez créer un utilisateur en utilisant la commande personnalisée create_user. Par exemple :
```sh
docker-compose exec server python manage.py create_user johndoe johndoe@example.com password123 --first_name=John --last_name=Doe --profile=CD --role=admin --site=CDG
```

## Accès à l'application

L'application sera accessible via http://localhost:5173.


## Auteurs

- Elton DOISY - Développeur full stack
- Lucas MALATCHOUMY - Développeur full stack
- Aminata DIARRA - UX/UI Design
- Chloë JAMES - Direction Artistique
