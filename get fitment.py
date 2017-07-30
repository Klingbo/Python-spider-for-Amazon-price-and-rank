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
    fitment = page_text.find_all('tr', {'class': re.compile('fitment')})
    
    for each in fitment:
    td = each.find_all('td')
        for x in range(10):
            f = open('fitment/{}.txt'.format(x), 'a')
            try:
                print(td[x].string, file=f)
            except IndexError:
                print(None, file=fx)
   
