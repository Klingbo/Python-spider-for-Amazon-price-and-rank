# encoding = 'UTF-8'
import re
import requests

rank = open('sales_rank.txt', 'a')
with open('url_file.txt') as f:
    url = f.read().strip().split(',')
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
i = 0
for i in range(52):
    if i < 52:
        page_url = requests.get(url[i], headers=header)
        page = page_url.text
        sales_rank = re.findall('<span>#(.*?) in Automotive', page, re.S)[0]
        print(sales_rank, file=rank)
    else:
        print('Finish')
