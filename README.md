## Scrapy爬取小程序教程

爬取教程内的文章标题、作者、发表日期和内容



## Create

```python
scrapy startproject wxapp

cd wxapp

scrapy genspider -t crawl wxapp_spider "wxapp-union.com"
```

> 创建好之后在根目录新建`start.py`文件，方便运行爬虫和调试



## Preview

