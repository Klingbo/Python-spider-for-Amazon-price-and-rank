import re
import requests


class HtmlDownloader(object):

    def download(self, url):
        header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                                "(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
        page_url = requests.get(url, headers=header)
        page = page_url.text
        sales_rank = re.findall('<span>#(.*?) in Automotive', page, re.S)
        return sales_rank
