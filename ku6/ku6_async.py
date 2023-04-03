import asyncio
import os
import re
import time

import aiohttp
import parsel
import requests
import uvloop

base_url = 'https://www.ku6.com'


async def request_detail_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            video_res = await response.text()
            video_url = re.search('flvURL: "(.*?)",', video_res).group(1)
            video_name = re.search('document.title = "(.*?)"', video_res).group(1)
            video_list.append({'url': video_url, 'name': video_name})
            # return video_list,
def request_data(loop):
    index_url = 'https://www.ku6.com/index'

    index_res = requests.get(index_url)
    # print(index_res.text)

    selector = parsel.Selector(index_res.text)
    video_detail_list = selector.xpath('//a[@class="video-image-warp"]/@href').getall()

    # v_list = []

    task_list = []

    for detail_url in video_detail_list:
        if re.search('/video/.*', detail_url):
            task_list.append(
                asyncio.ensure_future(request_detail_data(base_url + detail_url), loop=loop)
            )

    return task_list



async def downloadVideo(down_url, name, semaphore):
    print(down_url)
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(down_url, ssl=False) as down_response:
                if down_response.status == 200:
                    if os.path.exists(dir_path + name):
                        print(name + ' 文件已存在')
                        return
                    else:
                        print('正在下载：' + name)
                    with open(dir_path + name + '.mp4', 'wb') as file:
                        async for chunk in down_response.content.iter_chunked(1024):
                            file.write(chunk)


if __name__ == '__main__':
    start_time = time.time()
    dir_path = os.getcwd() + '/videos/'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    video_list = []
    semaphore = asyncio.Semaphore(5)
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    task_list = request_data(loop)
    loop.run_until_complete(asyncio.wait(task_list))
    print(video_list)
    tasks = [asyncio.ensure_future(downloadVideo(item['url'], item['name'], semaphore), loop=loop)
             for item in video_list]
    loop.run_until_complete(asyncio.wait(tasks))

    print("async total time：", time.time() - start_time)
