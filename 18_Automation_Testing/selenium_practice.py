from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_browser = webdriver.Chrome(
  "./chrome_driver/chromedriver.exe",
  options=options
)

def chrome_auto():

  chrome_browser.get(
    "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
  )

  # check if head contents are match
  assert "Selenium Easy Demo" in chrome_browser.title

  # html body -  button class on webpage
  button_text = chrome_browser.find_element_by_class_name("btn-default")
  
  # get the button text using get_attribute("innerHTML")
  return button_text.get_attribute("innerHTML")
  

def test_submit():
  """testing form submission function"""

  chrome_browser.get(
    "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
  )
  button = chrome_browser.find_element_by_class_name("btn-default")
  # check "Show Message button text" in webpage source
  assert "Show Message" in chrome_browser.page_source
  # return button.get_attribute("innerHTML")

  # text field
  msg_field = chrome_browser.find_element_by_id("user-message")

  
  
  msg_field.clear()                       # clear user_input
  msg_field.send_keys("Hi, Tareq!!")      # type text in text field
  
  time.sleep(3)

  button.click()                   # click button

  # display user input
  return chrome_browser \
  .find_element_by_id("display") \
  .get_attribute("innerHTML")

  

def css_selector():
  """submit form using css_selector func"""
  chrome_browser.get(
    url="https://www.seleniumeasy.com/test/basic-first-form-demo.html"
  )

  button_text = chrome_browser\
    .find_element_by_css_selector("#get-input")\
    .find_element_by_css_selector(".btn")\
    .get_attribute("innerHTML")
  
  print(button_text)

  time.sleep(3)

  #chrome_browser.close()  # closes one chrome webpage (session)
  chrome_browser.quit()   # quits ALL chrome sessions
  return "Done!"
    

if __name__ == "__main__":
  # print(chrome_auto())
  # print(test_submit())
  print(css_selector())
