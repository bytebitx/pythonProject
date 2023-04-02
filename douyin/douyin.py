import hashlib
import json
import os
import pprint
import re

import parsel
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_6ecae4b4661639f51be579865c839753=1680272717; Hm_lvt_5f160b35156601be1a20b4e58e497ecc=1680272718; Hm_lpvt_6ecae4b4661639f51be579865c839753=1680316450; Hm_lpvt_5f160b35156601be1a20b4e58e497ecc=1680316450',
    'Host': 'www.poco.cn',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

dir_path = os.getcwd() + '/imgs/'

response = requests.get("https://www.poco.cn/works/detail_id22140446", headers=headers)
print(response.text)

# print(re.search("http://v26-web.douyinvod.com", response.text).group())

# slashUStr = "https:\u002F\u002Fgossv.cfp.cn\u002Fvideos\u002Fmts_videos\u002Fpreview\u002FVCG42N1364165756.mp4"
# decodedUniChars = slashUStr.encode('utf-8').decode("unicode_escape")
# print("decodedUniChars=", decodedUniChars)
