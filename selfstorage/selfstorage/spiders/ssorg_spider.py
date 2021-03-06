import scrapy

class ssorg_spider(scrapy.Spider):
    name = 'ssorg_spider'
    start_urls = ['http://www.selfstorage.org/cvweb/cgi-bin/utilities.dll/CustomList?O.ORGNAME=~~&O.STATECD=AZ&RANGE=0/25&O.ISMEMBERFLG=Y&O.NOWEBFLG=%3C%3EY&O.STATUSSTT=Active&SHOWSQL=N&WHP=dir_facility.htm&WBP=dir_facility_list.htm&SORT=ORGNAME&QNAME=FACILITYNODISTANCE']


    def parse(self, response):
        outer_div = response.xpath('//*[@id="content"]/div[2]/div')
        for div in outer_div.xpath('.//div'):
            yield {
                    div.xpath('.//p[1]/a/text()').extract_first(): div.xpath('.//p[2]/text()').extract_first()
            }

    #TODO: write the response lookup for this, look at the link -> change range from 0 -> 1 (?) + page_num * 25



if __name__ == '__main__':
    main()
