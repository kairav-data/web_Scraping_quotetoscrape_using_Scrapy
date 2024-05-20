**Quotes Scraping Project :/n**
This repository contains a web scraping project using Scrapy to scrape quotes from quotes.toscrape.com. The scraped data includes the text of the quotes, the authors, and the tags associated with each quote. The data is then stored in an SQLite database.

**Features:/n**
Scrapes quotes, authors, and tags from the website.
Stores the scraped data into an SQLite database.
Implements Scrapy pipelines to process and save the data.

**Project Structure:/n**
spiders/quotes_spider.py: Contains the spider code to scrape the quotes.
pipelines.py: Defines the pipeline to store the scraped data in an SQLite database.
items.py: Defines the data structure for the scraped items.
settings.py: Configuration settings for the Scrapy project.

**install virtual environment:/n**
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

**Install the required packages:/n**
pip install -r requirements.txt
