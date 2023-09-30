from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=C:\\Users\\Techron\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)
url = "https://web.whatsapp.com/"
driver.get(url)
driver.implicitly_wait(10)


time.sleep(4)
def find_contact(pnumber):
    contacts = driver.find_elements(By.XPATH, "//span[contains(@class, 'ggj6brxn')]")

    filtered_contacts = [contact for contact in contacts if contact.get_attribute('title')]
    for contact in filtered_contacts:
        if pnumber == contact.text:
            contact.click()


def send_message(msg):
    msgbox = driver.find_element(By.CLASS_NAME,"_3Uu1_")
    msgbox.send_keys(Keys.CONTROL + "a")
    msgbox.send_keys(Keys.DELETE)
    msgbox.send_keys(msg)
    msgbox.send_keys(Keys.ENTER)


find_contact("Brayo")
send_message("This is code speaking to you")
#driver.quit()