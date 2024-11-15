---
# You can also start simply with 'default'
theme: seriph
addons:
  - tldraw
  - slidev-addon-excalidraw
# some information about your slides (markdown enabled)
title: Projet Openclassrooms 6
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# take snapshot for each slide in the overview
overviewSnapshots: true
hideInToc: true
---

# Projet 6 Openclassrooms

Classifiez automatiquement des biens de consommation

<div class="abs-br m-6 flex gap-2">
  <a href="https://openclassrooms.com/fr/projects/1502/mission---segmentez-des-clients-d'un-site-e-commerce" target="_blank" alt="OpenClassrooms" title="OpenClassrooms"
     class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <img src="./assets/Logo_OpenClassrooms.png" alt="OpenClassrooms Logo" style="width: 32px; height: 32px;" />
  </a>
  <a href="https://github.com/dimitri-feniou/openclassrooms-projet6-classification-conso" target="_blank" alt="GitHub" title="Open in GitHub"
     class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->
---
transition: fade-out
layout: cover
---
# _I. Présentation du contexte projet et du jeu de données_




---
transition: fade-out
---

# Contexte Projet

- L'entreprise **Place de marché** souhaite lancer une markeplace e-commerce
- **Problématique:** actuellement l'attribution de la catégorie du produit est effectuée manuellement par le vendeur, et est donc peu fiable.

<div class="flex items-center gap-4">
  <div class="encart-dark flex-1">
  <strong>Notre mission :</strong><br>
  <strong>Faire une étude de faisabilité d'un moteur de classification pour l'automatisation de l'attribution de la catégorie de l'article</strong> en fonction de la description et de l'image de l'article.
</div>

  <img src="https://user.oc-static.com/upload/2023/03/30/1680170799854_Data%20Scientist-P6-01%20%281%29.png" alt="Illustration du projet" class="w-1/2 h-" />
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://openclassrooms.com/fr/projects/1502/mission---segmentez-des-clients-d'un-site-e-commerce" target="_blank" alt="OpenClassrooms" title="OpenClassrooms"
     class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <img src="./assets/Logo_OpenClassrooms.png" alt="OpenClassrooms Logo" style="width: 32px; height: 32px;" />
  </a>
  <a href="https://github.com/dimitri-feniou/openclassrooms-projet6-classification-conso" target="_blank" alt="GitHub" title="Open in GitHub"
     class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<style>
h1 {
  background-color: #2B90B6;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
.encart-dark {
  border: 2px solid #ffffff; /* Bordure blanche pour contraster avec le fond sombre */
  padding: 15px;
  border-radius: 8px;
  font-weight: bold;
  background-color: #333333; /* Fond gris foncé pour s'harmoniser avec le mode sombre */
  color: #ffffff; /* Texte blanc pour une meilleure lisibilité */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* Ombre portée pour donner de la profondeur */
  margin: 20px 0; /* Espacement vertical pour aérer le contenu */
}
</style>

<!--
Here is another comment.
-->

---
transition: fade-out
zoom: 0.5
---

# Présentation du jeu de données 

<div class="encart-dark flex-1">
  <strong>Fichier CSV</strong>
  <ul>
    <li><strong>1050 lignes</strong> contenant des articles.</li>
    <li><strong>15 colonnes</strong> fournissant des informations sur chaque produit :</li>
    <ul>
      <li>Identifiant unique du produit</li>
      <li><strong>Nom du produit</strong></li>
      <li>Marque du produit</li>
      <li>URL du produit</li>
      <li><strong>Arborescence de la catégorie du produit (7 niveaux)</strong></li>
      <li>Prix</li>
      <li><strong>Description du produit</strong></li>
      <li><strong>Nom de l'image</strong></li>
    </ul>
  </ul>
  <p><strong>Nettoyage des données :</strong> Très peu de données manquantes, aucune absence dans les champs utilisés.</p>
</div>
<div class="encart-dark flex-1">
  <strong>Dossier d'images</strong>
  <ul>
    <li>Vérification de la corruption et du format des images</li>
  </ul>
   <div class="flex items-center justify-center mt-4">
   <strong>1050 image pour chaque produit</strong>
  </div>
  <div class="flex items-center justify-center mt-4">
    <img src="./assets/capture_article.png" alt="Illustration du projet" class="w-12 h-auto" />
  </div>
</div>


<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
}

.flex {
  display: flex;
}

.flex-1 {
  flex: 1;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.mt-4 {
  margin-top: 1rem;
}

.w-12 {
  width: 80%;
}

.h-auto {
  height: auto;
}
</style>

---
transition: fade-out
layout: cover
---
# _II.Présentation des approches de modélisation de classification et résultats_

---
transition: fade-out
---

# Approche de modélisation 

<div class="flex items-left justify-left mt-4">
    <img src="/public/schema_classification.png" alt="Illustration du projet" style="width: 90%; max-width: 450px;" />
</div>

<style>
h1 {
  background-color: #2B90B6;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
.encart-dark {
  border: 2px solid #ffffff; /* Bordure blanche pour contraster avec le fond sombre */
  padding: 15px;
  border-radius: 8px;
  font-weight: bold;
  background-color: #333333; /* Fond gris foncé pour s'harmoniser avec le mode sombre */
  color: #ffffff; /* Texte blanc pour une meilleure lisibilité */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* Ombre portée pour donner de la profondeur */
  margin: 20px 0; /* Espacement vertical pour aérer le contenu */
}
</style>

---
transition: fade-out
---
# Approche de modélisation générale

<div class="flex items-left justify-left mt-4">
    <img src="/public/schema_approche_gen.png" alt="Illustration du projet" style="width: 100%;" />
</div>

<style>
h1 {
  background-color: #2B90B6;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
.encart-dark {
  border: 2px solid #ffffff; /* Bordure blanche pour contraster avec le fond sombre */
  padding: 15px;
  border-radius: 8px;
  font-weight: bold;
  background-color: #333333; /* Fond gris foncé pour s'harmoniser avec le mode sombre */
  color: #ffffff; /* Texte blanc pour une meilleure lisibilité */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5); /* Ombre portée pour donner de la profondeur */
  margin: 20px 0; /* Espacement vertical pour aérer le contenu */
}
</style>

---
transition: fade-out
layout: cover
---
# _III.Présentation des approches de modélisation de classification du Texte_

---
transition: fade-out
---

# Traitement des données textuelles
Nettoyage des données textuelles

- Normalisation du texte sur le texte `product_name` et `description`:

1. Conversion du texte en minuscules et suppression de la ponctuation 

2. Tokenisation : Division du texte par mots

3.  Suppression des stopwords (articles,pronoms...)

4. Ajout du texte `product_name` et `description` dans la même phrase 




<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
}

.flex {
  display: flex;
}

.flex-1 {
  flex: 1;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.mt-4 {
  margin-top: 1rem;
}

.w-12 {
  width: 80%;
}

.h-auto {
  height: auto;
}
</style>

---
transition: fade-out
zoom: 0.7
---

# Approche Bag of words : comptage simple

- Représentation de chaque document en **fonction de la fréquence des mots** (count vectorizer)
- Création d'un vecteur pour chaque document rassemblé dans une **matrice de comptage**


<div class="flex items-left justify-left mt-4">
  <div style="display: flex; gap: 20px;">
    <img src="/public/tnse_cont_vec_category.png" alt="Illustration du projet" style="width: 50%;" />
    <img src="/public/tnse_cont_vec_cluster.png" alt="Illustration du projet" style="width: 50%;" />
  </div>
</div>
<div class="encart-dark flex-1 encart-centered">
  Score ARI : 0.3347 Séparation partielle des catégories
</div>

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centrer les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
transition: fade-out
zoom: 0.6
---

# Approche Bag of words : TF-IDF (Term Frequency-Inverse Document Frequency)

- TF (Term Frequency) : Fréquence d'un mot dans le document
- IDF (Inverse Document Frequency) : Réduit l'importance des mots communs qui apparaissent dans de nombreux documents.


<div class="flex items-left justify-left mt-4">
  <div style="display: flex; gap: 20px;">
    <img src="/tnse_tfidf_category.png" alt="Illustration du projet" style="width: 50%;" />
    <img src="/tnse_tfidf_cluster.png" alt="Illustration du projet" style="width: 50%;" />
  </div>
</div>
<div class="encart-dark flex-1 encart-centered">
  Score ARI : 0.4092 Assez bonne séparation des catégories
</div>

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centrer les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
transition: fade-out
zoom: 0.8
---

# Approche Bag of words : Word2Vec

- Word2Vec transforme chaque mot d'un texte en un vecteur de nombres, capturant des **caractéristiques sémantiques**.
- **similarité sémantique** : Les mots ayant des contextes similaires se retrouvent proches dans l'espace vectoriel



<div class="flex items-left justify-left mt-4">
  <div style="display: flex; gap: 20px;">
    <img src="/tnse_word2vec_category.png" alt="Illustration du projet" style="width: 50%; height: auto; max-height: 350px;" />
    <img src="/tnse_word2vec_cluster.png" alt="Illustration du projet" style="width: 50%; height: auto; max-height: 350px;" />
  </div>
</div>
<div class="encart-dark flex-1 encart-centered">
  Score ARI : 0.4364 Assez bonne séparation des catégories
</div>

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centrer les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
transition: fade-out
zoom: 0.8
---

# Approche Bag of words : BERT  (Bidirectional Encoder Representations from Transformers)

- Réseau de neuronne pré-entrainé basé sur l'architecture transformers
- **Pré-entraînement bidirectionnel** : BERT apprend le contexte des mots à la fois avant et après chaque mot.Ce qui permet de mieux capture le contexte et sens des phrase.



<div class="flex items-left justify-left mt-4">
  <div style="display: flex; gap: 20px;">
    <img src="/tnse_bert_category.png" alt="Illustration du projet" style="width: 50%; height: auto; max-height: 350px;" />
    <img src="/tnse_bert_cluster.png" alt="Illustration du projet" style="width: 50%; height: auto; max-height: 350px;" />
  </div>
</div>
<div class="encart-dark flex-1 encart-centered">
  Score ARI : 0.3251 Séparation partielle des catégories
</div>

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centrer les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
transition: fade-out
zoom: 0.8
---

# Approche Bag of words : USE  (Universal Sentence Encoder)

- USE produit une représentation vectorielle dense de chaque phrase 
- **Représentation sémantique** : Les vecteurs produits par USE sont créés pour que les phrases similaires (sémantiquement proches) aient des vecteurs proches dans l’espace vectoriel.

<div class="flex items-left justify-left mt-4">
  <div style="display: flex; gap: 20px;">
    <img src="/tnse_use_category.png" alt="Illustration du projet" style="width: 50%; height: auto; max-height: 350px;" />
    <img src="/tnse_use_clusters.png" alt="Illustration du projet" style="width: 50%; height: auto; max-height: 350px;" />
  </div>
</div>
<div class="encart-dark flex-1 encart-centered">
  Score ARI : 0.5122 Bonne séparation des catégories
</div>

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centrer les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
transition: fade-out
layout: cover
---
# _III.Présentation des approches de modélisation de classification des images_


---
transition: fade-out
zoom: 0.8
---

# Approche SIFT

- **SIFT** : alorithme du domaine de la vision par ordinateur de reconnaissance de caractéristiques(feature détection).Il permet de **détecter et d'extraire des descripteurs de points clés dans une image** (bord,contours et point d'intérêt)qui sont invariant aux variations d'échelle et à la rotation.


<div class="flex items-left justify-left mt-4">
  <div style="display: flex; gap: 20px;">
    <img src="/schéma_sift.png" alt="Illustration du projet" style="height: auto; max-height: 450px;" />
  </div>
</div>


<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centrer les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>



---
transition: fade-out
zoom: 0.8
---

# Approche Bag of words : SIFT  (Bidirectional Encoder Representations from Transformers)



<div class="flex items-left justify-left mt-4">
  <div style="display: flex; gap: 20px;">
    <img src="/tnse_sift_category.png" alt="Illustration du projet" style="width: 50%; height: auto; max-height: 350px;" />
    <img src="/tnse_sift_cluster.png" alt="Illustration du projet" style="width: 50%; height: auto; max-height: 350px;" />
  </div>
</div>
<div class="encart-dark flex-1 encart-centered">
  Score ARI : 0.04989 SIFT ne permet pas la séparation des catégories
</div>

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centrer les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
transition: fade-out
zoom: 0.8
---

# Approche CNN transfer Learning et data augmentation avec VGG 16

- **CNN réseau de neurones** conçu pour traiter des données ayant une structure de grille, comme les images:
  - **Couches de convolution**: elles extraient automatiquement des caractéristiques importantes des images (comme les bords, textures, motifs).
  - **Couches de pooling** : elles réduisent la taille des images pour diminuer le nombre de calculs, tout en gardant les informations principales.
  - **Couches entièrement connectées** : en fin de réseau, elles combinent les caractéristiques extraites pour classer ou interpréter l'image.

**VGG16**: 13 couches de convolution et 3 couches entièrement connectées entraîné sur l'ensemble des données ImageNET

**Transfer Learning** : Le Transfer Learning consiste à utiliser un modèle pré-entraîné et à adapter ce modèle pour une tâche spécifique avec moins de données et de temps d'entraînement.

**Data Augmentation** : La Data Augmentation consiste à créer de nouvelles images d'entraînement en appliquant des transformations sur les images existantes:

  - Rotations, translations, zooms, et inversions.
  - Changements de luminosité ou d'échelle de couleurs.
  - Découpes aléatoires ou ajouts de bruit.
<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centrer les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
---
transition: fade-out
zoom: 0.8
---

# Approche CNN transfer Learning et data augmentation avec VGG 16


<div class="flex">
  <img src="/schéma_vgg16.png" alt="Illustration du projet" style="max-width: 100%; height: auto;" />
</div>

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centre les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>


---
transition: fade-out
layout: cover
---
# _IV.Utilisation de l'api pour récupération de produit_

---
transition: fade-out
zoom: 0.6
---

# Création du script avec api pour récupération des produits


```python
# Script for API 

# Term to search
query = 'champagne'

# URL of API
url = 'https://api.edamam.com/api/food-database/v2/parser'

# parameter query 
params = {
    'app_id': app_id,
    'app_key': app_key,
    'ingr': query,

}

# Send request GET
response = requests.get(url, params=params)

# Verify statut of response
if response.status_code == 200:
    data = response.json()
    # Extract first 10 products
    hints = data.get('hints', [])[:10]
    # Prepare data 
    products = []
    for hint in hints:
        food = hint.get('food', {})
        products.append({
            'foodId': food.get('foodId', ''),
            'label': food.get('label', ''),
            'category': food.get('category', ''),
            'foodContentsLabel': food.get('foodContentsLabel', ''),
            'image': food.get('image', '')
        })
    # Create dataframe
    df = pd.DataFrame(products)
    # Save dataframe into csv file 
    df.to_csv('edamam_products.csv', index=False)
    print('Les données ont été enregistrées dans edamam_products.csv')
else:
    print(f'Erreur {response.status_code} : {response.text}')

```

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centre les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>

---
transition: fade-out
layout: cover
---
# _V.Conclusion du Projet_
---
transition: fade-out
---

# Faisabilité du moteur de classification 

- L'analyse graphique et du score ARI nous permis qu'il est réailisable de séparer automatiquement les produits selon leurs vraies catégories avec leurs nom/description et des images

<style>
.encart-dark {
  border: 2px solid #ffffff;
  padding: 15px;
  border-radius: 8px;
  background-color: #333333;
  color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  margin: 20px 0;
  max-width: 500px; /* Limite la largeur de l'encart */
}

/* Centre l'encart en définissant une marge automatique */
.encart-centered {
  margin-left: auto;
  margin-right: auto;
}

/* Centre les images */
.flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
