# City Scraper Project
# Lamudi Scraper

## Important Notice

This project has transitioned to a monetized service on Apify. The full-featured version with unlimited scraping capabilities is now available exclusively on Apify.

For full access, visit the [Apify Actor]([https://console.apify.com/actors/qRbb45JvqeJUKBaw4](https://apify.com/pixelperfekt/lamudi-ph-real-estate-listings-scraper)).

## Features

The open-source version provides a limited preview of the capabilities:
- Scrapes basic property information from Lamudi.
- Limited to a few sample listings.

For full functionality, including unlimited scraping and advanced features, please use the Apify service.

## Why the Change?

We have decided to transition this project to a monetized service to ensure continuous improvements, dedicated support, and to cover the ongoing costs of development and maintenance.

## Contact

For any inquiries or support, please contact [pixelperfekt@proton.me].

## Overview
**City Scraper** is an advanced web scraping tool designed to extract real estate listings from [Lamudi](https://www.lamudi.com.ph/house/rent/). It leverages Python with Selenium and BeautifulSoup for scraping, and Tkinter for its graphical user interface (GUI). This script efficiently collects data on rental properties across various cities and saves the information into CSV files for analysis, demonstrating a practical application of web scraping for real-world data collection challenges.

## Features
- **Dynamic City Selection**: Enables scraping of real estate listings from multiple cities.
- **Headless Browser Support**: Operates in headless mode for efficiency and compatibility with server or automated environments.
- **CSV Output**: Organizes scraped data into CSV format for ease of storage and analysis.
- **Dynamic Data Collection**:  Captures real-time listings, including detailed property information.
- **Customizable Scraper**: Easily extendable for additional fields or other websites with similar structures.
- **User-Friendly Interface**: Simplifies operation with a GUI, removing the need for code modifications.


## How It Works
- **Setup Selenium Driver**: Initializes a headless Firefox browser session.
- **City Listings Retrieval**: Extracts cities from the dropdown menu on the main page.
- **Scrape Listings**: Collects data from each property listing in the selected city.
- **Data Parsing**: Parses HTML content to extract and organize listing details.
- **CSV File Saving**: Saves the collected data into a CSV file named after the city.
- Graphical User Interface: Facilitates city selection and scraping initiation through a GUI.

## Requirements
- Python 3.6+
- Selenium
- BeautifulSoup4
- Tkinter (typically included with Python)
- Firefox and geckodriver installed and configured

## Installation
Ensure you have Python 3.6+ installed on your system. Then, install the required dependencies using pip:

pip install selenium beautifulsoup4

**Note**: Selenium requires a WebDriver for Firefox. Download it from [Mozilla's geckodriver](https://github.com/mozilla/geckodriver/releases) and ensure it's in your PATH.

## Usage
To start the scraper:
1. Run the script with Python:
python lamscrap.py
2. The GUI will launch. Select a city from the dropdown menu.
3. Click "Scrape" to begin collecting data. The results will be saved in a CSV file named after the selected city.

## Why This Tool?
City Scraper is tailored for the website [Lamudi](https://www.lamudi.com.ph/house/rent/)., a leading real estate platform in the Philippines, showcasing a wide range of properties for rent. This tool is designed to automate the data collection process, making it invaluable for real estate analysis, market research, and data enthusiasts interested in property trends.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer
This tool is for educational purposes only. Be mindful of the target website's terms of service regarding web scraping and data usage.


----------------------

# Projet City Scraper

## Aperçu
**City Scraper** est un outil de web scraping avancé conçu pour extraire les annonces immobilières du site [Lamudi](https://www.lamudi.com.ph/house/rent/). Il utilise Python avec Selenium et BeautifulSoup pour le scraping, et Tkinter pour son interface graphique (GUI). Ce script collecte efficacement des données sur les propriétés à louer dans diverses villes et sauvegarde les informations dans des fichiers CSV pour analyse, démontrant une application pratique du web scraping pour les défis de collecte de données dans le monde réel.

## Fonctionnalités
- **Sélection Dynamique de la Ville** : Permet le scraping d'annonces immobilières de plusieurs villes.
- **Support du Navigateur en Mode Sans Tête** : Fonctionne en mode headless pour une efficacité et une compatibilité avec les environnements serveur ou automatisés.
- **Sortie CSV** : Organise les données scrapées au format CSV pour faciliter le stockage et l'analyse.
- **Collecte de Données Dynamique** : Capture les annonces en temps réel, y compris des informations détaillées sur les propriétés.
- **Scraper Personnalisable** : Facilement extensible pour des champs supplémentaires ou d'autres sites web ayant des structures similaires.
- **Interface Utilisateur Conviviale** : Simplifie l'opération avec une GUI, éliminant le besoin de modifications de code.

## Fonctionnement
- **Configuration du Pilote Selenium** : Initialise une session de navigateur Firefox en mode sans tête.
- **Récupération des Annonces par Ville** : Extrait les villes du menu déroulant sur la page principale.
- **Scraping des Annonces** : Collecte des données de chaque annonce immobilière dans la ville sélectionnée.
- **Analyse des Données** : Parse le contenu HTML pour extraire et organiser les détails des annonces.
- **Sauvegarde des Fichiers CSV** : Sauvegarde les données collectées dans un fichier CSV nommé d'après la ville.
- Interface Graphique : Facilite la sélection de la ville et le lancement du scraping à travers une GUI.

## Prérequis
- Python 3.6+
- Selenium
- BeautifulSoup4
- Tkinter (généralement inclus avec Python)
- Firefox et geckodriver installés et configurés

## Installation
Assurez-vous d'avoir Python 3.6+ installé sur votre système. Ensuite, installez les dépendances requises en utilisant pip :

pip install selenium beautifulsoup4

**Note** : Selenium nécessite un WebDriver pour Firefox. Téléchargez-le depuis les [releases de geckodriver de Mozilla](https://github.com/mozilla/geckodriver/releases) et assurez-vous qu'il est dans votre PATH.

## Utilisation
Pour démarrer le scraper :
1. Exécutez le script avec Python :
python lamscrap.py
2. La GUI se lancera. Sélectionnez une ville dans le menu déroulant.
3. Cliquez sur "Scrape" pour commencer la collecte des données. Les résultats seront sauvegardés dans un fichier CSV nommé d'après la ville sélectionnée.

## Pourquoi Cet Outil ?
City Scraper est adapté pour le site [Lamudi](https://www.lamudi.com.ph/house/rent/), une plateforme immobilière de premier plan aux Philippines, présentant une large gamme de propriétés à louer. Cet outil est conçu pour automatiser le processus de collecte de données, le rendant inestimable pour l'analyse immobilière, la recherche de marché et les passionnés de données intéressés par les tendances immobilières.

## Contribution
Les contributions sont les bienvenues ! Veuillez forker le dépôt, apporter vos modifications et soumettre une pull request. Pour les changements majeurs, veuillez d'abord ouvrir une issue pour discuter de ce que vous souhaitez changer.

## Licence
Distribué sous la Licence MIT. Voir `LICENSE` pour plus d'informations.

## Avertissement
Cet outil est à des fins éducatives uniquement. Soyez attentif aux conditions de service du site cible concernant le web scraping et l'utilisation des données sur le web.
