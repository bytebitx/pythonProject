import time

import parsel
import requests

for page in range(0, 101, 10):
    # time.sleep(2)
    url = 'https://maoyan.com/board/4?offset={}'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Cookie': '__mta=20345351.1670903159717.1670903413872.1670903436333.5; uuid_n_v=v1; uuid=A8065B807A9811ED82C293D7E110319C9B09821067E1411AB6F4EC82889E1869; _csrf=916b8446658bd722f56f2c092eaae35ea3cd3689ef950542e202b39ddfe7c91e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1670903160; _lxsdk_cuid=1850996db5dc8-07670e36da28-26021151-1fa400-1850996db5d67; _lxsdk=A8065B807A9811ED82C293D7E110319C9B09821067E1411AB6F4EC82889E1869; __mta=213622443.1670903327420.1670903417327.1670903424017.4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1670903436; _lxsdk_s=1850996db5e-8b2-284-88a%7C%7C18',
        'Host': 'www.maoyan.com',
        'Referer': 'https://www.maoyan.com/films/1200486'
    }
    response = requests.get(url, headers=headers)
    selector = parsel.Selector(response.text)
    li_s = selector.css('.board-wrapper')
    for item in li_s:
        name = item.css('.name a::text').get()
        print(name)