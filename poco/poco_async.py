import asyncio
import hashlib
import json
import os
import re
import time
import urllib.parse

import aiohttp
import execjs
import requests
import uvloop

album_url = 'https://web-api.poco.cn/v1_1/rank/get_homepage_recommend_list'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Content-Length': '393',
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

    # print(now)
    # print(time_point)

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
    return data_params


async def download_img(url, title):
    # print(url, title)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as down_response:
            url_content_array = url.split('/')
            name = url_content_array[len(url_content_array) - 1]
            if down_response.status == 200:
                dir_path = os.getcwd() + '/images/' + title + "/"
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                if os.path.exists(dir_path + name):
                    print(name + ' 文件已存在')
                    return
                else:
                    pass
                    print('正在下载：' + name)
                with open(dir_path + name, 'wb') as file:
                    async for chunk in down_response.content.iter_chunked(1024):
                        file.write(chunk)


async def fetch_image(url, title):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=get_headers) as response:
                html_content = await response.text()
                img_list = re.findall('<img data-src="(.*?)"/>', html_content)
                while '' in img_list:
                    img_list.remove('')
                # print(img_list)
                task_list = [asyncio.ensure_future(download_img('https:' + url, title), loop=loop) for url in img_list]
                await asyncio.wait(task_list)


async def main():
    data_params = fetch_params(page_no=0, page_count=20)
    async with aiohttp.ClientSession() as session:
        async with session.post(url=album_url, headers=headers, data=data_params) as response:
            json_content = await response.json()
            total = json_content['data']['total']
            print(f'total:{total}')
            await create_fetch_list_tasks(total)


async def fetch_images_list(total, page_count):
    async with semaphore:
        for page_no in range(0, total, page_count):
            data_params = fetch_params(page_no=page_no, page_count=page_count)
            async with aiohttp.ClientSession() as session:
                async with session.post(url=album_url, headers=headers, data=data_params) as response:
                    json_content = await response.json()
                    data_list = json_content['data']['list']
                    task_list = []
                    for item in data_list:
                        url = item['other']['works']['url']
                        title = item['other']['works']['title']
                        task = asyncio.ensure_future(fetch_image(url, title), loop=loop)
                        task_list.append(task)
                    await asyncio.wait(task_list)


async def create_fetch_list_tasks(total):
    page_count = 20
    task_list = []
    for page_no in range(0, total, page_count):
        print(f'pageNo:{page_no}')
        task = asyncio.ensure_future(fetch_images_list(total, page_count), loop=loop)
        task_list.append(task)
        await asyncio.wait(task_list)


if __name__ == '__main__':
    start_time = time.time()
    semaphore = asyncio.Semaphore(5)
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()
    print("async total time：", time.time() - start_time)
