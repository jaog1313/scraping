from selenium impor webdriver
from time import sleep


class myScrapper:
    def __init__(self):
        #Obtener el user agent
        user_agent = ""

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent?{user_agent}')
        self.options.add_argument("--window-size=1920,1000")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--allow-running-insecure-content")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(
			executable_path="",
			options=self.options)
myScrapper()
