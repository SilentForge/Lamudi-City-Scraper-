# City Scraper Project

## Overview
**City Scraper** is an advanced web scraping tool designed to extract real estate listings from [Lamudi](https://www.lamudi.com.ph/house/rent/). Utilizing Python with Selenium and BeautifulSoup, this script navigates through the site, collects data on rental properties in various cities, and saves this information into CSV files for further analysis. This project demonstrates a practical application of web scraping techniques to real-world data collection challenges, especially valuable for market analysis and real estate trends.

## Features
- **Dynamic Data Collection**: Scrapes real-time property listings, including URLs, titles, prices, locations, number of bedrooms, and lot sizes.
- **Customizable Scraper**: Easily extendable for additional fields or other websites with similar structures.
- **User-Friendly Interface**: Includes a simple GUI to select cities for scraping without editing the code.

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

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
Distributed under the MIT License. See `LICENSE` for more information.

---

# Projet City Scraper

## Vue d'ensemble
**City Scraper** est un outil avancé de web scraping conçu pour extraire les annonces immobilières de [Lamudi](https://www.lamudi.com.ph/house/rent/). Utilisant Python avec Selenium et BeautifulSoup, ce script navigue sur le site, collecte des données sur les propriétés à louer dans diverses villes, et enregistre ces informations dans des fichiers CSV pour une analyse ultérieure. Ce projet démontre une application pratique des techniques de web scraping aux défis de collecte de données du monde réel, particulièrement précieuse pour l'analyse du marché et les tendances immobilières.

## Fonctionnalités
- **Collecte de données dynamique** : Scrapes des annonces de propriétés en temps réel, incluant les URL, titres, prix, emplacements, nombre de chambres, et tailles de lots.
- **Scraper personnalisable** : Facilement extensible pour des champs supplémentaires ou d'autres sites Web avec des structures similaires.
- **Interface utilisateur conviviale** : Comprend une interface graphique simple pour sélectionner les villes à scraper sans modifier le code.

## Installation
Assurez-vous d'avoir Python 3.6+ installé sur votre système. Ensuite, installez les dépendances requises en utilisant pip :
pip install selenium beautifulsoup4
**Note** : Selenium nécessite un WebDriver pour Firefox. Téléchargez-le depuis [le geckodriver de Mozilla](https://github.com/mozilla/geckodriver/releases) et assurez-vous qu'il soit dans votre PATH.

## Utilisation
Pour démarrer le scraper :
1. Exécutez le script avec Python :
python lamscrap.py
2. L'interface graphique se lancera. Sélectionnez une ville dans le menu déroulant.
3. Cliquez sur "Scrape" pour commencer la collecte des données. Les résultats seront sauvegardés dans un fichier CSV nommé d'après la ville sélectionnée.

## Contribuer
Les contributions sont les bienvenues ! Veuillez forker le dépôt, faire vos changements, et soumettre une pull request. Pour les changements majeurs, veuillez ouvrir une issue d'abord pour discuter de ce que vous aimeriez changer.

## Licence
Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.



