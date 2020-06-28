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