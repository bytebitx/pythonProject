import asyncio
import time


async def request(url):
    print(f'正在请求的url{url}')
    print(f'{url}请求成功')
    # return url

c = request('www.google.com')

print(c)
print(type(c))

# loop = asyncio.new_event_loop()
# loop.run_until_complete(c)

def callback_func(task):
    print(task.result())


loop = asyncio.new_event_loop()
task = asyncio.ensure_future(c, loop=loop)
task.add_done_callback(callback_func)
loop.run_until_complete(task)

async def request_url(url):
    print(f'正在请求：{url}')
    # 在异步协程中不能出现同步代码块，否则无法实现异步
    # time.sleep(2)
    # 在异步协程中，遇到耗时操作必须手动挂起
    await asyncio.sleep(2)
    print(f'{url}请求完成')

urls = [
    'www.google.com',
    'www.weibo.sina.cn',
    'www.tencent.com'
]

start_time = time.time()
print('start time ', start_time)
loop = asyncio.new_event_loop()
tasks = [asyncio.ensure_future(request_url(url), loop=loop) for url in urls]
loop.run_until_complete(asyncio.wait(tasks))

print('task complete time', time.time() - start_time)