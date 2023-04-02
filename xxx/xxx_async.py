import asyncio
import os
import re
import time

import aiohttp
import requests
import uvloop

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

url = 'https://r5vg.com/web/abcdefg.ashx?v='


async def fetch_page_count(time_stamp, page_size):
    async with semaphore:
        fetch_url = url + str(time_stamp)
        data = "action=getvideos&vtype=3026&pageindex=1&pagesize=1&tags=%E5%85%A8%E9%83%A8&sortindex=1"
        async with aiohttp.ClientSession() as session:
            async with session.post(url=fetch_url, headers=headers, data=data) as response:
                content = await response.json()
                count = content['pagecount']
                print(f'count={count}')
                if count % page_size == 0:
                    total_page = count / page_size
                else:
                    total_page = count / page_size + 1

                task_list = []
                for page_no in range(1, total_page):
                    task_list.append(
                        asyncio.ensure_future(fetch_data(time_stamp, page_no, page_size), loop=loop)
                    )
                await asyncio.wait(task_list)


async def fetch_data(time_stamp, page_index, page_size):
    async with semaphore:
        fetch_url = url + str(time_stamp)
        data = f"action=getvideos&vtype=3026&pageindex={page_index}&pagesize={page_size}&tags=%E5%85%A8%E9%83%A8&sortindex=1"
        async with aiohttp.ClientSession() as session:
            async with session.post(url=fetch_url, headers=headers, data=data) as response:
                content = await response.json()
                video_list = content['videos']
                task_list = []
                for video in video_list:
                    viewcount = video['viewcount']
                    if viewcount < 400000:
                        continue
                    yuming = video['yuming']
                    vurl = video['vurl']
                    title = video['title']
                    m3u8_url = yuming + vurl
                    print(f'm3u8_url={m3u8_url}')
                    task_list.append(asyncio.ensure_future(fetch_video_data(m3u8_url, title), loop=loop))

                await asyncio.wait(task_list)


async def fetch_video_data(m3u8_url, title):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=m3u8_url) as response:
                m3u8_data = await response.text()
                ts_list = re.sub('#E.*', '', m3u8_data).split()
                ts_url_prefix = m3u8_url[0:m3u8_url.rfind('/') + 1]
                task_list = [asyncio.ensure_future(download_video(ts_url_prefix + ts, title), loop=loop) for ts in ts_list]
                await asyncio.wait(task_list)


async def download_video(ts_url, title):
    print(f'ts_url={ts_url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(ts_url, ssl=False) as down_response:
            if down_response.status == 200:
                dir_path = os.getcwd() + '/videos/'
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                name = title + ".mp4"
                if os.path.exists(dir_path + name):
                    print(name + ' 文件已存在')
                    return
                else:
                    pass
                    print('正在下载：' + name)
                with open(dir_path + name, 'ab') as file:
                    async for chunk in down_response.content.iter_chunked(1024):
                        file.write(chunk)


if __name__ == '__main__':
    start_time = time.time()
    time_stamp = round(start_time * 1000)
    page_size = 30
    semaphore = asyncio.Semaphore(5)
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_page_count(time_stamp, page_size))
    loop.close()
    print("async total time：", time.time() - start_time)