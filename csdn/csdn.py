import os.path
import pprint

import parsel
import pdfkit
import requests

header = {
    'cookie': 'uuid_tt_dd=10_30711554790-1660272679360-874892; '
              '__gads=ID=d31f65afdb5bcfa2-2294665e86d50095:T=1660272680:RT=1660272680:S'
              '=ALNI_MaiFIr0NZY20ev2Lapns3dx63ZZFA; UN=wyb112233; '
              'Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_30711554790-1660272679360-874892!5744*1*wyb112233; '
              '_ga=GA1.2.1689743054.1661309508; __bid_n=183ab6845ab49ceffb4207; '
              'FPTOKEN=30$xbYMAelJH8m+3bmAHi6kzqCjnSK0VWTYqBcHTzsBu90TBOy/v5bHJwSVqs'
              '/K2YZFCDpiWriKovRluOKKSDs6E0kucLT7mVyEDbNTM3UIiDOtaGjdrww7mv2Eyaaxl5h1prOpEso3cISbraIbguBC3pxB4gsX06EuqUJywdWd22ce7BeudH+F6YcsuRXhfmb1wFaS5XSfz/RyQY1RGB9Fjo9ngERiPzqnBb2u1B/4LX3wQ0hN6v/wWxrSxqd7LLq2w5uyLGvi03GJ231wkWJGVsliEQ3eozH2q/B728tKnoefBZDRXANr3YK3jIcqG6wJoUiRrDvxrTuFJA9ADlMccAHaGgaJIeefbZx0KPt38ix+loM/g4KB00C9PnQ+3t2s|r1DNfc3PtB86ESiBPer1orO1VuXikSYkhsamIdkONlA=|10|23051f8cff3d4db94b2a2eb293333669; FEID=v10-24be5015536a3600c937a9024fa7bb11eea16419; HWWAFSESID=67b3c6f4aba5748b455; HWWAFSESTIME=1672714650017; c_segment=12; dc_sid=f5a007b9dc0152a0546b286815eb3354; FCNEC=%5B%5B%22AKsRol9BPDoPryZ7_KoiYsmsE7bY9-sb4dYGHzDvttcg9sK_FexJ6cPomFI-PpTHYJJ69YZsqUVMIkGbNt-yQR3oQQ77eu_5PVChpiszoIDmAp3tRU_lerV92zKoQRQSOFz1eCJhd7drJgzK7nsdu2mK8V-9L08gsA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; __xaf_fpstarttimer__=1672888473175; __xaf_fptokentimer__=1672888473289; __gpi=UID=000006f0edea93f3:T=1660272680:RT=1672888474:S=ALNI_MYQVYWg9e7xCqlyA9LFk6OqVGrZ4Q; __xaf_thstime__=1672898035904; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1675651835; c_dl_prid=-; c_dl_rid=1675757091856_708010; c_dl_fref=https://www.baidu.com/link; c_dl_fpage=/download/weixin_42168230/18581052; c_dl_um=-; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1675822135; Hm_lpvt_e5ef47b9f471504959267fd614d579cd=1675822135; SESSION=df2024b1-9ff1-41a9-94ef-9584a0007547; UserName=wyb112233; UserInfo=078ed1dfb031422bbc1c76d7d83cdbc3; UserToken=078ed1dfb031422bbc1c76d7d83cdbc3; UserNick=crazyWangyb; AU=7B3; BT=1675926353836; p_uid=U010000; ssxmod_itna=eqjOq0xfxIxAxDqxBpkQdGkWGCDRi00Q0mgQEBxhx0yGReGzDAxn40iDt=aMGjfRw4YYR08YqQ3KBhP5e=s2maKNt72DxLaHDneG0DQKGmDBKDSDWKD9IG74GGRxBYDQxAYDGDDPBDGuXcbqDFRMXDTdXUKYNDG4DgDB64xBoVbLQMRuxDCODDbhpg+QbDtT0lQdQtgMixVC4KGDLaDS=PCOeeBY4KYBm4FGGKGD+mlDgtKGq4BYEdB84Y8CDYUBemPD; ssxmod_itna2=eqjOq0xfxIxAxDqxBpkQdGkWGCDRi00Q0mgQEBxxn9fvYDsqzYtDLQAmOvx2Bxq+=hg4tnFqK0Dn+vw37R0IuQr2Oqxukq0f18yp3/I1ov2QoCUj8utg0j=Bx41bz/yydNAFQHMn6oX1fwoejrflbT3Rbw00jgKRUrfglbffFbfkRuo5MeQvB3NUBf3+0x4IYp5weS=he3LTpZAHNRqTXaEOk=iwlMyUtcFGg39GEcamMc9wh13AFpD5SpSvuPBvu8a+OZn3cUymZpy0sKHOUcSw30f6jDx4lSKgsCTntejkUxu6l=TciEVoPNada1plBNQoiRefVOQih0qSjw759xpu6t+m35Fo5IpNaPEiEW1q2WPSgd27Ayi4CjwjjqumP2YIyjwnmpnmuaDG2R0Q8orA2FnxN4fQYPr2hruhbUuxA2W7GLB09YcQQndYbxD08DijWxhq0x1mWeQGGQqLgxNe6A=GQYNoYXeY94mfeYLPmW5G2NYwQ7fsi=MfFPCcYeeNBD473tlngBDxD===; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22wyb112233%22%2C%22scope%22%3A1%7D%7D; FPTOKEN=Xxt3ztJ/mkS1MFsVWkQ/9UrWVEoIN0mJ+PWJ0URTBxvkq9cZqrodDKTolHDZn9YJQk9qiTah1zemqL/NGxrH+Y8v713LuA+vVzoqzyT6B1BJWkKZPHkABTy2cqUXzseEgEV77xZ70ao2xhQOzCNDi9P/8O0hUVGtW/1hykXRysZPQDa3UfMHmnaDHs/H/o0C4G6PW5n9mgiqd/nX5IpTeJZpHgFDOlSb+2aze1g+9Mh1hMH7VytK+KGWkF6PFMoi7xfH//kf11omac4SZCF9T2RthOrtk8CG7r1nYNDoW/tnx8vpTPonkZB355a+q1mWQm4hB2a1AI0rD9ilTCr45FvLk4awPnKHuQKvY5yDEbAJnQqKFSjIQRBKjY3hA7jHGSpm5ElG8NHPxO2dB1fnXA==|8XX92C8pzeURcExAJVGH+/H5BVdHn8LRubCiE+J4aiw=|10|bf7dc4a63829e84d93c72ab6713d9e48; firstDie=1; dc_session_id=10_1676599420580.289054; log_Id_view=7103; log_Id_click=892; c_pref=default; c_ref=default; c_first_ref=default; c_first_page=https%3A//blog.csdn.net/guolin_blog%3Ftype%3Dblog; c_dsid=11_1676599434767.808908; c_page_id=default; dc_tos=rq7cei; log_Id_pv=1663; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1676599435',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/109.0.0.0 Safari/537.36',
    'authority': 'blog.csdn.net'
}

url = 'https://blog.csdn.net/community/home-api/v1/get-business-list?page=1&size=20&businessType=blog&orderby=&noMore' \
      '=false&year=&month=&username=sinyu890807'

response = requests.get(url, headers=header)
pprint.pprint(response.json())

article_list = response.json()['data']['list']
print(article_list)

dir_path = os.getcwd() + '/html/'

if not os.path.exists(dir_path):
    os.mkdir(dir_path)

for article in article_list:
    print(article['title'])
    print(article['url'])
    print('---------------')
    # 将html转pdf，需要安装pdfkit模块 pip install pdfkit
    # 同时电脑上需要安装wkhtmltopdf软件   wkhtmltopdf下载地址：https://wkhtmltopdf.org/downloads.html
    # 在线转pdf
    # pdfkit.from_url(article['url'], dir_path + article['title'] + '.pdf')

    article_html = requests.get(article['url'], headers=header)
    selector = parsel.Selector(article_html.text)
    article_content = selector.xpath('//div[@class="blog-content-box"]').get()
    html_path = dir_path + article['title'] + '.html'
    pdf_path = dir_path + article['title'] + '.pdf'
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(article_content)
    pdfkit.from_file(html_path, pdf_path, options={'encoding': 'utf-8'})
