from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from Selenium_config import (
    get_chrome_web_driver,
    get_chrome_options,
    set_chrome_incognito,
    set_chrome_fullscreen
)

NAME = "NoobFromUA"
URL = "https://www.youtube.com/"

class YouTubeAPI:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        options = get_chrome_options()
        set_chrome_incognito(options)
        set_chrome_fullscreen(options)
        self.driver = get_chrome_web_driver(options)
        self.repositorie = []

    def run(self):
        self.driver.get(self.url)
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span').click()

        self.driver.implicitly_wait(5)
        search = self.driver.find_element_by_xpath('//*[@id="search"]')
        search.send_keys(self.name)
        search.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="contents"]/ytd-channel-renderer').click()

        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div').click()

        self.find_videos()

        for video in self.repositorie:
            print(f'\n{video[6:]}')

        self.tearDown()

    def find_videos(self):
        try:
            for i in range(1, 6):
                time.sleep(1)
                new_ones = self.driver.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[' + str(i) + ']')
                self.repositorie.append(new_ones.text)

        except NoSuchElementException as e:
            print(e)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    obj = YouTubeAPI(NAME, URL)
    obj.run()

