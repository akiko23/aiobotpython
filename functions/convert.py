import time

import requests
from config import *
from bs4 import BeautifulSoup
from selenium import webdriver

MAIN_URL = 'https://finance.rambler.ru/calculators/converter/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}


def convert(v1, v2, col):
    response = requests.get(f"{MAIN_URL}{col}-{v1}-{v2}/")
    soup = BeautifulSoup(response.text, "html.parser")

    return float(soup.find_all("div", class_="converter-display__value")[1].text)


def translate_ru_to_france(text):
    word_list = []
    url = 'https://translate.yandex.ru/?lang=ru-en'

    driver = webdriver.Chrome(
        'C:\\Users\\hdhrh\\Desktop\\pythonProject\\MainApiProject\\ChromeDriver\\chromedriver.exe')

    try:
        driver.get(url=url)
        time.sleep(10)

        inp = driver.find_element_by_xpath('//*[@id="fakeArea"]')
        inp.send_keys(text)
        time.sleep(5)

        result = driver.find_elements_by_class_name('translation-word')

        for word in list(result):
            word_list.append(word.text)

        time.sleep(2)

        str_res = ''.join([f for f in word_list])

        return str_res

    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
