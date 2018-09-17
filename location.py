#location script
#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

def login(driver, _username, _password):
    username = driver.find_element_by_xpath('//input[@type="text"]')
    username.send_keys(_username)
    time.sleep(3)
    password = driver.find_element_by_xpath('//input[@type="password"]')
    password.send_keys(_password)
    submitButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Log in")]')))
    time.sleep(3)
    submitButton.click()
    time.sleep(3)

def mostRecentPost(driver):
    post = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/section/main/article/div[2]/div/div[1]/div[1]')))
    post.click()
    post.click()

def like(driver):
    for x in range(1, int(count)):
        heart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button')))
        heart.click()
    
        next = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[1]/div/div/a[2]')))
        next.click()
        print("Total likes: " + str(x))
        time.sleep(2)

locations = ['https://www.instagram.com/explore/locations/323005774/oahu-life/', 'https://www.instagram.com/explore/locations/213953267/honolulu-hawaii/', 'https://www.instagram.com/explore/locations/7168034/kapolei-hawaii/', 'https://www.instagram.com/explore/locations/235236339/kailua-honolulu-county-hawaii/', 'https://www.instagram.com/explore/locations/217866689/kaneohe-hawaii/', 'https://www.instagram.com/explore/locations/1865880/ewa-beach-hawaii/', 'https://www.instagram.com/explore/locations/301127/mililani-town-hawaii/', 'https://www.instagram.com/explore/locations/226354908/waipahu-hawaii/', 'https://www.instagram.com/explore/locations/1806574296285140/north-shore-oahu-hawaii/', 'https://www.instagram.com/explore/locations/213529821/pearl-city-hawaii/', 'https://www.instagram.com/explore/locations/493088/aiea-hawaii/', 'https://www.instagram.com/explore/locations/216875770/waianae-hawaii/' , 'https://www.instagram.com/explore/locations/878354670/ko-olina/', 'https://www.instagram.com/explore/locations/213255755/daniel-k-inouye-international-airport/']

_username = input("Username: ")
_password = input("Password: ")

#hashtag = input("Targeted hashtag: ")
location = input("1. Oahu  2. Honolulu 3. Kapolei  4. Kailua   5. Kaneohe\n6. Ewa Beach 7. Mililani 8. Waipahu 9. North Shore 10. Pearl City\n11. Aiea  12. Waianae 13. Ko Olina 15. Airport 16. Other location. \nLocation number: ")

count = input("Number of likes: ")
driver = webdriver.Firefox()

#startpage
url = 'https://www.instagram.com/accounts/login/?hl=en'
driver.get(url)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/span/section/main/div/article/div/div[2]/p/a')));

login(driver, _username, _password)

#location URL
driver.get(str(locations[int(location) - 1]))

#select first post
mostRecentPost(driver)

#begin liking
like(driver)

driver.quit()
