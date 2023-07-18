from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time 

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

latest_string = ""

def extract(text):
    idx = text.find("#")
    if (idx != - 1):
        original_list = text[0:idx].split()
        x = text[0:idx].lower() #removes last 104 characters to aid time complexity for split function?
        list1 = x.split()
        try:
            index = list1.index("text")
            return original_list[index + 1]
        except ValueError:
            print("keyword not found")
            return None
    else:
        print("keyword not found")
        return None
def fetch_tweet(user):
    url = f"https://twitter.com/ChipotleTweets"
    print(url)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[2]/div')))
        if myElem.text != latest_string:
            start = time.time()
            x = extract(myElem.text)
            end = time.time()
            if (x != None): 
                print(x)
                print("Extraction Runtime: ", end - start)
    except TimeoutException:
        print ("Loading took too much time!")
fetch_tweet("ChipotleTweets")