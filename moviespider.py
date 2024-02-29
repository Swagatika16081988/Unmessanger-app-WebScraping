import scrapy


class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    def parse(self, response):
        movies = response.css('div.ipc-metadata-list-summary-item__c')

        for movie in movies:
            yield {
                
                    'Title':movie.css('h3.ipc-title__text').getall(),
                    'Year':movie.css('div div span::text').getall(),
                    'Ratings':movie.css('.ipc-rating-star--base::text').getall()
                  }
       