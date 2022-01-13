# -*- coding: utf-8 -*-
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
        chrome_options.add_argument('--headless')
        chrome_path = which("chromedriver")
        driver = webdriver.Chrome(
            executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get("https://www.fzmovies.net/")

        obj = driver.switch_to.alert

        # Or Dismiss the Alert using
        if obj:
            obj.dismiss()

        yield {
            'message': 'obj.text'
        }
