import asyncio
import json
import os
import re
import time

import aiohttp
import parsel
import requests
import uvloop

base_url = 'https://www.ku6.com'


def request_index():
    index_url = 'https://www.ku6.com/index'

    index_res = requests.get(index_url)
    # print(index_res.text)

    selector = parsel.Selector(index_res.text)
    video_detail_list = selector.xpath('//a[@class="video-image-warp"]/@href').getall()

    v_list = []

    for detail_url in video_detail_list:
        if re.search('/video/.*', detail_url):
            video_res = requests.get(base_url + detail_url).text
            # print(video_res)
            video_url = re.search('flvURL: "(.*?)",', video_res).group(1)
            video_name = re.search('document.title = "(.*?)"', video_res).group(1)
            # print(video_url)
            # print(video_name)
            v_list.append({'url': video_url, 'name': video_name})
    return v_list


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
    semaphore = asyncio.Semaphore(5)
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    video_list = request_index()
    tasks = [asyncio.ensure_future(downloadVideo(item['url'], item['name'], semaphore), loop=loop)
             for item in video_list]
    loop.run_until_complete(asyncio.wait(tasks))
    print('task end, total time:', time.time() - start_time)
    # sync task end, total time: 933.0300421714783
