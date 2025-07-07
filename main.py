import time

import pandas as pd

from amazon import amazon_scraper

def main():
    keywords = pd.read_json('user_queries.json').iloc[:, 0].tolist()
    # keywords = ["headphones"] # for testing purposes
    total_items = []
    for keyword in keywords:
        items = amazon_scraper(keyword)
        df = pd.DataFrame(items)
        df.to_json(f'{keyword}.json', orient='records')
        time.sleep(5)
    
if __name__ == "__main__":
    main()
