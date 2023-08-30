from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Ui_test import *



url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
selectors = {'ClLog': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
             'MenLog': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
             'Hermoine': '#userSelect > option:nth-child(2)',
             'Harry': '#userSelect > option:nth-child(3)',
             'Ron': '#userSelect > option:nth-child(4)',
             'Albus': '#userSelect > option:nth-child(5)',
             'Neville': '#userSelect > option:nth-child(6)',
             'Login btm': 'body > div > div > div.ng-scope > div > form > button',
             'Transactions': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
             'Deposit': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
             'Deposit text box': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
             'Deposit Btm': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
             'Withdrawl': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
             'account number': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(1)',
             'Balance': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)',
             'Manager add': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)',
             'Manager open': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(2)',
             'Manage costumers': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
             'First name text box': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input',
             'Last name text box': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input',
             'Post code text box': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input',
             'Add customer Btm': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button',
             'Customer table': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table',
             'acount 1004': '#accountSelect > option:nth-child(1)',
             'acount 1005': '#accountSelect > option:nth-child(2)',
             'acount 1006': '#accountSelect > option:nth-child(3)',
             'transections1004': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
             'transections1005': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
             'transections1006': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
             'back btm': 'body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)',
             'table1004': 'body > div > div > div.ng-scope > div > div:nth-child(2) > table',
             'account 1002': '#accountSelect > option:nth-child(2)',
             'transections1002': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
             'table her 1002': 'body > div > div > div.ng-scope > div > div:nth-child(2) > table',
             'back btm1004': 'body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)',
             'back btm1005': 'body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)',
             'back btm1006': 'body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)'
             }



# driver = get_driver(url)


# 3
def add_client(driver):
    driver.get(url)
    time.sleep(2)
    manager_log = driver.find_element(By.CSS_SELECTOR, selectors['MenLog'])
    manager_log.click()
    time.sleep(1)
    add_customer = driver.find_element(By.CSS_SELECTOR, selectors['Manager add'])
    add_customer.click()
    time.sleep(1)
    first_name = driver.find_element(By.CSS_SELECTOR, selectors['First name text box'])
    first_name.send_keys('Draco')
    time.sleep(1)
    last_name = driver.find_element(By.CSS_SELECTOR, selectors['Last name text box'])
    last_name.send_keys('Malfoy')
    time.sleep(1)
    post_code = driver.find_element(By.CSS_SELECTOR, selectors['Post code text box'])
    post_code.send_keys('E66655')
    time.sleep(1)
    add_customer_2 = driver.find_element(By.CSS_SELECTOR, selectors['Add customer Btm'])
    add_customer_2.click()
    driver.switch_to.alert.accept()
    time.sleep(1)
    manage_customers = driver.find_element(By.CSS_SELECTOR, selectors['Manage costumers'])
    manage_customers.click()
    time.sleep(1)
    customer_table = driver.find_element(By.CSS_SELECTOR, selectors['Customer table'])
    if 'Draco' in customer_table.text:
        return customer_table
    else:
        return 'Error'



# 7
def rows_counter(driver):
    driver.get(url)
    time.sleep(1)
    costumer_log = driver.find_element(By.CSS_SELECTOR, selectors['ClLog'])
    costumer_log.click()
    time.sleep(1)
    Harry = driver.find_element(By.CSS_SELECTOR, selectors['Harry'])
    Harry.click()
    customer_log_btm = driver.find_element(By.CSS_SELECTOR, selectors['Login btm'])
    customer_log_btm.click()
    time.sleep(1)
    transactions1004 = driver.find_element(By.CSS_SELECTOR, selectors['transections1004'])
    transactions1004.click()
    time.sleep(1)
    rows = driver.find_element(By.TAG_NAME, 'tbody')
    counter = 0
    for t in rows.text:
        if t.count('t') == 1:
            counter += 1
    back_btm1004 = driver.find_element(By.CSS_SELECTOR, selectors['back btm1004'])
    back_btm1004.click()
    time.sleep(1)
    account_105 = driver.find_element(By.CSS_SELECTOR, selectors['acount 1005'])
    account_105.click()
    transactions1005 = driver.find_element(By.CSS_SELECTOR, selectors['transections1005'])
    transactions1005.click()
    time.sleep(1)
    rows = driver.find_element(By.TAG_NAME, 'tbody')
    for t in rows.text:
        if t.count('t') == 1:
            counter += 1
    back_btm1005 = driver.find_element(By.CSS_SELECTOR, selectors['back btm1005'])
    back_btm1005.click()
    time.sleep(1)
    account_106 = driver.find_element(By.CSS_SELECTOR, selectors['acount 1006'])
    account_106.click()
    transactions1006 = driver.find_element(By.CSS_SELECTOR, selectors['transections1006'])
    transactions1006.click()
    time.sleep(1)
    rows = driver.find_element(By.TAG_NAME, 'tbody')
    for t in rows.text:
        if t.count('t') == 1:
            counter += 1
    if counter == 1:
        return 'Harry only have 1 transaction'
    else:
        return 'Error'



# 10
def no_fisrt_name(driver):
    driver.get(url)
    time.sleep(1)
    manager_log = driver.find_element(By.CSS_SELECTOR, selectors['MenLog'])
    manager_log.click()
    time.sleep(1)
    add_customer = driver.find_element(By.CSS_SELECTOR, selectors['Manager add'])
    add_customer.click()
    time.sleep(1)
    last_name = driver.find_element(By.CSS_SELECTOR, selectors['Last name text box'])
    last_name.send_keys('Malfoy')
    time.sleep(1)
    post_code = driver.find_element(By.CSS_SELECTOR, selectors['Post code text box'])
    post_code.send_keys('E66655')
    time.sleep(1)
    add_customer_2 = driver.find_element(By.CSS_SELECTOR, selectors['Add customer Btm'])
    add_customer_2.click()
    time.sleep(3)
    manage_customers = driver.find_element(By.CSS_SELECTOR, selectors['Manage costumers'])
    manage_customers.click()
    time.sleep(1)
    customer_table = driver.find_element(By.CSS_SELECTOR, selectors['Customer table'])
    if 'Malfoy' in customer_table.text:
        return 'Error'
    else:
        return "The website won't add a new client without a first name"


# 12
def letters_no_numbers(driver):
    driver.get(url)
    time.sleep(1)
    costumer_log = driver.find_element(By.CSS_SELECTOR, selectors['ClLog'])
    costumer_log.click()
    time.sleep(1)
    Hermoine = driver.find_element(By.CSS_SELECTOR, selectors['Hermoine'])
    Hermoine.click()
    customer_log_btm = driver.find_element(By.CSS_SELECTOR, selectors['Login btm'])
    customer_log_btm.click()
    time.sleep(1)
    account_1002 = driver.find_element(By.CSS_SELECTOR, selectors['account 1002'])
    account_1002.click()
    deposit_btm = driver.find_element(By.CSS_SELECTOR, selectors['Deposit'])
    deposit_btm.click()
    time.sleep(1)
    invalid_input = 'abc'
    deposit_text = driver.find_element(By.CSS_SELECTOR, selectors['Deposit text box'])
    deposit_text.send_keys(invalid_input)
    time.sleep(1)
    deposit_btm2 = driver.find_element(By.CSS_SELECTOR, selectors['Deposit Btm'])
    deposit_btm2.click()
    time.sleep(1)
    trans1002 = driver.find_element(By.CSS_SELECTOR, selectors['transections1002'])
    trans1002.click()
    time.sleep(1)
    table_her_1002 = driver.find_element(By.CSS_SELECTOR, selectors['table her 1002'])
    if invalid_input in table_her_1002.text:
         return 'Error'
    else:
         return table_her_1002



# driver.get(url)
# costumer_log = driver.find_element(By.CSS_SELECTOR, selectors['ClLog'])
# costumer_log.click()
# time.sleep(1)
# Hermoine = driver.find_element(By.CSS_SELECTOR, selectors['Hermoine'])
# Hermoine.click()
# customer_log_btm = driver.find_element(By.CSS_SELECTOR, selectors['Login btm'])
# customer_log_btm.click()
# time.sleep(1)
# trans1001 = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)')
# trans1001.click()
# time.sleep(1)
# rows = driver.find_element(By.TAG_NAME,'tbody')
# print(rows.text)
# counter = 0
# for t in rows.text:
#     if t.count('t') == 1:
#         counter += 1
# if counter == 1:
#     print('yay')
# else:
#     print('booo')
