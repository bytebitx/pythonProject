import os
import re

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
url = 'https://www.ximalaya.com/album/9723091'


response = requests.session().get(url=url, headers=headers)
# print(response.text)
titles_a = re.findall('"tag":0,"title":"(.*?)","playCount"', response.text)
titles_b = re.findall('"trackName":"(.*?)","playCount"', response.text)
audio_id_a = re.findall('"url":"(.*?)","duration"', response.text)
audio_id_b = re.findall('"uri":"(.*?)","createDateFormat"', response.text)

title_audio = zip(titles_b + titles_a, audio_id_b + audio_id_a)
audio_request_url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'
for item in title_audio:
    title = item[0]
    audio_id = str(item[1]).split('/')[-1]
    audio_addr = requests.get(audio_request_url.format(audio_id), headers=headers)
    audio_addr.encoding = 'utf-8'
    # pprint.pprint(audio_addr.json())
    audio_url = audio_addr.json()['data']['src']
    print(audio_url)

    # 下载文件方式一：
    # file_content = requests.get(audio_url)
    # if file_content.status_code == 200:
    #     with open(os.getcwd() + '/file/' + title + '.mp3', 'wb') as file:
    #         file.write(file_content.content)
    #         print('正在保存：' + title)

    # 下载文件方式二：
    # 当使用requests的get下载大文件 / 数据时，建议使用使用stream模式。
    # 当把get函数的stream参数设置成False时，它会立即开始下载文件并放到内存中，如果文件过大，有可能导致内存不足。
    # 当把get函数的stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载。需要注意一点：文件没有下载之前，它也需要保持连接。
    # iter_content：一块一块的遍历要下载的内容
    # iter_lines：一行一行的遍历要下载的内容
    # 使用上面两个函数下载大文件可以防止占用过多的内存，因为每次只下载小部分数据。
    r = requests.get(audio_url, stream=True)
    dir_path = os.getcwd() + '/file/'
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    if r.status_code == 200:
        print('正在保存：' + title)
        with open(dir_path + title + '.mp3', 'wb') as file:
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    file.write(chunk)
