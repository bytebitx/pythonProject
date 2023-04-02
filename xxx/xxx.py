import hashlib
import os
import re

import requests
from tqdm import tqdm

headers = {
    'authority': 'r5vg.com',
    'method': 'POST',
    'path': '/web/abcdefg.ashx?v=1680408554131',
    'scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '87',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'footer_bar_sindex=1; ASP.NET_SessionId=hnxshxskrx1pnk1l2w22n0cu; Hm_lvt_9f18188cf6ca76964151d7b599951471=1680408534; Hm_lvt_7061c4deafdcbf84d71ddd292445ef38=1680408534; Hm_lpvt_7061c4deafdcbf84d71ddd292445ef38=1680408543; Hm_lpvt_9f18188cf6ca76964151d7b599951471=1680408543',
    'origin': 'https://r5vg.com',
    'referer': 'https://r5vg.com/web/video-3026.html',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

url = "https://r5vg.com/web/abcdefg.ashx?v=1680408554131"
data = "action=getvideos&vtype=3026&pageindex=1&pagesize=12&tags=%E5%85%A8%E9%83%A8&sortindex=1"
response = requests.post(url=url, headers=headers, data=data)
yuming = response.json()['videos'][0]['yuming']
downvurl = response.json()['videos'][0]['downvurl']
vurl = response.json()['videos'][0]['vurl']
title = response.json()['videos'][0]['title']
m3u8_data = requests.get(yuming + vurl).text
ts_list = re.sub('#E.*', '', m3u8_data).split()
dir_path = os.getcwd() + '/videos/'
# print(ts_list)
index = vurl.rfind('/')
vurl[::index]

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

for ts in tqdm(ts_list):
    video_data = requests.get(
        yuming + "/m3u8/zhongwenzimu/202303/《看似贞洁的骚人妻，堕落出轨男下属》番号URE-068（人妻）/" + ts).content
    with open(dir_path + title + '.mp4', mode='ab') as file:
        file.write(video_data)
