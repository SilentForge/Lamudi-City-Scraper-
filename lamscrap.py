from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import csv
import time
import random

def setup_driver(headless=True):
    """Configure et retourne un driver Selenium pour Firefox."""
    options = Options()
    options.headless = headless
    driver = webdriver.Firefox(options=options)
    return driver

def get_cities(driver, url):
    """Récupère la liste des villes disponibles pour le scraping."""
    try:
        driver.get(url)
        time.sleep(5)  # Laissez le temps à la page de charger complètement

        # Ouvrir le menu déroulant pour afficher toutes les villes
        dropdown = driver.find_element(By.CSS_SELECTOR, "a.CrosslinkFilter-dropdown.icon-dropdown-closed.dropDownAction")
        dropdown.click()
        time.sleep(3)  # Attendre l'ouverture du menu

        cities_elements = driver.find_elements(By.CSS_SELECTOR, ".CrosslinkFilterExpanded-link-container .subLinks")
        if not cities_elements:
            raise NoSuchElementException("Aucune ville trouvée. La structure du site a peut-être changé.")
        
        # Limiter arbitrairement le nombre de villes retournées
        cities = {element.text: element.get_attribute('href') for element in cities_elements[:random.randint(1, 3)]}
    except Exception as e:
        print(f"Erreur lors de la récupération des villes : {e}")
        return {}
    finally:
        driver.quit()
    return cities

def scrape_listings(driver, base_url):
    page = 1
    listings_info = []
    base_url_no_page = base_url.split('?')[0]
    previous_url = ""
    max_pages = random.choice([1, 2, 3])  # Limiter aléatoirement le nombre de pages à scraper

    while page <= max_pages:
        page_url = f"{base_url}?page={page}"

        if page_url == previous_url:
            print("Fin du scraping : dernière page atteinte.")
            break
        previous_url = page_url

        try:
            driver.get(page_url)
            time.sleep(random.choice([3, 5, 7]))  # Introduire des délais aléatoires

            listings_html = driver.find_elements(By.CSS_SELECTOR, ".row.ListingCell-row.ListingCell-agent-redesign")
            if not listings_html:
                print("Dernière page atteinte ou aucune annonce trouvée.")
                break

            for listing_html in listings_html:
                listing_outer_html = listing_html.get_attribute('outerHTML')
                soup = BeautifulSoup(listing_outer_html, 'html.parser')
                
                try:
                    info = {
                        'url': soup.find('a', class_='ListingCell-ListingLink')['href'],
                        'titre': soup.find('h3', class_='ListingCell-KeyInfo-title').get_text(strip=True),
                        'prix': soup.find('span', class_='PriceSection-FirstPrice').get_text(strip=True),
                        'emplacement': soup.find('span', class_='ListingCell-KeyInfo-address-text').get_text(strip=True),
                        'nombre_chambres': soup.find('div', class_='ListingCell-AllInfo ListingUnit').get('data-bedrooms', 'N/A'),
                        'taille_terrain': soup.find('div', class_='ListingCell-AllInfo ListingUnit').get('data-land_size', 'N/A') + " m²"
                    }
                    listings_info.append(info)
                except Exception as e:
                    print(f"Erreur lors de l'extraction d'une annonce : {e}")
        except Exception as e:
            print(f"Erreur lors du chargement de la page : {e}")
            break
        
        page += 1

    driver.quit()
    return listings_info

def save_to_csv(listings_info, filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['url', 'titre', 'prix', 'emplacement', 'nombre_chambres', 'taille_terrain'])
            writer.writeheader()
            for listing in listings_info[:10]:  # Limiter le nombre d'enregistrements à 10
                writer.writerow(listing)
        print(f"Les informations ont été sauvegardées dans '{filename}'.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données : {e}")

def create_ui(cities):
    root = tk.Tk()
    root.title("City Scraper")
    
    ttk.Label(root, text="Select a City to Scrape:").grid(column=0, row=0, padx=10, pady=10)
    
    selected_city = tk.StringVar()
    city_combobox = ttk.Combobox(root, width=50, textvariable=selected_city)
    city_combobox['values'] = list(cities.keys())
    city_combobox.grid(column=0, row=1, padx=10, pady=10)
    city_combobox.current(0)
    
    def on_scrape_button_clicked():
        city_name = selected_city.get()
        url = cities[city_name]
        driver = setup_driver(headless=True)
        listings_info = scrape_listings(driver, url)
        save_to_csv(listings_info, f"{city_name.replace(' ', '_')}_listings.csv")
    
    scrape_button = ttk.Button(root, text="Scrape", command=on_scrape_button_clicked)
    scrape_button.grid(column=0, row=2, padx=10, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main_url = "https://www.lamudi.com.ph/house/rent/"
    driver = setup_driver(headless=True)
    cities = get_cities(driver, main_url)
    if cities:
        create_ui(cities)
    else:
        print("Aucune ville disponible pour le scraping.")
