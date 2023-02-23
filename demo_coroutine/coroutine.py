import asyncio
import time


async def test():
    print('hello')

c = test()
print(c)
print(type(c))
loop = asyncio.new_event_loop()
task = asyncio.ensure_future(test(), loop=loop)
loop.run_until_complete(task)
# loop.run_until_complete(asyncio.wait(task))
# TypeError: expect a list of futures, not Task

def running():
    async def test1():
        print('test1')
        await test2()
        print('test2')
    async def test2():
        print('3')
        print('4')
    loop = asyncio.new_event_loop()
    loop.run_until_complete(test1())

if __name__ == '__main__':
    running()


async def func(url):
    print(f'正在请求{url}')

# func('www.google.com')
# coroutine 'test' was never awaited

async def do_some_work(n):
    print(f'waiting {n} 秒')
    # await asyncio.sleep(2)
    time.sleep(n)
    return '{}秒后返回结束运行'.format(n)

start_time = time.time()

c = do_some_work(2)
loop = asyncio.new_event_loop()
f = asyncio.ensure_future(c, loop=loop)
loop.run_until_complete(f)
print(f.result())

print('运行时间：', time.time() - start_time)
