import hashlib
import json
import os
import re
import time
import urllib.parse

import execjs
import requests

album_url = 'https://web-api.poco.cn/v1_1/rank/get_homepage_recommend_list'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '393',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'web-api.poco.cn',
    'Origin': 'https://www.poco.cn',
    'Referer': 'https://www.poco.cn/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/110.0.0.0 Safari/537.36'
}

get_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # Accept-Encoding: gzip, deflate, br
    # Accept-Language: zh-CN,zh;q=0.9
    # Cache-Control: max-age=0
    # Connection: keep-alive
    'Cookie': 'Hm_lvt_6ecae4b4661639f51be579865c839753=1680272717; Hm_lvt_5f160b35156601be1a20b4e58e497ecc=1680272718; Hm_lpvt_6ecae4b4661639f51be579865c839753=1680356532; Hm_lpvt_5f160b35156601be1a20b4e58e497ecc=1680356532',
    'Host': 'www.poco.cn',
    # sec-ch-ua: "Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"
    # sec-ch-ua-mobile: ?0
    # sec-ch-ua-platform: "macOS"
    # Sec-Fetch-Dest: document
    # Sec-Fetch-Mode: navigate
    # Sec-Fetch-Site: none
    # Sec-Fetch-User: ?1
    # Upgrade-Insecure-Requests: 1
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}


def fetch_params(page_no, page_count):
    time_point = time.time()

    now = round(time_point * 1000)

    print(now)
    print(time_point)

    params = {
        "start": page_no,
        "length": page_count,
        "works_category": "1",
        "time_point": round(time_point)
    }

    with open('./k2.js', 'r', encoding='utf-8') as file:
        js_code = file.read()

    ctx = execjs.compile(js_code).call('call_js', page_no, page_count, round(time_point))
    # print(ctx)

    req_dic = {
        "version": "1.1.0",
        "app_name": "poco_photography_web",
        "os_type": "weixin",
        "is_enc": 0,
        "env": "prod",
        "ctime": now,
        "param": params,
        "sign_code": ctx
    }

    url = {
        'host_port': 'https://www.poco.cn'
    }

    data_params = 'req=' + urllib.parse.quote(json.dumps(req_dic)) + "&" + urllib.parse.urlencode(url)
    # print(data_params)
    return data_params


def download_img(url, title):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        dir_path = os.getcwd() + '/images/' + title + "/"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        # print('正在保存：' + title)
        name = hashlib.md5(url.encode(encoding='utf-8')).hexdigest()
        if os.path.exists(dir_path + name):
            print(name + ' 文件已存在')
            return
        with open(dir_path + name + '.jpg', 'wb') as file:
            for chunk in response.iter_content(chunk_size=512):
                if chunk:
                    file.write(chunk)


def fetch_image(url, title):
    response = requests.get(url, headers=get_headers)

    img_list = re.findall('<img data-src="(.*?)"/>', response.text)
    while '' in img_list:
        img_list.remove('')

    for url in img_list:
        download_img('https:' + url, title)


def fetch_images_count():
    data_params = fetch_params(page_no=0, page_count=20)
    response = requests.post(url=album_url, headers=headers, data=data_params)
    total = response.json()['data']['total']
    print(f'total:{total}')
    fetch_images_list(total)


def fetch_images_list(total):
    page_count = 20
    for page_no in range(20, total, page_count):
        print(f'pageNo:{page_no}')
        data_params = fetch_params(page_no=page_no, page_count=page_count)
        response = requests.post(url=album_url, headers=headers, data=data_params)
        data_list = response.json()['data']['list']
        for item in data_list:
            url = item['other']['works']['url']
            title = item['other']['works']['title']
            # print(url)
            fetch_image(url, title)


if __name__ == '__main__':
    fetch_images_count()
