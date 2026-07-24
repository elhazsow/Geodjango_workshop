# GeoDjango Workshop – Guide d'utilisation

Ce dépôt permet de découvrir les bases de GeoDjango à travers une petite application web de cartographie. Il a été conçu pour montrer comment :

- créer une application web avec Django,
- stocker des données géographiques dans une base PostGIS,
- afficher des couches vectorielles sur une carte Leaflet,
- saisir un point géographique à partir d’un formulaire,
- charger des données administratives et raster.

---

## 1. Objectifs pédagogiques

À l’issue de ce TP, l’étudiant doit être capable de :

1. installer un environnement Python pour GeoDjango,
2. configurer une base de données PostGIS,
3. lancer une application Django,
4. charger des données géographiques dans la base,
5. visualiser des objets spatiaux sur une carte web.

---

## 2. Prérequis

Avant de commencer, il faut avoir installé sur votre machine :

- Python 3.10 ou 3.11,
- PostgreSQL avec l’extension PostGIS,
- un environnement virtuel,
- Git,
- un éditeur de code comme Visual Studio Code.

Pour GeoDjango sur Windows, il est aussi nécessaire d’avoir installé les bibliothèques GDAL/GEOS, généralement via OSGeo4W ou une installation équivalente.

---

## 3. Cloner le dépôt

Ouvrez un terminal et exécutez :

```bash
git clone https://github.com/elhazsow/Geodjango_workshop.git
cd Geodjango_workshop
```

Si vous travaillez déjà dans ce dossier, passez directement à l’étape suivante.

---

## 4. Créer et activer l’environnement virtuel

Sous Windows, vous pouvez utiliser l’environnement déjà fourni dans le projet, ou en créer un nouveau :

```bash
python -m venv mon_env
mon_env\Scripts\activate
```

Vérifiez que l’environnement est bien activé. Le prompt doit afficher le nom de l’environnement.

Ensuite, installez les dépendances :

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 5. Configurer la base de données PostGIS

### 5.1 Créer une base de données

Dans PostgreSQL, créez une base de données, par exemple :

```sql
CREATE DATABASE geodjango_workshop;
```

Puis activez l’extension PostGIS :

```sql
\c geodjango_workshop
CREATE EXTENSION IF NOT EXISTS postgis;
```

### 5.2 Créer le fichier de configuration

À la racine du projet, créez un fichier nommé `.env` avec le contenu suivant :

```env
DEBUG=True 
DB_NAME=nom_de_ta_BD
DB_USER=user_de_ta_BD
DB_PASSWORD=votre_mot_de_passe
DB_HOST=localhost
DB_PORT=5432
```

Adaptez les valeurs selon votre installation PostgreSQL.

> Remarque : le projet lit automatiquement ce fichier grâce à la configuration Django dans le dossier websig.

---

## 6. Vérifier la configuration GeoDjango

Le fichier de configuration principal se trouve dans :

- websig/settings.py

Il contient notamment les chemins vers les bibliothèques GDAL et GEOS. Sur Windows, il peut être nécessaire de vérifier ces lignes :

```python
GEOS_LIBRARY_PATH = 'C:\\OSGeo4W\\bin\\geos_c.dll'
GDAL_LIBRARY_PATH = 'C:\\OSGeo4W\\bin\\gdal309.dll'
```

Si votre installation OSGeo4W utilise un autre chemin, adaptez-le.

Ajoute les variables d'environnement pour GDAL et PROJ:
```
GDAL_DATA="C:\OSGeo4W\apps\gdal\share\gdal"
PROJ_LIB="C:\OSGeo4W\share\proj"
```
---

## 7. Appliquer les migrations

Avant de lancer l’application, il faut créer les tables de la base :

```bash
python manage.py migrate
```

Si tout se passe bien, Django crée les tables nécessaires pour les modèles géographiques.

---

## 8. Charger les données de base

Le projet contient des scripts d’import de données dans le dossier :

- sig_app/scripts

### 8.1 Charger les limites administratives

Ce script importe les couches de régions, départements et communes à partir des shapefiles fournis :

```bash
python manage.py runscript load_admin_limit
```

Cette opération peut prendre quelques secondes selon la taille des données.

### 8.2 Charger un raster (optionnel)

Le script de chargement de raster est également disponible(nécessite l'extension *postgis_raster*). Il est toutefois dépendant d’un fichier local. Il faut adapter le chemin du fichier TIFF dans le script avant de l’exécuter :

```bash
python manage.py runscript load_raster
```

---

## 9. Lancer l’application

Pour démarrer le serveur de développement :

```bash
python manage.py runserver
```

Ensuite, ouvrez votre navigateur à l’adresse :

```text
http://127.0.0.1:8000/
```

Vous devriez voir la carte interactive de l’application.

![App screen shot](captures/Home.PNG?raw=true)

---

## 10. Utiliser l’application

### 10.1 Voir la carte

La page d’accueil affiche une carte avec des données géographiques chargées depuis la base.

### 10.2 Ajouter un point géographique

Une route dédiée permet de saisir un point sur une carte Leaflet :

```text
http://127.0.0.1:8000/create_point
```

Cette page permet de remplir :

- un nom,
- une description,
- un point géographique positionné sur la carte.

  ![App screen shot](captures/Formulaire.PNG?raw=true)

### 10.3 Explorer les données avec Django ORM

Vous pouvez aussi tester les requêtes spatiales depuis la ligne de commande :

```bash
python manage.py shell
```

Exemples :
Je vous connseille à jouer avec les requêtes et relations spatiales entre géomètries

```python
from sig_app.models import Region, Commune

print(Region.objects.count())
print(Commune.objects.count())
```

#### Challenge 1 – localisation simple
Écrire une requête pour trouver la commune qui contient un point donné.

#### Challenge 2 – relation entre couches
Trouver tous les départements appartenant à une région précise.

#### Challenge 3 – comptage spatial
Compter le nombre de communes par région et afficher le résultat.

#### Challenge 4 – distance
Identifier toutes les communes situées à moins de 10 km d’un point de référence.

#### Challenge 5 – intersection
Trouver les objets géographiques qui intersectent une zone tampon autour d’un point.

---

## 11. Structure du projet

Voici les principaux éléments du dépôt :

- sig_app/models.py : définition des modèles géographiques,
- sig_app/views.py : vues Django qui affichent la carte et le formulaire,
- sig_app/forms.py : formulaire de saisie de points,
- sig_app/scripts : scripts d’import de données,
- websig/settings.py : configuration du projet et de la base de données,
- templates/ : pages HTML utilisées par l’application.

---

## 12. Résolution des problèmes courants

### Problème : erreur liée à GDAL ou GEOS

Vérifiez que les chemins dans settings.py correspondent bien à votre installation OSGeo4W.

### Problème : impossible de se connecter à PostgreSQL

Contrôlez :

- le nom de la base,
- l’utilisateur,
- le mot de passe,
- le port 5432,
- l’état du service PostgreSQL.

### Problème : la carte ne s’affiche pas

Vérifiez que les données administratives ont bien été chargées avec le script d’import.

### Problème : la page de formulaire ne fonctionne pas

Vérifiez que les migrations ont bien été appliquées et que la base est accessible.

---

## 13. Conseils pour bien avancer

Pour bien progresser dans ce TP :

1. lisez les messages d’erreur Django avec attention,
2. testez chaque étape séparément,
3. gardez les commandes utiles dans un carnet de bord,
4. comparez ce que vous voyez sur la carte avec les données stockées en base.

---

## 14. Pousser le travail sur son propre dépôt Git

À la fin du TP, chaque étudiant peut sauvegarder son travail sur un dépôt Git personnel.

### Étapes à suivre

1. Créer un dépôt GitHub, GitLab ou autre plateforme de votre choix.
2. Initialiser un dépôt local si ce n’est pas déjà fait :

```bash
git init
git add .
git commit -m "Première version du TP GeoDjango"
```

3. Ajouter l’URL de votre dépôt distant :

```bash
git remote add origin https://github.com/votre_nom/votre_repo.git
```

4. Pousser le code vers la branche principale :

```bash
git branch -M main
git push -u origin main
```

### Conseils

- ajoutez un fichier `.gitignore` pour ne pas versionner les fichiers temporaires, les environnements virtuels ou les secrets,
- faites des commits réguliers pendant le TP,
- utilisez des messages de commit clairs, par exemple : `ajout du formulaire de saisie`, `chargement des données administratives`.

---

## 15. Conclusion

Ce projet est un bon point de départ pour apprendre GeoDjango de manière pratique. Il permet de découvrir la chaîne complète :

- collecte de données,
- stockage dans PostGIS,
- exploitation avec Django,
- visualisation sur une carte web.

Bon travail !
