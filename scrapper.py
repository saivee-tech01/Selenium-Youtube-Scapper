from selenium import webdriver
from selenium.webdriver.chrome.options import Options
YOUTUBE_TRENDING_URL="https://www.youtube.com/feed/trending"
chrome_options=Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(options=chrome_options)
driver.get(YOUTUBE_TRENDING_URL)
print(driver.title)