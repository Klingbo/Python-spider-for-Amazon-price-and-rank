import requests
from bs4 import BeautifulSoup


for i in range(0, 675, 25):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Connection': 'keep-alive'}
    url = 'https://www.amazon.com/gp/product/portal/desktop/compatibility-chart/B000CF3WFI?ie=UTF8&i={}'.format(i)
    page_url = requests.get(url, headers=head)
    page_get = page_url.text
    page_text = BeautifulSoup(page_get, 'lxml')
    fitment_1 = page_text.find_all('tr', {'class': 'fitment listRowEven'})
    fitment_2 = page_text.find_all('tr', {'class': 'fitment listRowOdd'})
    for each_tag_1 in fitment_1:
        td_text_1 = each_tag_1.find_all('td')
        for x in range(10):
            fx = open('fitment/{}.txt'.format(x), 'a')
            try:
                print(td_text_1[x].string, file=fx)
            except IndexError:
                print(None, file=fx)
    for each_tag_2 in fitment_2:
        td_text_2 = each_tag_2.find_all('td')
        for y in range(10):
            fy = open('fitment/{}.txt'.format(y), 'a')
            try:
                print(td_text_2[y].string, file=fy)
            except IndexError:
                print(None, file=fy)
