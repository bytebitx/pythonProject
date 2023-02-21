import hashlib
import os
import re

import parsel
import requests

url = 'https://so.toutiao.com/search?dvpf=pc&source=sug&keyword=%E8%A1%97%E6%8B%8D%E7%BE%8E%E5%A5%B3%E9%AB%98%E9%A2%9C%E5%80%BC%E5%A5%B3%E7%A5%9E'
headers = {
    'cookie': 'ttwid=1%7Cr16TK1rMYyZQWnQMtTxJSe764U7DYCnaMtdcotGOu3c%7C1668046192%7C3e33cc3ce177bfd6b83f1512d46bb6f89f6b6afcf1b1b4051d0e37063430b2be; tt_webid=7164203797182481956; _ga=GA1.1.1394716138.1676944185; __ac_signature=_02B4Z6wo00f01BqgsfAAAIDDjnbq.pZoD7AagLVAAGVi99; __ac_referer=https://www.toutiao.com/; _tea_utm_cache_4916=undefined; _S_DPR=2; _S_IPAD=0; MONITOR_WEB_ID=7164203797182481956; _S_WIN_WH=1512_749; msToken=v4a8BPWalY-1JH9Hn0eEN7MXE0c1EDvkbHJ-xLTCrjPt8wevokeQ9x6D66UF9VOAGeCYNjj4md3Lxm_osHOqcngU5ygqwrJgqD4dRkQUkDM=; _ga_QEHZPBE5HH=GS1.1.1676955111.2.1.1676955170.0.0.0',
    'Host': 'so.toutiao.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
# print(response.text)
# selector = parsel.Selector(response.text)
# type_list = selector.xpath('//div[@class="cs-view cs-view-block cs-card-content"]/a/@href').getall()
# for page in type_list:
#     print(page)
result_id = re.findall('self_article&quot;,&quot;(.*?),&quot;result_level&quot;', response.text)
result_id_list = re.sub('search_result_id&quot;:&quot;', '', ''.join(result_id))
id_list_str = re.sub('&quot', '', ''.join(result_id_list))
id_list = id_list_str.split(';')

headers = {
    'cookie': 'ttcid=210c63e887bd4d5ea9fd032d02be20e925; csrftoken=7e9e8912f2ac698c32343062bef34769; ttwid=1%7Cr16TK1rMYyZQWnQMtTxJSe764U7DYCnaMtdcotGOu3c%7C1668046192%7C3e33cc3ce177bfd6b83f1512d46bb6f89f6b6afcf1b1b4051d0e37063430b2be; tt_webid=7164203797182481956; local_city_cache=%E6%B7%B1%E5%9C%B3; _ga=GA1.1.1394716138.1676944185; s_v_web_id=verify_ledl9qnj_YIyL7t6l_wrVP_4tjU_98aZ_NfzdnNqed7w7; _S_DPR=2; _S_IPAD=0; _S_WIN_WH=1512_749; _ga_QEHZPBE5HH=GS1.1.1676955111.2.1.1676959124.0.0.0; msToken=5jwY4hNnBecgtp2xnI2oF977nKe-1WxJQUiym74pet6c-kwrrL7j6RJ-qKtsBqiIEWUq6pEgYO7efKRRt-uoWdc1hFwqs6v5L_7-S7SDawc=; tt_scid=2tt-mAlHOvSkhpUgsD1XXiPm3-EYHscr1bk0.vTgNPFY9T42jz-If0pwzZ-3LB0X4365',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

dir_path = os.getcwd() + '/imgs/'

for page_id in id_list:
    if page_id:
        url = f'https://www.toutiao.com/article/{page_id}'
        # print(url)
        page_response = requests.get(url, headers=headers).text
        # print(page_response)
        selector = parsel.Selector(page_response)
        src_list = selector.xpath('//div[@class="pgc-img"]/img/@src').getall()
        print(src_list)
        for url in src_list:
            response = requests.get(url, stream=True)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            if response.status_code == 200:
                # print('正在保存：' + title)
                name = hashlib.md5(url.encode(encoding='utf-8')).hexdigest()
                with open(dir_path + name + '.jpg', 'wb') as file:
                    for chunk in response.iter_content(chunk_size=512):
                        if chunk:
                            file.write(chunk)
