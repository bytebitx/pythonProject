import re

import parsel
import requests

html = '''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
  </div>
 </body>
</html>
'''

selector = parsel.Selector(html)
'''使用xpath方法获取id为images下的所有a标签'''
items = selector.xpath('//div[@id="images"]/a')
print(items.getall())
result_text = [item.xpath('./text()').get() for item in items]
result_href = [item.xpath('./@href').get() for item in items]
reuslt_img = [item.re('src="(.*)"') for item in items]
print(type(items))
print(items)
print(result_text)
print(result_href)
print(reuslt_img)

# 运行结果
# ['<a href="image1.html">Name: My image 1 <br><img src="image1_thumb.jpg"></a>', '<a href="image2.html">Name: My image 2 <br><img src="image2_thumb.jpg"></a>', '<a href="image3.html">Name: My image 3 <br><img src="image3_thumb.jpg"></a>', '<a href="image4.html">Name: My image 4 <br><img src="image4_thumb.jpg"></a>', '<a href="image5.html">Name: My image 5 <br><img src="image5_thumb.jpg"></a>']
# <class 'parsel.selector.SelectorList'>
# [<Selector xpath='//div[@id="images"]/a' data='<a href="image1.html">Name: My image ...'>, <Selector xpath='//div[@id="images"]/a' data='<a href="image2.html">Name: My image ...'>, <Selector xpath='//div[@id="images"]/a' data='<a href="image3.html">Name: My image ...'>, <Selector xpath='//div[@id="images"]/a' data='<a href="image4.html">Name: My image ...'>, <Selector xpath='//div[@id="images"]/a' data='<a href="image5.html">Name: My image ...'>]
# ['Name: My image 1 ', 'Name: My image 2 ', 'Name: My image 3 ', 'Name: My image 4 ', 'Name: My image 5 ']
# ['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
# [['image1_thumb.jpg'], ['image2_thumb.jpg'], ['image3_thumb.jpg'], ['image4_thumb.jpg'], ['image5_thumb.jpg']]

'''使用css方法获取id为images下的所有a标签'''
print('\n')
items = selector.css('#images > a')
result_text = [item.css('::text').get() for item in items]
result_href = [item.css('::attr(href)').get() for item in items]
print(result_text)
print(result_href)

# 一般在实际工作中，比较常用的一种方式是使用css选择器先获取大的数据，
# 在使用xpath去进行分析每一项的数据，最后如果需要仅获取里面的数值可以加上正则表达式进行获取

with open('demo.html') as file:
    content = file.read()

selector = parsel.Selector(content)
product_list = selector.css('.product-list li')
print(product_list)
for product in product_list:
    temp_name = product.xpath('.//div[@class="p-name"]/text()').get()
    product_name = re.match('(.*) .*', temp_name).group(1)
    print(product_name)
    href = 'http' + product.xpath('./a/@href').get()
    print(href)
    price_str = product.xpath('.//div[@class="p-price"]/text()').get()
    price = product.xpath('.//div[@class="p-price"]/text()').re('\d+\D\d+')[0]
    print(price_str)
    print(price)
    product_imgs = product.xpath('.//img[@class="p-img"]')
    for product_img in product_imgs:
        img_cover = 'http' + product_img.re('src="(.*?)"')[0]
        print(img_cover)
    print('\n')

# 使用css解析
# css解析用法参见：https://blog.csdn.net/zxctime/article/details/106962727
headers = {
    'cookie': 'll="118282"; bid=I4xPT5iBnNA; '
              '_vwo_uuid_v2=D24D03DD4403E8749B798BE979D3E3B5E|8d01754b7587dfc1a572f4f21b96a2e0; '
              '__gads=ID=b834e936a3161bec-229502ff15d7008f:T=1665994840:RT=1665994840:S'
              '=ALNI_MbDUoILtgmRIVFDO5g46facXBo6Pw; __utmc=30149280; '
              '__utmz=30149280.1676280790.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; '
              '__utmz=223695111.1676280790.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; '
              '__yadk_uid=tQBnYimVbXCP9hlhpHGKQ3Jqfta3ADMT; dbcl2="200474597:RtMKQfIj5zk"; ck=RfrM; push_noty_num=0; '
              'push_doumail_num=0; __gpi=UID=00000b645227019d:T=1665994840:RT=1676340177:S=ALNI_MYfoD'
              '-0SPdfUbgBJdrWOPMj3740kA; ap_v=0,6.0; __utma=30149280.1056144027.1665994530.1676340176.1676357576.6; '
              '__utmb=30149280.0.10.1676357576; __utma=223695111.325937377.1667269149.1676340176.1676357576.5; '
              '__utmb=223695111.0.10.1676357576; '
              '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1676357576%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl'
              '%3DpHtW5VrWQbX2OS5DculysbPKwBbhfX9-ISy0kBrD9biD01gH8EljcZpRA-VqzwT1X0rN4GFb7lX_T2QDHNGiOK%26wd%3D'
              '%26eqid%3Da2badfe4000080d20000000663ea03d2%22%5D; _pk_ses.100001.4cf6=*; '
              '_pk_id.100001.4cf6=4f3af99e95fa081b.1667269148.5.1676357601.1676340176.; '
              'Hm_lvt_16a14f3002af32bf3a75dfe352478639=1676357601; '
              'Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1676357601; frodotk_db="dc82683367a5f02c9587389a36f1d084"',
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36'
}

reponse = requests.get('https://movie.douban.com/chart', headers=headers)
selector = parsel.Selector(reponse.text)
content = selector.css('#content')
print(content)
for item in content:
    page_title = item.css('h1::text').get()
    print(page_title)
    movie_list = item.css('.item')
    for movie_item in movie_list:
        cover_href = movie_item.css('.nbg::attr(href)').get()
        title = movie_item.css('.nbg::attr(title)').get()
        print(cover_href)
        print(title)
        movie_url = movie_item.css('.pl2 a::attr(href)').get()
        print(movie_url)
        first = movie_item.css('.pl2 a::text').get().strip().replace('\n', '').replace(' ', '')
        second = movie_item.css('.pl2 span::text').get().strip()
        print(first + second)
        author = movie_item.css('.pl::text').get().strip()
        print(author)
        score = movie_item.css('.rating_nums::text').get().strip()
        print(score)
        print('--------------')
    print('*************************************\n'
          '*************************************\n'
          '*************************************')

    # 使用xpath解析
    for movie_item in movie_list:
        movie_cover = movie_item.xpath('.//a[@class="nbg"]/@href').get()
        movie_url = movie_item.xpath('.//div[@class="pl2"]/a/@href').get()
        first = movie_item.xpath('.//div[@class="pl2"]/a/text()').get().strip().replace('\n', '').replace(' ', '')
        second = movie_item.xpath('.//div[@class="pl2"]/a/span/text()').get()
        author = movie_item.xpath('.//p[@class="pl"]/text()').get()
        rating_num = movie_item.xpath('.//span[@class="rating_nums"]/text()').get()
        print('movie_cover:' + movie_cover)
        print('movie_url:' + movie_url)
        print('movie_name:' + first + second)
        print('movie_author:' + author)
        print('movie_rating_nums:' + rating_num)

with open('demo2.html', 'r', encoding='utf-8') as file:
    content = file.read()

selector = parsel.Selector(content)
ul_list = selector.xpath('.//ul/li')
result_dict = {ul.xpath('./a/text()').get(): ul.xpath('./a/@href').get() for ul in ul_list}
print(result_dict)
