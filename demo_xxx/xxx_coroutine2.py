import asyncio
import json
import os
import pprint
import re
import time

import aiohttp
import requests
import uvloop

async def request_url(page):
    name_list = []
    url_list = []
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
    params = f'action=getvideos&vtype=3026&pageindex={page}&pagesize=30&tags=全部&sortindex=1'
    data = params.encode('utf-8')
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, json=None, headers=headers, ssl=False) as response:
            content = await response.text()
            json_content = json.loads(content)
            # video_list = json_content['videos']
            # for video in video_list:
            #     title = video['title']
            #     download_url = video['downvurl']
            #     match_obj_1 = re.search(r'JUL', title, re.M | re.I)
            #     match_obj_2 = re.search(r'ADN', title, re.M | re.I)
            #     if match_obj_1 or match_obj_2:
            #         name_list.append(title)
            #         url_list.append(f'https://xunlei.grr4d46c.com/changpian{download_url}')
            #         continue
            pprint.pprint(json_content)
            return name_list, url_list


def task_call_back(task):
    global u_list
    n_list, u_list = task.result()
    pprint.pprint(n_list)
    pprint.pprint('---------------------')
    pprint.pprint(u_list)
    return u_list

async def downloadVideo(down_url, semaphore):
    dir_path = os.getcwd() + '/videos/'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    async with semaphore:
        async with aiohttp.ClientSession() as session:
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


def create_request_task():
    task_list = []
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    for page in range(1, 2):
        task = asyncio.ensure_future(request_url(page), loop=loop)
        # task.add_done_callback(task_call_back)
        task_list.append(task)
    loop.run_until_complete(asyncio.wait(task_list))

    # semaphore = asyncio.Semaphore(2)
    # download_tasks = [asyncio.ensure_future(downloadVideo(url, semaphore), loop=loop)for url in u_list]
    # loop.run_until_complete(asyncio.wait(download_tasks))
    return task_list
    # result, pending = await asyncio.wait(task_list)
    # # 得到执行结果
    # for done_task in result:
    #     print(f"{time.time()} 得到执行结果 {done_task.result()}")



if __name__ == '__main__':
    # create_sync_task()
    start_time = time.time()
    print(f'async start time = {start_time}')
    create_request_task()
    print('async total time = ', time.time() - start_time)
