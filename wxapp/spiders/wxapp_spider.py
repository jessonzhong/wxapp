# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.*mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.*article-.*-1\.html'), callback='parse_detail', follow=False)
    )

    def parse_detail(self, response):
        item = {}
        title = response.xpath("//h1[@class='ph']/text()").get()
        author_p = response.xpath("//p[@class='author']")
        author = author_p.xpath("./a/text()").get()
        pub_time = author_p.xpath("./span/text()").get()
        article_content_div = response.xpath("//td[@id='article_content']/div/text()").extract()
        if article_content_div:
            article_content = article_content_div
        else:
            article_content = response.xpath("//td[@id='article_content']//text()").extract()

        content = ''.join(article_content).strip()
        item = WxappItem(title=title, author=author, pub_time=pub_time, content=content)
        return item
