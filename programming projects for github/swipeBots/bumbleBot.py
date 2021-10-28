from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = 'eric_rak@hotmail.com'

FB_PASSWORD = 'Allie110!'

# chrome_driver_path = '../chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://bumble.com/get-started")

sleep(2)

login_fb = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')
login_fb.click()
sleep(4)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_id('email')
password = driver.find_element_by_id('pass')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
sleep(10)


for n in range(1000):
    print(n)
    try:
        sleep(1)
        # like_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span')
        like_button = driver.find_element_by_css_selector('.encounters-action--like ')
        # like_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
        # like_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span')
        like_button.click()
    except:
        #if it is a match, click continue Bumbling
        try:
            continue_bumbling = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div')
            continue_bumbling.click()
            print('Match!')
        except:
        # exit_super_swipe = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div/div[2]/div/div[2]')
        # exit_super_swipe.click()
        # sleep(10)
            pass
