import asyncio
import hashlib
import os
import time

import aiohttp
import parsel
import uvloop


async def request_data(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                text_content = await response.text()
                selector = parsel.Selector(text_content)
                page_list = selector.xpath('//ul[@class="txtList"]/li/h3/a/@href').getall()
                title_list = selector.xpath('//ul[@class="txtList"]/li/h3/a/@title').getall()
                # 将两个列表转为字典
                return dict(zip(page_list, title_list))


async def request_detail_data(url, title):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                text_content = await response.text()
                selector = parsel.Selector(text_content)
                detail_list = selector.xpath('//div[@class="img"]/a/img/@src').getall()
                # 字典推导式
                result = {item: title for item in detail_list}
                return result


async def downloadVideo(down_url, title):
    # print(down_url)
    async with down_semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(down_url, ssl=False) as down_response:
                name = hashlib.md5(down_url.encode(encoding='utf-8')).hexdigest()
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
                    with open(dir_path + name + '.jpg', 'wb') as file:
                        async for chunk in down_response.content.iter_chunked(1024):
                            file.write(chunk)


async def create_task_list():
    for index in range(1, 197, 2):
        task_list = []
        page_list = {}
        for page in range(index, index + 2):
            url = f"https://bbs.fengniao.com/forum/forum_101_{page}_execpost.html"
            task_list.append(asyncio.ensure_future(request_data(url), loop=loop))
        done, pending = await asyncio.wait(task_list)
        for done_task in done:
            # print(len(done_task.result()))
            page_list.update(done_task.result())
        # print(len(page_list))
        # print(page_list)

        download_dict = {}
        data_task_list = [asyncio.ensure_future(request_detail_data(f'https://bbs.fengniao.com{key}', value), loop=loop)
                          for key, value in page_list.items()]
        done, pending = await asyncio.wait(data_task_list)
        for done_task in done:
            print(len(done_task.result()))
            # 将一个字典的内容添加到另外一个字典中
            download_dict.update(done_task.result())
        print(len(download_dict))
        download_task_list = [asyncio.ensure_future(downloadVideo(key, value), loop=loop)
                              for key, value in download_dict.items()]  # 遍历字典
        await asyncio.wait(download_task_list)
        print("fetch next 2")
        await asyncio.sleep(60 * 3)


if __name__ == '__main__':
    start_time = time.time()

    semaphore = asyncio.Semaphore(2)
    down_semaphore = asyncio.Semaphore(5)
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(create_task_list())

    print("async total time：", time.time() - start_time)
