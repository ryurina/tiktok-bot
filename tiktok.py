from time import sleep
from selenium import webdriver
from getpass import getpass

class Bot:
	def __init__(self, username, password): 
		self.browser = webdriver.Chrome(executable_path="chromedriver.exe")
		self.browser.implicitly_wait(5)
		self.browser.get('https://www.tiktok.com/login/?redirect_url=https%3A%2F%2Fwww.tiktok.com%2Ftrending%2F%3Flang%3Dfr&lang=fr&enter_method=top_bar')
		sleep(2)
		self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]').click()
		sleep(2)

		# switch window
		root = self.browser.window_handles[0]
		self.browser.switch_to_window(self.browser.window_handles[1]) # switch to popup facebook login window

		# login with facebook
		self.browser.find_element_by_xpath('//*[@id="email"]').send_keys(username)
		self.browser.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
		self.browser.find_element_by_xpath('//*[@id="u_0_0"]').click()
		sleep(10)

		self.browser.switch_to_window(root) #switch to first window

		for i in range(1, 100):
			sleep(2)
			self.browser.get("https://www.tiktok.com/trending/?lang=fr&loginType=facebook")
			sleep(2)
			self.browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div/div/main/div/div[{}]/div/div/div/a/div/div/div'.format(i)).click()
			sleep(2)
			self.browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div/div/div/main/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]/span').click()
			self.browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/div/div/main/div[2]/div[2]/div[1]/div/button').click()



username = input("Username: ")  # Enter your facebook username
password = getpass("password: ") # Enter your facebook password

Bot(username, password)

sleep(50)
