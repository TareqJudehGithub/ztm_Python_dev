from selenium import webdriver

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
  


if __name__ == "__main__":
  
  print(chrome_auto())
