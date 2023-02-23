import hashlib
import os
import pprint
import re
from multiprocessing.dummy import Pool

import requests

url = 'https://4m3p.com/web/abcdefg.ashx?v=1676979456017'

headers = {
    'cookie': 'footer_bar_sindex=1; ASP.NET_SessionId=3ruz5np1wxh3nxyp3e4rdrim; '
              'Hm_lvt_9f18188cf6ca76964151d7b599951471=1676979419; '
              'Hm_lvt_7061c4deafdcbf84d71ddd292445ef38=1676979419; '
              'Hm_lpvt_9f18188cf6ca76964151d7b599951471=1676979429; '
              'Hm_lpvt_7061c4deafdcbf84d71ddd292445ef38=1676979429',
    'authority': '4m3p.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
data = 'action=getvideos&vtype=3026&pageindex=1&pagesize=30&tags=全部&sortindex=1'.encode('utf-8')
response = requests.post(url, data=data, json=None, headers=headers)
page_count = response.json()['pagecount']
url_list = []
name_list = []

for page in range(1, 5):
    params = f'action=getvideos&vtype=3026&pageindex={page}&pagesize=30&tags=全部&sortindex=1'
    data = params.encode('utf-8')
    response = requests.post(url, data=data, json=None, headers=headers)
    # pprint.pprint(response.json())

    video_list = response.json()['videos']
    for video in video_list:
        title = video['title']
        download_url = video['downvurl']
        match_obj_1 = re.search(r'JUL', title, re.M | re.I)
        match_obj_2 = re.search(r'ADN', title, re.M | re.I)
        if match_obj_1 or match_obj_2:
            name_list.append(title)
            url_list.append(f'https://xunlei.grr4d46c.com/changpian{download_url}')
            continue

dir_path = os.getcwd() + '/videos/'
if not os.path.exists(dir_path):
    os.mkdir(dir_path)


def downloadVideo(down_url):
    down_response = requests.get(down_url, stream=True)
    if down_response.status_code == 200:
        name = down_url.split('/')[-1]
        if os.path.exists(dir_path + name):
            print(name + ' 文件已存在')
            return
        else:
            print('正在下载：' + name)
        # name = hashlib.md5(download_url.encode(encoding='utf-8')).hexdigest()

        with open(dir_path + name, 'wb') as file:
            for chunk in down_response.iter_content(chunk_size=512):
                if chunk:
                    file.write(chunk)


pool = Pool(5)
pool.map(downloadVideo, url_list)
# url = response.json()['videos'][0]['downvurl']
# title = response.json()['videos'][0]['title']
# pprint.pprint(response.json())
# print((title, url))

# download_url = 'https://xunlei.grr4d46c.com/changpian' + url
#
# response = requests.get(download_url, stream=True)
# if not os.path.exists(dir_path):
#     os.mkdir(dir_path)
# if response.status_code == 200:
#     # print('正在保存：' + title)
#     name = hashlib.md5(url.encode(encoding='utf-8')).hexdigest()
#     with open(dir_path + name + '.mp4', 'wb') as file:
#         for chunk in response.iter_content(chunk_size=512):
#             if chunk:
#                 file.write(chunk)
