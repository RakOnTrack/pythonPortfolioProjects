from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = 'eric_rak@hotmail.com'
FB_PASSWORD = 'Allie110!'

chrome_driver_path = '/Users/ericrak/Desktop/100DaysOfCode/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="u-648818393"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
# login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="u1917767827"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
try:
    meet_people_nearby = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[1]')
    meet_people_nearby.click()
except:
    pass
sleep(1)
try:
    notifications_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[2]')
    notifications_button.click()
except:
    pass
try:
    cookies = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[2]/div/div/div[1]/button')
    cookies.click()
except:
    pass

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()
        try:
            while True:
                sleep(.5)
                try:
                    like_button.click()
                    # dislike_button.click()
                except:
                    #if its a match
                    try:
                        its_a_match_exit = driver.find_element_by_xpath(
                            '//*[@id="q-1095164872"]/div/div/div/div/div[4]/button')
                        its_a_match_exit.click()
                    except:
                        #if it wants you to superlike
                        try:
                            super_like_no_thanks = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/button[2]/span')
                            super_like_no_thanks.click()
                        except:
                            #if it asks to up tinder on homescreen
                            try:
                                add_to_homescreen_not_interested = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div[2]/button[2]/span')
                                add_to_homescreen_not_interested.click()
                            except:
                                pass

        except:
            pass
    except:
        print('didnt work')
        pass



    # #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    # except ElementClickInterceptedException:
    #     try:
    #         match_popup = driver.find_element_by_css_selector(".itsAMatch a")
    #         match_popup.click()
    #
    #     #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
    #     except NoSuchElementException:
    #         sleep(2)

driver.quit()