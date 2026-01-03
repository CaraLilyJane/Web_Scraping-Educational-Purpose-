# Web_Scraping-Educational-Purpose-
Product list and prices scraping from a supermarket (This project is used for Educational Purpose only.)

🛍️ City Mall Web Scraper (Myanmar)
📌 Overview

This Python project scrapes product information from the City Mall Myanmar website. The script collects:

Product Name

Product Price

It navigates through all pages automatically and saves the results into an Excel file with the current date.

🛠️ Technologies & Libraries Used

Python 3

requests – for sending HTTP requests

BeautifulSoup (bs4) – for parsing HTML content

pandas – for data processing and Excel export

tqdm – for progress visualization

re – for text cleaning and formatting

datetime – for timestamped filenames

time – to control request frequency

urllib3 & requests.adapters – for retrying failed requests

⚙️ Features

Automatically detects and navigates all pages of the product listing

Extracts:

Product name (cleaned and formatted)

Product price (converted to integer)

Implements retry logic for network errors (429, 500, 502, 503, 504)

Exports the results to an Excel (.xlsx) file with the current date in the filename

Sleep delays included to prevent overwhelming the server

📂 Output

The script generates an Excel file in the project directory:

Output_YYYY-MM-DD.xlsx

Example Columns:
Product Name	Product Price
Samsung_Galaxy_S23	1999000
iPhone_14_Pro	2399000
🚀 How to Run the Script
1️⃣ Install Required Packages
pip install requests beautifulsoup4 pandas tqdm html5lib

2️⃣ Run the Script
python main.py


(Replace main.py with your filename if different.)

📌 Notes & Limitations

This script relies on the current HTML structure of the website. If the site updates, selectors may need adjustment.

Ensure stable internet connection while scraping.

Use responsibly and respect the website’s terms of service.

🔮 Future Improvements

Improve error handling and logging

Add command-line arguments for flexible usage

Implement multi-threading for faster scraping

Export data to CSV or database

Include product availability or category information

👤 Author

Thin Thin
Python & Data Automation Enthusiast
Civil / Hydraulic Engineer
