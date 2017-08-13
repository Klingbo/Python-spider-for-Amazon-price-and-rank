from Urlmanager import UrlManager
from Htmldownloader import HtmlDownloader


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.download = HtmlDownloader()

    def crawl(self, Afile, Bfile):
        rank = open(Bfile, 'a')
        self.manager.get_urls(Afile)
        while self.manager.old_url_size() < 2:
            new_url = self.manager.get_new_url()
            sales_rank = self.download.download(new_url)[0]
            print(sales_rank, file=rank)
            print('已经抓取了%s个rank' % self.manager.old_url_size())


if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl('url.txt', 'rank.txt')
