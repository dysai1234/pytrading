def login_kite(username,password ,pin):
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.get('https://kite.zerodha.com')
    user_name_ele=driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[2]/input')
    password_ele= driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[3]/input')
    submit_ele=driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[4]/button')

    user_name_ele.send_keys(username)
    password_ele.send_keys(password)
    submit_ele.click()
    time.sleep(1)# you can use explicit wait also or expected contition also
    
    pin_ele=driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[2]/div/input')
    continue_ele=driver.find_element_by_xpath('//*[@id="container"]/div/div/div/form/div[3]/button')

    pin_ele.send_keys(pin)
    continue_ele.click()
    return driver

## this function returns the value of brokerage calculator value if there is no it opens and returns it
def search_for_brokerage_calculator(driver='null'):
    try:
        for tab in driver.window_handles:
            driver.switch_to_window(tab)
            if (driver.title==''):
                driver.get('https://zerodha.com/brokerage-calculator#tab-equities')
                return driver
                
            elif (driver.title == 'Brokerage calculator'):
                return tab
            
        driver.execute_script("window.open('');")
        driver.switch_to_window(driver.window_handles[-1])
        driver.get('https://zerodha.com/brokerage-calculator#tab-equities')
        return driver.window_handles[-1]
    except:
        from selenium import webdriver
        driver = webdriver.Chrome()
        return search_for_brokerage_calculator(driver)
    
    
def return_brokerage_calculator(driver='null'):
    try:
        for tab in driver.window_handles:
            driver.switch_to_window(tab)
            if (driver.title==''):
                driver.get('https://zerodha.com/brokerage-calculator#tab-equities')
                return driver
                
            elif (driver.title == 'Brokerage calculator'):
                return tab
            
        driver.execute_script("window.open('');")
        driver.switch_to_window(driver.window_handles[-1])
        driver.get('https://zerodha.com/brokerage-calculator#tab-equities')
        return driver.window_handles[-1]
    except:
        from selenium import webdriver
        driver = webdriver.Chrome()
        return return_brokerage_calculator(driver)

    
    
    
    
    
# net profit_loss function


def calculate_net_profit_loss(buy_price,sell_price,quantity=1,exchange_type="NSE",driver='ntg'):
    brokerage_window = 0
    for tab in driver.window_handles:
        driver.switch_to_window(tab)
        if (driver.title==''):
            driver.get('https://zerodha.com/brokerage-calculator#tab-equities')
            brokerage_window =tab
            break
        elif(driver.title == 'Brokerage calculator'):
            brokerage_window =tab
            break
    
    if (brokerage_window ==0):
        driver.execute_script("window.open('');")
        driver.switch_to_window(driver.window_handles[-1])
        driver.get('https://zerodha.com/brokerage-calculator#tab-equities')
        brokerage_window =driver.window_handles[-1]
        
    # for now we opened brokerage calculator tab
    # now we calculate the net profit loss
    
    buy_input = driver.find_element_by_xpath('//*[@id="intraday-equity-calc"]/div[1]/div[1]/input')
    sell_input=driver.find_element_by_xpath('//*[@id="intraday-equity-calc"]/div[1]/div[2]/input')
    buy_input.clear()
    buy_input.send_keys(buy_price)
    sell_input.clear()  
    sell_input.send_keys(sell_price)
    quantity_input=driver.find_element_by_xpath('//*[@id="intraday-equity-calc"]/div[1]/div[3]/input')
    quantity_input.clear()
    quantity_input.send_keys(quantity)
    Bse_path=driver.find_element_by_xpath('//*[@id="radio12"]')
    Nse_path=driver.find_element_by_xpath('//*[@id="radio11"]')
    if exchange_type =='NSE':
        Nse_path.click()
    elif exchange_type =='BSE':
        Bse_path.click()
    net_profit_element=driver.find_element_by_xpath('/html/body/div/main/section[2]/div/div/div[1]/div/div[{}]/div[12]/span'.format(equity))
    net_profit = net_profit_element.text
    #driver.close()
    return net_profit
    
    
        
        