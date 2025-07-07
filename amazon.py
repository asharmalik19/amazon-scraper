import time

import pandas as pd
from curl_cffi import requests
from bs4 import BeautifulSoup

def parse_items(soup):
    items_selector = 'div[data-cy="asin-faceout-container"]'
    items = soup.select(items_selector)

    total_items = []
    for item in items:
        title = item.select_one('div[data-cy="title-recipe"]')
        price = item.select_one('span[class="a-price"] span[class="a-offscreen"]')
        total_reviews = item.select_one('span[data-component-type="s-client-side-analytics"] span')
        image_url = item.select_one('img')

        # Output data schema
        total_items.append({
            'title': title.text.strip() if title else '',
            'price': price.text.strip() if price else '',
            'total_reviews': total_reviews.text.strip() if total_reviews else '',
            'image_url': image_url['src'] if image_url else '',
            'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
        })
    return total_items

def get_next_page_url(soup):
    BASE_URL = 'https://www.amazon.com'
    next_page = soup.select_one('a[aria-label^="Go to next page"]')
    next_page_url = BASE_URL + next_page['href'] if next_page else None
    return next_page_url

def amazon_scraper(keyword):
    url = f'https://www.amazon.com/s?k={keyword}'
    print(f'Scraping: {url}')

    total_items = []
    # control the no of pages to scrape
    for page in range(0, 20):
        r = requests.get(url, impersonate='chrome')
        soup = BeautifulSoup(r.text, 'html.parser')
        items = parse_items(soup)
        total_items.extend(items)
        url = get_next_page_url(soup)
        if not url:
            break
        print(f'Page {page + 1} scraped.')
    return total_items
    
        
if __name__=='__main__':
    print('Warning! Do not run me directly')
    amazon_scraper('headphones')



    
    