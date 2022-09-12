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
    # Setup splinter / remote chrome browser driver
    executable_path = {'executable_path': cdm().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Create an empty dict for listings that we can save to Mongo
    mars_db = {}
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
    mars_db["news_title"] = soup.find(class_="content_title").get_text()
    mars_db["news_teaser"] = soup.find(class_="article_teaser_body").get_text()

    # Quit the browser
    browser.quit()
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
    mars_db["feature"] = feature

    # Quit the browser
    browser.quit()
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
    mars_db["table"] = table.to_html(index=False)

    # Quit the browser
    browser.quit()
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
    mars_db["cerb_title"] = 'Cerberus Hemisphere'
    cerb_tif = browser.links.find_by_partial_text('cerberus_enhanced').text
    mars_db["cerb_tif"] = url + cerb_tif

    # Quit the browser
    browser.quit()

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
    mars_db["schi_title"] = 'Schiaparelli Hemisphere'
    schi_tif = browser.links.find_by_partial_text('schiaparelli_enhanced').text
    mars_db["schi_tif"] = url + schi_tif

    # Quit the browser
    browser.quit()

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
    mars_db["syrt_title"] = 'Syrtis Major Hemisphere'
    syrt_tif = browser.links.find_by_partial_text('syrtis_major_enhanced').text
    mars_db["syrt_tif"] = url + syrt_tif

    # Quit the browser
    browser.quit()

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
    mars_db["vall_title"] = 'Valles Marineris Hemisphere'
    vall_tif = browser.links.find_by_partial_text('valles_marineris_enhanced').text
    mars_db["vall_tif"] = url + vall_tif

    # Quit the browser
    browser.quit()
    
    #-----------End Multi-page CDM Scrape Commands-----------##
    # Return our populated dictionary
    return mars_db