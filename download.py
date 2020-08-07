from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage=directory, type="face", size="medium")
google_crawler.crawl(keyword="shak", max_num=1)
