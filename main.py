from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


options = Options()
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=C:\\Users\\Techron\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)
url = "https://web.whatsapp.com/"
driver.get(url)
driver.implicitly_wait(10)

time.sleep(4)
def find_contact(cname):
    contacts = driver.find_elements(By.XPATH, "//span[contains(@class, 'ggj6brxn')]")
    filtered_contacts = [contact for contact in contacts if contact.get_attribute('title')]
    if cname in filtered_contacts:
        cname.click()
    elif cname not in filtered_contacts:
        search_bar = driver.find_element(By.XPATH, "(//p[contains(@class,'selectable-text copyable-text')])[1]")
        search_bar.click()
        search_bar.send_keys(cname)
        time.sleep(2)
        chat_bar = driver.find_element(By.XPATH,"//div[@class = '_199zF _3j691']")
        chat_bar.click()
    else:
        print(f"{cname} is not in contacts")

def send_message(msg):
    msgbox = driver.find_element(By.CLASS_NAME,"_3Uu1_")
    msgbox.send_keys(Keys.CONTROL + "a")
    msgbox.send_keys(Keys.DELETE)
    msgbox.send_keys(msg)
    msgbox.send_keys(Keys.ENTER)
    print("Message sent")

def main(cname,msg):
    find_contact(cname)
    send_message(msg)
    time.sleep(5)
    driver.quit()