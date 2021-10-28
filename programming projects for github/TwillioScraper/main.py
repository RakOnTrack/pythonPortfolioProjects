from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome_driver_path = '/Users/ericrak/Desktop/100DaysOfCode/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# driver.get('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.91432417822266%2C%22east%22%3A-122.11094893408203%2C%22south%22%3A37.677805844354516%2C%22north%22%3A37.91708111010459%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D')
driver.get('https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.60263210887238%2C%22east%22%3A-78.33670193309113%2C%22south%22%3A42.96561561829618%2C%22north%22%3A44.10646905913619%7D%2C%22mapZoom%22%3A9%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A699942%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A1700%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D')

sleep(1)
modal = driver.find_element_by_id('search-page-list-container')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

sleep(1)


addresses = driver.find_elements_by_css_selector('.list-card-addr')
prices = driver.find_elements_by_css_selector('.list-card-price')
links = driver.find_elements_by_css_selector('.list-card-link')

print(addresses)
print(prices)
print(links)


#
addresses_list = []
prices_list = []
links_list = []

# print(postings)
for i in range(len(addresses)):
    addresses_list.append(addresses[i].text)
    prices_list.append(prices[i].text)
    links_list.append(links[i].get_attribute('href'))
    print('\n')

print(addresses_list)
print(prices_list)
print(links_list)

print(addresses_list[0])
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScsFGiqJD9igTWigLzd1UM3dSqH8K6UCCk4t__Q6wvNfBBcqw/viewform?usp=sf_link'

driver.get(form_url)

sleep(1)





for i in range(len(addresses)):
    address_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    try:
        address_input.send_keys(addresses_list[i])
        price_input.send_keys(prices_list[i])
        link_input.send_keys(links_list[i])
    except:
        pass
    submit.click()
    sleep(1)
    submit_another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')

    submit_another_response.click()
    sleep(1)


