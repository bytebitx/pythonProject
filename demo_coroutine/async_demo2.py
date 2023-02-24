import asyncio
import time

import aiohttp
import parsel
import requests
import uvloop

headers = {
    'cookie': 'll="118282"; bid=I4xPT5iBnNA; '
              '_vwo_uuid_v2=D24D03DD4403E8749B798BE979D3E3B5E|8d01754b7587dfc1a572f4f21b96a2e0; '
              '__gads=ID=b834e936a3161bec-229502ff15d7008f:T=1665994840:RT=1665994840:S'
              '=ALNI_MbDUoILtgmRIVFDO5g46facXBo6Pw; '
              '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1676280789%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl'
              '%3DpHtW5VrWQbX2OS5DculysbPKwBbhfX9-ISy0kBrD9biD01gH8EljcZpRA-VqzwT1X0rN4GFb7lX_T2QDHNGiOK%26wd%3D'
              '%26eqid%3Da2badfe4000080d20000000663ea03d2%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,'
              '6.0; __utma=30149280.1056144027.1665994530.1667269149.1676280790.3; __utmb=30149280.0.10.1676280790; '
              '__utmc=30149280; __utmz=30149280.1676280790.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; '
              '__utma=223695111.325937377.1667269149.1667269149.1676280790.2; __utmb=223695111.0.10.1676280790; '
              '__utmc=223695111; __utmz=223695111.1676280790.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; '
              '__yadk_uid=tQBnYimVbXCP9hlhpHGKQ3Jqfta3ADMT; '
              '__gpi=UID=00000b645227019d:T=1665994840:RT=1676280791:S=ALNI_MYfoD-0SPdfUbgBJdrWOPMj3740kA; '
              'dbcl2="200474597:RtMKQfIj5zk"; ck=RfrM; '
              '_pk_id.100001.4cf6=4f3af99e95fa081b.1667269148.2.1676283955.1667269148.; push_noty_num=0; '
              'push_doumail_num=0',
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36'
}


async def request_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False) as response:
            html_content = await response.text()
            html_list.append(html_content)
            # print(html_content)
            return html_content


async def request_all_data():
    task_list = []
    for page in range(0, 250, 25):
        rc = request_data('https://movie.douban.com/top250?start={}'.format(page))
        task_list.append(asyncio.ensure_future(rc, loop=loop))
    done, pending = await asyncio.wait(task_list)
    # for done_task in done:
    #     html_list.append(done_task.result())
    #     print(done_task.result())


async def crawl_data(data):
    selector = parsel.Selector(data)
    li_s = selector.css('.grid_view li')

    # 爬取电影名称、导演、演员、评分等
    for item in li_s:
        film_name_li = item.css('.hd')
        for item_name in film_name_li:
            title_list = item_name.css('.title')
            title = title_list[0].css('span::text').get()
            print(title)
            title_dict = {'电影名字': title}
            other_info = item.css('.bd')
            for other_item in other_info:
                au_li = other_item.css('p::text')
                for au_item in au_li:
                    if au_item.get().strip() != '':
                        print(au_item.get().strip())
                # print(other_item.css('p::text').get().strip())
                ra_dict = {'评分': other_item.css('.rating_num::text').get(),
                           '简介': other_item.css('.inq::text').get()}
                print(other_item.css('.rating_num::text').get())
                print(other_item.css('.inq::text').get())
                ra_dict.update(title_dict)
                print(ra_dict)
        print('--------------')


if __name__ == '__main__':
    start_time = time.time()
    html_list = []
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(request_all_data())
    task_list = [asyncio.ensure_future(crawl_data(item), loop=loop) for item in html_list]
    loop.run_until_complete(asyncio.wait(task_list))

    print('async crawl data is ', time.time() - start_time)
