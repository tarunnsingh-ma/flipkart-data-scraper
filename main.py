from bot import Flipkart_Scrapper
import time



if __name__ == "__main__": 
    print ("Bot Started...")
    flipkart_scraper = Flipkart_Scrapper("config.cfg")
    flipkart_scraper.scrape()
