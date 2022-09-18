# Import Splinter to automate browser actions
# BeautifulSoup, pandas, time, and chromedriver
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager as cdm

def scrape():
    # Setup splinter / remote chrome browser driver
    executable_path = {'executable_path': cdm().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Create an empty dict for listings that we can save to Mongo
    collection = {}
    #----Below this Repeat remote chrome driver as needed----##
    #---------------to scrape each updated page--------------##

    ##  Scrape 1st Webpage JPL MARS Planet Science News ##

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
    collection["news_title"] = soup.find(class_="content_title").get_text()
    collection["news_teaser"] = soup.find(class_="article_teaser_body").get_text()

    #------------------------Continue------------------------##

    ##  Scrape 2nd Webpage JPL Lab Space Image ##

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
    collection["feature"] = url + feature

    #------------------------Continue------------------------##

    ##  Scrape 3rd Webpage Talaxyfacts Mars Facts ##

    # The url we want to scrape
    url = "https://galaxyfacts-mars.com/"
    
    # Go to the page we wish to scrape
    browser.visit(url)

    # Delay briefly while the page loads
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html

    # Modify the table in Pandas 
    tabledata = pd.read_html(url)
    table = tabledata[0]
    new_h = table.iloc[0]
    table = table[1:]
    table.columns = new_h
    table.set_index('Mars - Earth Comparison')
    table.to_html(index=False)
    
    # Populate the dictionary 
    collection["table"] = table.to_html(index=False, classes="table table-striped table-hover")

    #------------------------Continue------------------------##

    ##  Scrape 4th Webpage Astropedia Cerberus Hemispheres ##

    # The url we want to scrape
    url = "https://marshemispheres.com/"
    
    # Go to the page we wish to scrape
    browser.visit(url)

    # Delay briefly while the page loads
    time.sleep(1)

    # You will need to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.
    browser.links.find_by_partial_text('Cerberus').click()

     # Delay briefly while the page loads
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and use the html parser
    soup = bs(html, "html.parser")

    # Populate the dictionary with key-value pairs for Hemisphere names and image urls
    collection["cerb_title"] = 'Cerberus Hemisphere'
    result = soup.find_all('a')[3]
    cerb_jpg = result['href']
    collection["cerb_jpg"] = url + cerb_jpg

#------------------------Continue------------------------##

    ##  Scrape 4th Webpage Astropedia Schiaparelli Hemispheres ##

    # The url we want to scrape
    url = "https://marshemispheres.com/"
    
    # Go to the page we wish to scrape
    browser.visit(url)

    # Delay briefly while the page loads
    time.sleep(1)

    # You will need to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.
    browser.links.find_by_partial_text('Schiaparelli').click()

    # Delay briefly while the page loads
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and use the html parser
    soup = bs(html, "html.parser")

    # Populate the dictionary with key-value pairs for Hemisphere names and image urls
    collection["schi_title"] = 'Schiaparelli Hemisphere'
    result = soup.find_all('a')[3]
    schi_jpg = result['href']
    collection["schi_jpg"] = url + schi_jpg

    #------------------------Continue------------------------##

    ##  Scrape 4th Webpage Astropedia Syrtis Major Hemispheres ##

    # The url we want to scrape
    url = "https://marshemispheres.com/"
    
    # Go to the page we wish to scrape
    browser.visit(url)

    # Delay briefly while the page loads
    time.sleep(1)

    # You will need to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.
    browser.links.find_by_partial_text('Syrtis').click()

    # Delay briefly while the page loads
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and use the html parser
    soup = bs(html, "html.parser")

    # Populate the dictionary with key-value pairs for Hemisphere names and image urls
    collection["syrt_title"] = 'Syrtis Major Hemisphere'
    result = soup.find_all('a')[3]
    syrt_jpg = result['href']
    collection["syrt_jpg"] = url + syrt_jpg

    #------------------------Continue------------------------##

    ##  Scrape 4th Webpage Astropedia Valles Marineris Hemispheres ##
    
    # The url we want to scrape
    url = "https://marshemispheres.com/"
    
    # Go to the page we wish to scrape
    browser.visit(url)

    # Delay briefly while the page loads
    time.sleep(1)

    # You will need to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.
    browser.links.find_by_partial_text('Valles').click()

    # Delay briefly while the page loads
    time.sleep(1)

    # Return all the HTML on our page
    html = browser.html
    
    # Create a Beautiful Soup object, pass in our HTML, and use the html parser
    soup = bs(html, "html.parser")

    # Populate the dictionary with key-value pairs for Hemisphere names and image urls
    collection["vall_title"] = 'Valles Marineris Hemisphere'
    result = soup.find_all('a')[3]
    vall_jpg = result['href']
    collection["vall_jpg"] = url + vall_jpg

    # Quit the browser
    browser.quit()
    
    #-----------End Multi-page CDM Scrape Commands-----------##
    # Return our populated dictionary
    return collection