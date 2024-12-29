from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from product_crawler.models import Product  

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






