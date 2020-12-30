# Model credentials
URL = "https://www.google.com/search"
HEADERS = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"" AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/84.0.4147.135 Safari/537.36"}
# Import libraries
import requests
from bs4 import BeautifulSoup
import sys

def search(query):
    """ API calling """
    SESSION = requests.Session()
    response = SESSION.get(URL, params={"q": query}, headers=HEADERS)
    try:
        if response.status_code == 200:
            document=BeautifulSoup(response.text, "html.parser")
            content = document.find_all("div", class_="kp-blk c2xzTb Wnoohf OJXvsb")
            display_text=content[0].find_all("div", class_="ifM9O")[0]
            snippet=str(display_text.find_all("div", class_="mod")[0])
            url=str(display_text.find('a').get('href'))
            title=str(display_text.find_all("h3", class_="LC20lb DKV0Md")[0].findAll('span')[0].text)
            titleup=str(display_text.find_all("div", class_="TbwUpd NJjxre")[0].text)
            output={"snippet":snippet,"titleup":titleup,"title":title,"url":url}
            return(output)
        else:
            pass
    except:
        print("Oops! " + str(sys.exc_info()) + " occured.")
        pass
