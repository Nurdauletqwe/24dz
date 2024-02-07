# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from openpyxl import Workbook

# wb = Workbook()
# ws = wb.active
# ws['A1'] = '#'
# ws['B1'] = 'Name'
# ws['C1'] = 'Desc'
# ws['D1'] = 'Price'

# chrome = webdriver.Chrome()

# chrome.get('https://www.saucedemo.com/')

# username = chrome.find_element(By.NAME, 'user-name')
# username.send_keys('standard_user')

# password = chrome.find_element(By.ID, 'password')
# password.send_keys('secret_sauce')

# btn = chrome.find_element(By.XPATH, '//*[@id="login-button"]')
# btn.click()


# names = chrome.find_elements(By.CLASS_NAME, 'inventory_item_name')
# descriptions = chrome.find_elements(By.CLASS_NAME, 'inventory_item_desc')
# prices = chrome.find_elements(By.CLASS_NAME, 'inventory_item_price')

# for i in range(6):
#     ws[f'A{2+i}'] = i+1
#     ws[f'B{2+i}'] = names[i].text
#     ws[f'C{2+i}'] = descriptions[i].text
#     ws[f'D{2+i}'] = prices[i].text

# wb.save('data.xlsx')

# time.sleep(20)