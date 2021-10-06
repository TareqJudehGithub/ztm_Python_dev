"""
$ pip install selenium  

In case of Chrome Error after running Python script, add the following
lines to your .py script:
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])

  chrome_browser = webdriver.Chrome(
  "./chrome_driver/chromedriver.exe",
  options=options
  )

"""