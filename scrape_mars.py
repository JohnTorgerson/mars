# Import Splinter to automate browser actions
from splinter import Browser

# Import Beautiful Soup
from bs4 import BeautifulSoup as bs

# Import the Chromedriver
from webdriver_manager.chrome import ChromeDriverManager as cdm

# Import the others
import pandas as pd
import time

def scrape():
    # Create an empty dict for listings that we can save to Mongo
    listings = {}
    #----Below this Repeat remote chrome driver as needed----##
    #---------------to scrape each updated page--------------##


    ##  Scrape 1st Webpage JPL MARS Planet Science News##
    # Setup splinter
    executable_path = {'executable_path': cdm().install()}
    browser = Browser('chrome', **executable_path, headless=False)

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

    # Populate the dictionary with key-value pairs for title and teaser paragraph
    listings["news_title"] = soup.find(class_="content_title").get_text()
    listings["news_teaser"] = soup.find(class_="article_teaser_body").get_text()

    # Quit the browser
    browser.quit()
    #------------------------Continue------------------------##

     ##  Scrape 2nd Webpage JPL Lab Space Image##
    # Setup splinter
    executable_path = {'executable_path': cdm().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # The url we want to scrape
    url = "https://spaceimages-mars.com/"
    
    # Go to the page we wish to scrape
    browser.visit(url)

    # Delay briefly while the page loads
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and use the html parser
    soup = bs(html, "html.parser")

    # Populate the dictionary with key-value pairs for the title and image url
    feature = soup.find('img', class_="headerimage fade-in")['src']
    listings["feature"] = feature

    # Quit the browser
    browser.quit()
    #------------------------Continue------------------------##

     ##  Scrape 3rd Webpage Talaxyfacts Mars Facts##
    # Setup splinter
    executable_path = {'executable_path': cdm().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # The url we want to scrape
    url = "https://galaxyfacts-mars.com/"
    
    # Go to the page we wish to scrape
    browser.visit(url)

    # Delay briefly while the page loads
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html

    # Populate the dictionary 
    tabledata = pd.read_html(url){0}
    table = tabledata[1]
    new_h = table.iloc[0]
    table = table[1:]
    table.columns = new_h
    table.set_index('Mars - Earth Comparison')
    table.to_html(index=False)
    listings["table"] = table.to_html(index=False)

    # Quit the browser
    browser.quit()
    #------------------------Continue------------------------##

     ##  Scrape 4th Webpage Astropedia Mars Hemispheres##
    # # Setup splinter
    # executable_path = {'executable_path': cdm().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    # # The url we want to scrape
    # url = "https://marshemispheres.com/"
    
    # # Go to the page we wish to scrape
    # browser.visit(url)

    # # Delay briefly while the page loads
    # time.sleep(1)

    # # Return all the HTML on our page
    # html = browser.html
    
    # # Create a Beautiful Soup object, pass in our HTML, and use the html parser
    # soup = bs(html, "html.parser")

    # # Populate the dictionary with key-value pairs for Hemisphere names and image urls
    # Edit These vv Get Statements (maybe loop back 4x)
    # listings["news_title"] = soup.find(class_="content_title").get_text()
    # listings["news_teaser"] = soup.find(class_="article_teaser_body").get_text()

    # # Quit the browser
    # browser.quit()

    
    #-----------End Multi-page CDM Scrape Commands-----------##
    # Return our populated dictionary
    return listings