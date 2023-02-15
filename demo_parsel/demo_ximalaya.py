import parsel
import requests

headers = {
    'cookie': '_xmLog=h5&a02650f5-6950-40ed-95ef-8992c609b616&process.env.sdkVersion; xm-page-viewid=ximalaya-web; '
              'impl=www.ximalaya.com.login; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A'
              '%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A; '
              'Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1676360116; hide_himayala_bar=1; '
              'Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1676426638',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36',
    'Host': 'www.ximalaya.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9'
}

response = requests.get('https://www.ximalaya.com/album/9723091', headers=headers)
# print(response.text)
selector = parsel.Selector(response.text)
print(selector.xpath('//ul/li[@class="_nO"]'))
# for ul_item in ul_list:
#     ul_a = ul_item.xpath('./ul')
#     print(ul_a)
    # title = ul_a.xpath('./a/@title').get()
    # href = ul_a.xpath('./a/href').get()
    # print('title = ' + title)
    # print('href = ' + title)
# 音频名字
# titles = re.findall('"tag":0,"title":"(.*?)","playCount"', response.text)
# # 音频ID
# audio_id_list = re.findall('"url":"/sound/(\d+)","duration"', response.text)
# print(titles)
# print(audio_id_list)