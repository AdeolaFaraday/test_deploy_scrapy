# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from shutil import which


class TestdeploySpider(scrapy.Spider):
    name = 'testdeploy'
    allowed_domains = ['www.fzmovies.net']
    start_urls = ['http://www.fzmovies.net/']

    def parse(self, response):
        chrome_options = Options()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get("https://www.fzmovies.net/")

        obj = driver.switch_to.alert

        # Or Dismiss the Alert using
        if obj:
            obj.dismiss()

        yield {
            'message': 'obj.text'
        }
