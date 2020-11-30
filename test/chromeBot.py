from selenium import webdriver

#Purchased_Made = False;


driver = webdriver.Chrome()
driver.get("https://www.bestbuy.com/site/msi-optix-g27c5-27-led-monitor-black/6425570.p?skuId=6425570")

element = driver.find_element_by_css_selector("input.btn")
element.click()

## Now iterate through them and check for our desired match
