# Import Splinter to automate browser actions
from splinter import Browser

# Import Beautiful Soup
from bs4 import BeautifulSoup as bs

# Import the Chromedriver
from webdriver_manager.chrome import ChromeDriverManager as cdm

# Import the others
import pandas as pd
import time

def scrape1():
    # Setup splinter
    executable_path = {'executable_path': cdm().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Create an empty dict for listings that we can save to Mongo
    news_scrape = {}

    # The url we want to scrape
    url = "https://redplanetscience.com/"
    
    # Go to the page we wish to scrape
    browser.visit(url)

    # Delay briefly while the page loads
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and use the html parser
    soup = bs(html, "html.parser")

    # Populate the dictionary with key-value pairs for the headline, price, and reviews
    news_scrape["news_title"] = soup.find("a", class_="content_title").get_text()
    news_scrape["news_teaser"] = soup.find("h4", class_="article_teaser_body").get_text()

    # Quit the browser
    browser.quit()

    # Return our populated dictionary
    return news_scrape

    def scrape2, 3, 4