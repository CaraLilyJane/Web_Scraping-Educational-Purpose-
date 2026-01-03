import re
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm
import pandas as pd
import time
from datetime import date

def main():
    default_url = "https://www.citymall.com.mm/citymall/my/c/id05011"

    url = default_url

    extracted_url_list = [default_url, ]
    product_list = []
    price_list = []
    while True:

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                   "AppleWebKit/537.36 (KHTML, like Gecko)"
                   "Chrome/120.0.0.0 Safari/537.36",
                   "Accept-Encoding":"identity"}

        session = requests.Session()
        retry = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]) 
        session.mount("https://", HTTPAdapter(max_retries=retry))

        response = session.get(url, headers=headers, timeout=30) 
        #print(response.status_code)

        bsObj = BeautifulSoup(response.text, "html5lib")

        next_link_tag = bsObj.find('a', class_ = 'page-link next')

        next_link_text = next_link_tag.get('href')

        if next_link_text != '#':
            next_link_part = next_link_text.split("/")[-1]
            next_link_url = default_url.replace('id05011', next_link_part)
            print(next_link_url)
            url = next_link_url
            extracted_url_list.append(url)
            time.sleep(2)
        else:
            print("All pages are scraped.")
            break

        #print(extracted_url_list)
        bsObj = BeautifulSoup(response.text, "html5lib")
        #Extract all product tags
        name_tags = bsObj.find_all("div", class_="product-info")
        number_tags = len(name_tags)
        #print(number_tags)

        def product_name(tag):
            """Extract Product Name"""
            name_tag = tag.find("div", class_="product-title")
            name_tag = name_tag.text.strip()
            name_tag = name_tag.replace("\n", "")
            name_tag = re.sub(r"\s{2,}", "_", name_tag.strip())
            return name_tag
        def product_price(tag):
            """Extract Product Price"""
            price_tag = tag.find("p", class_="product-price mt-1")
            price_tag = price_tag.text
            price_tag = price_tag.replace(",","").replace("Ks","").strip()
            price_tag = int(price_tag.replace("\n","").split()[0])
            return price_tag
        #Extract one product
        #dummy_tag = name_tags[0]
        count = 1

        for dummy_tag in name_tags:
            try:
                #print("\n")
                #print(count)
                #Product Name
                name_tag = product_name(dummy_tag)
                product = product_list.append(name_tag)
                #print("\n")
                #print(product)

                #Product Price
                price_tag = product_price(dummy_tag)
                price = price_list.append(price_tag)
                #print("\n")
                #print(price)        
                count = count + 1
            except:
                print(dummy_tag)
                raise
                break
    #print(product_list)
    #print(price_list)
    # Export to Excel
    data_dict = {"Product Name":product_list,
                "Product Price":price_list}
    #Create Data Frame
    df = pd.DataFrame(data_dict)
    today = date.today().strftime("%Y-%m-%d")
    df.to_excel(f"Output_{today}.xlsx", index=False)
    print("All Steps are completed.")
if __name__=="__main__":
    main()