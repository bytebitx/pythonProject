import asyncio
import hashlib
import os
import pprint
import re
from multiprocessing.dummy import Pool

import aiohttp
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

# async def request_page_count():
#     response = requests.post(url, data=data, json=None, headers=headers)
#     page_count = response.json()['pagecount']
#     print(f'page_count = {page_count}')
#     return page_count
#
#
# # async修饰的函数，调用之后返回一个协程对象
# async_result = request_page_count()
# print(async_result)
# # 创建一个事件循环对象
# loop = asyncio.new_event_loop()


# 将协程对象注册到loop当中，然后启动loop
# loop.run_until_complete(async_result)
# page_count = 159


# task = asyncio.ensure_future(async_result, loop=loop)
# print(task)
# loop.run_until_complete(task)
# print(task)
# <Task pending name='Task-1' coro=<request_page_count() running at /Users/geely/PycharmProjects/pythonProject/demo_xxx/xxx_coroutine.py:25>>
# page_count159
# <Task finished name='Task-1' coro=<request_page_count() done, defined at /Users/geely/PycharmProjects/pythonProject/demo_xxx/xxx_coroutine.py:25> result=None>


url_list = []
name_list = []

dir_path = os.getcwd() + '/videos/'
if not os.path.exists(dir_path):
    os.mkdir(dir_path)


def request_all_data():
    for page in range(1, 2):
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


async def downloadVideo(down_url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:

            # 以下代码也能执行，注意写法
            # down_response = await session.get(down_url, ssl=False)
            # if down_response.status == 200:
            #     name = down_url.split('/')[-1]
            #     if os.path.exists(dir_path + name):
            #         print(name + ' 文件已存在')
            #         return
            #     else:
            #         pass
            #     with open(dir_path + name, 'wb') as file:
            #         file_content = await down_response.read()
            #         file.write(file_content)

            # 建议这种写法
            async with session.get(down_url, ssl=False) as down_response:
                if down_response.status == 200:
                    name = down_url.split('/')[-1]
                    if os.path.exists(dir_path + name):
                        print(name + ' 文件已存在')
                        return
                    else:
                        print('正在下载：' + name)
                    with open(dir_path + name, 'wb') as file:
                        async for chunk in down_response.content.iter_chunked(1024):
                            file.write(chunk)


if __name__ == '__main__':
    # 控制并发数量
    semaphore = asyncio.Semaphore(2)
    request_all_data()
    loop = asyncio.new_event_loop()
    tasks = [asyncio.ensure_future(downloadVideo(url, semaphore), loop=loop) for url in url_list]
    loop.run_until_complete(asyncio.wait(tasks))
