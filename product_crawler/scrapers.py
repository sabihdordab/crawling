from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from .models import Product  

class BaseScraper(ABC):
    
    def __init__(self, url, limit=50):
        self.url = url
        self.limit = limit

    @abstractmethod
    def parse_products(self, html_content):
        pass

    def fetch_products(self):
        response = requests.get(self.url)
        
        if response.status_code == 200:
            return self.parse_products(response.text)
        else:
            return []

    def save_to_db(self, products):
        products_to_save = products[:self.limit]
        
        for product in products_to_save:
            Product.objects.update_or_create(
                source_url=product['source_url'],
                defaults={
                    'title': product['title'],
                    'price': product['price'],
                    'image_url': product['image_url'],
                    'source_website': product['source_website'],
                    'description': product['description'],
                    'source_url' : product['source_url'],
                }
            )

    def collect_products(self):
        products = self.fetch_products()
        if products:
            self.save_to_db(products)
        else:
            print("No products found to save.")


    def run(self):
        self.collect_products()



class DivarScraper(BaseScraper):
    
    def __init__(self, limit=50):
        url = "https://divar.ir/s/ahvaz/electronic-devices"
        super().__init__(url, limit)

    def parse_products(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        products = []
        for item in soup.find_all('article', class_='kt-post-card'):  
            title = item.find('h2', class_='kt-post-card__title').text.strip() if item.find('h2', class_='kt-post-card__title') else 'No title'
            description = item.find_all('div', class_='kt-post-card__description')[0].text.strip() if item.find_all('div', class_='kt-post-card__description') else 'No description'
            price = item.find_all('div', class_='kt-post-card__description')[1].text.strip() if len(item.find_all('div', class_='kt-post-card__description')) > 1 else 'No price'
        
            image = item.find('img')
            if image:
                image_url = image.get('data-src') if image.get('data-src') else image.get('src')
            else:
                image_url = None
        
        
            source_url = f"https://divar.ir{item.find('a', class_='kt-post-card__action')['href']}" if item.find('a', class_='kt-post-card__action') else None
        
        
            date = item.find('span', class_='kt-post-card__bottom-description').text.strip() if item.find('span', class_='kt-post-card__bottom-description') else ''
                   
        
            products.append({
                'title': title,
                'price': price,
                'description': description + ' ' + date,
                'image_url': image_url,
                'source_website': 'Divar',
                'source_url': source_url,
            })
    
        return products


class BamiloScraper(BaseScraper):
    
    def __init__(self, limit=50):
        url = "https://bamiloshop.ir/product-tag/%da%a9%d8%aa%d8%a7%d9%86%db%8c-%d8%b2%d9%86%d8%a7%d9%86%d9%87/"
        super().__init__(url, limit)

    def parse_products(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        products = []

        for item in soup.find_all('div', class_='product-wrapper'):
            title = item.find('h3', class_='wd-entities-title')
            if title:
                title = title.find('a').text.strip() if title.find('a') else 'No title'
            else:
                title = 'No title'

            description = item.find('span', class_='out-of-stock product-label')
            description = description.text.strip() if description else ''

            price_tag = item.find('span', class_='price')
            if price_tag:
                price = price_tag.find('bdi').text.strip() if price_tag.find('bdi') else 'No price'
            else:
                price = 'No price'

            link = item.find('a', class_='product-image-link')
            product_url = f"{link['href']}" if link else None

            image_tag = item.find('img')
            image_url = image_tag['src'] if image_tag  else None

            products.append({
                'title': title,
                'price': price,
                'description': description,
                'image_url': image_url,
                'source_website': 'Bamilo',
                'source_url': product_url,
            })

        return products