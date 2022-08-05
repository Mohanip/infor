from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(r'C:/chromedriver_win32/chromedriver.exe')

driver.get("https://www.gmail.com/")
# window_0 = browser.window_handles[0]
# window_0_title = browser.title
# print(window_0_title)
# browser.execute_script("window.open('https://facebook.com','new window')")
# window_1 = browser.window_handles[1]
# browser.switch_to.window(window_1)
# window_1_title = browser.title
#
# print(window_1_title)
#
# browser.switch_to.window(window_0)


emailElem = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
emailElem.send_keys("ipmohan5065@gmail.com")
nextButton = driver.find_element(By.XPATH, '//span[contains(text(),"Next")]')
nextButton.click()
time.sleep(5)
driver.quit()
# time.sleep(1)
# passwordElem = browser.find_element_by_id('Passwd')
# passwordElem.send_keys('MyPassword')
# signinButton = browser.find_element_by_id('signIn')
# signinButton.click()