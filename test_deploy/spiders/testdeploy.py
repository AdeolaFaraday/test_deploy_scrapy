# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy import FormRequest


class TestdeploySpider(scrapy.Spider):
    name = 'testdeploy'
    allowed_domains = ['www.fzmovies.net']
    start_urls = ['http://www.fzmovies.net/']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            formid="searchname",
            formdata={
                "searchname": "life itself",
                "Search": "Search",
                "searchby": "Name",
                "category": "All",
            },
            callback=self.parse_film
        )

    def parse_film(self, response):
        movies_link = Selector(text=response.body.decode(
            "utf-8")).xpath("//div[@class='mainbox']/table/tr/td[2]/span/a//@href").get()
        yield response.follow(url=movies_link, callback=self.parse_first_page)

    def parse_first_page(self, response):
        next_link = Selector(text=response.body.decode(
            "utf-8")).xpath("//a[@id='downloadoptionslink2']//@href").get()
        print(next_link, 'next link hereeeeeeeee')
        yield response.follow(url=next_link, callback=self.parse_second_page)

    def parse_second_page(self, response):
        next_link = Selector(text=response.body.decode(
            "utf-8")).xpath("//a[@id='downloadlink']//@href").get()
        yield response.follow(url=next_link, callback=self.parse_third_page)

    def parse_third_page(self, response):
        download_link = Selector(text=response.body.decode(
            "utf-8")).xpath("//a[@id='dlink0']//@href").get()
        yield {
            'download_link': download_link
        }
