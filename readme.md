<a name="readme-top"></a>
<!--
*** Thanks for using Document My Project. (https://github.com/luisvent/document_my_project) 
*** If you have a suggestion that would make this better, please fork  
*** the repo and create a pull request or simply open an issue.
*** Don't forget to give the project a star!
-->


<div align="center">

<a href="" target="_blank" title="Go to  website">
<img width="196px" alt="Projet 6 Openclassrooms : Classifiez automatiquement des biens de consommation" src="https://upload.wikimedia.org/wikipedia/fr/0/0d/Logo_OpenClassrooms.png">
</a>

# Projet 6 Openclassrooms : Classifiez automatiquement des biens de consommation

Ce projet explore la faisabilité d'un moteur de classification automatique pour une marketplace e-commerce anglophone. Il utilise l'image et la description textuelle des produits pour attribuer des catégories précises, offrant une expérience utilisateur optimisée et un gain de temps substantiel.

</div>


<div align="center"><h4><a href="#-about-the-project">ℹ️ About the Project</a> • <a href="#-stack-tech">🛠 Stack Tech</a> • <a href="#-setup">⚙ ️Setup</a></h4></div>

<p align="center"><img src="https://user.oc-static.com/upload/2023/03/30/1680170799854_Data%20Scientist-P6-01%20%281%29.png" alt="Main Image"/></p>

<!-- TABLE_CONTENT_PLACEHOLDER -->

## ℹ️ About the Project

L'entreprise Place de marché souhaite lancer une marketplace anglophone permettant aux vendeurs de proposer des articles à des acheteurs en postant une photo et une description. Actuellement, l'attribution de la catégorie des produits est manuelle, peu fiable, et ne peut être étendue à grande échelle.

Ce projet vise à :

1. Faciliter la mise en ligne de nouveaux articles en attribuant automatiquement des catégories aux produits basées sur leur description textuelle et leur image.

2. Améliorer l’expérience des acheteurs en rendant la recherche de produits plus précise.

3. Démontrer la faisabilité technique d'un moteur de classification automatique à partir d'un jeu de données fourni.

L’étude inclut :

- Prétraitement des données textes et images.

- Extraction et analyse des features (éléments caractéristiques).

- Visualisation réduite en deux dimensions et évaluation de la séparabilité des catégories.

- Classification supervisée avec des approches d'apprentissage automatique et deep learning.

- Test d’une collecte de produits à base de "champagne" via une API pour étendre la gamme d'articles.

Ce projet inclut également une présentation synthétique des résultats d'analyse sous forme de slides PDF.



## 🛠 Stack Tech
- [![Python][Python-badge]][Python-url] - A general-purpose programming language

[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python
[Python-url]: }
- [![Git][Git-badge]][Git-url] - A version control system

[Git-badge]: https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git
[Git-url]: }
- [![GitHub][GitHub-badge]][GitHub-url] - An online Git repository hosting service

[GitHub-badge]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github
[GitHub-url]: }


## ⚙ ️Setup

### Installation

To install this project, follow these steps:

1. Prérequis
- Python 3.8 ou supérieur
- Un environnement virtuel Python (recommandé)

2. Étapes d'installation
Clonez ce dépôt :
   ```bash
   git clone <https://github.com/dimitri-feniou/openclassrooms-projet6-classification-conso>
   cd <openclassrooms-projet6-classification-conso>
   ```

3. Créez et activez un environnement virtuel :
   ```bash
   python3 -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

5. Les dépendances principales incluent :
- `tensorflow` et `keras` : Pour l'entraînement et l'utilisation des modèles de deep learning.
- `opencv-python` : Pour la gestion des images et l'extraction des caractéristiques visuelles.
- `requests` : Pour les appels API externes.

Veuillez consulter le fichier `requirements.txt` pour une liste complète.



<p align="right"><a href="#readme-top">Top ⬆️</a></p>

---
 <div align="center">Built with ❤️ with <a href="https://github.com/luisvent/document_my_project">Document My Project</a></div>

