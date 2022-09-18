# Unit 12 Homework: Mission to Mars
ubild a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following information outlines what you need to do.

##### Authors:
* John Torgerson (JohnTorgerson)
---

##### Tools & Supplies:
* jupyter notebook, PythonData38, MongoDB

* python, pandas, splinter, Browser, BeautifulSoup, ChromeDriverManager, requests, pymongo, flask, jinja
---

### Guide to Repo Contents:

* `mission_to_mars.ipynb` is a jupyter notebook for testing the individual chrome driver commands and for investigating scrape objects
* `insert.py` is app flask with the definition of the functions
* `README` is the file you're currently viewing
* `scrape_mars.py` is the app that defines the scrape functions operated by the web driver

* In folder, `templates`:
    1. `index.html` is the html code for the contents of the browser page
    
    
---

### Observations:
* The act of scraping is fairly simple, finding the html path for what is to be scraped is a challenge
* Having additional screens is helpful for looking at flask apps, scrape function apps, html pages, style sheets, and mongo db compasses, which are all talking to each other and referencing each other.
* The moving parts are small and simple, but there are lots of them.
* 

---

### Credits and Special Thanks

* Andrew Sundquist for sharing a 20-30 minute brainstorming session with me and debugging some unforgiving and finicky jinja syntax