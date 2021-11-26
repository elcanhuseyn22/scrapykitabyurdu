import scrapy


class QuotesSpider(scrapy.Spider):
    name = "books"
    book_count = 1
    page_count = 0
    f = open("books.txt","a",encoding="UTF-8")
    start_urls = [
        'https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=16&filter_in_stock=1&filter_in_stock=1&page=1'

    ]
        
    

    def parse(self, response):
        book_names = response.css("div.name.ellipsis a span::text").getall()
        book_authors = response.css("div.author span a span::text").getall()
        book_publishers = response.css("div.publisher span a span::text").getall()

        i=0

        while i<len(book_names):
            #scrapy crawl  books -o books.json
            """yield {
                "name":book_names[i],
                "author":book_authors[i],
                "publisher":book_publishers[i]
            }"""
            #scrapy crawl books
            self.f.write("№: "+str(self.book_count)+"\n")
            self.f.write("Book name:"+book_names[i]+"\n")
            self.f.write("Author   :"+book_authors[i]+"\n")
            self.f.write("Publisher:"+book_publishers[i]+"\n")
            self.f.write("------------------------\n")
            self.book_count+=1
            i+=1

        next_url = response.css("a.next::attr(href)").get()
        self.page_count+=1
        
        if next_url is not None and self.page_count != 5:
            yield scrapy.Request(url= next_url,callback=self.parse)
        else:
            f.close()