# Blog API avec Django et Django REST Framework

## Description

Ce projet est une API REST pour un blog, développée avec Django et Django REST Framework. Il fournit des fonctionnalités de base pour la gestion des articles de blog, des commentaires et des utilisateurs.

## Fonctionnalités

- Création, lecture, mise à jour et suppression d'articles de blog
- Gestion des commentaires sur les articles
- Authentification et gestion des utilisateurs
- Paginisation et filtrage des articles

## Prérequis

- Python 3.x
- Django 3.x ou supérieur
- Django REST Framework

## Installation

1. Clonez le repository

```bash
git clone https://github.com/votreutilisateur/votreprojet.git
cd votreprojet
```

2. Créez un environnement virtuel et activez-le

```bash
python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
```

3. Installez les dépendances

```bash
pip install -r requirements.txt
```

4. Appliquez les migrations de la base de données

```bash
python manage.py migrate
```

5. Créez un superutilisateur pour accéder à l'admin Django

```bash
python manage.py createsuperuser
```

6. Lancez le serveur de développement

```bash
python manage.py runserver
```

## Endpoints de l'API

- **/api/auth/login/**: Authentification utilisateur et obtention du token JWT
- **/api/auth/register/**: Inscription d'un nouvel utilisateur
- **/api/posts/**: Liste et création des articles de blog
- **/api/posts/{id}/**: Détails, mise à jour et suppression d'un article spécifique
- **/api/posts/{id}/comments/**: Liste et création des commentaires sur un article
- **/api/comments/{id}/**: Détails, mise à jour et suppression d'un commentaire spécifique

## Utilisation

### Authentification

Pour accéder aux endpoints protégés, vous devez inclure le token JWT dans l'en-tête de la requête. Après avoir obtenu le token via l'endpoint de login, ajoutez l'en-tête suivant à vos requêtes :

```
Authorization: Bearer <votre_token_jwt>
```

### Exemples de requêtes

- **Inscription**

```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "nouvelutilisateur",
    "password": "votremotdepasse"
}
```

- **Authentification**

```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "nouvelutilisateur",
    "password": "votremotdepasse"
}
```

- **Création d'un article**

```http
POST /api/posts/
Authorization: Bearer <votre_token_jwt>
Content-Type: application/json

{
    "title": "Mon premier article",
    "content": "Ceci est le contenu de mon premier article."
}
```

- **Liste des articles**

```http
GET /api/posts/
```

## Tests

Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
python manage.py test
```

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une pull request pour toute amélioration ou fonctionnalité supplémentaire que vous souhaitez ajouter.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

## Auteurs

- [Votre Nom](https://github.com/DestinBir)

---

N'oubliez pas de remplacer les informations spécifiques par celles correspondant à votre projet. Ce modèle de README fournit une vue d'ensemble claire et concise de votre projet de blog API avec Django et Django REST Framework.
