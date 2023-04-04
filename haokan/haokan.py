import pprint
import time

import parsel
import requests

app_id = '1756519291876935'

url = 'https://haokan.baidu.com/author/1756519291876935'

headers = {
    'authority': 'haokan.baidu.com',
    'method': 'GET',
    'path': '/web/author/listall?app_id=1756519291876935&ctime=&video_type=haokan%7CtabhubVideo&rn=20',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'referer': 'https://haokan.baidu.com/author/1756519291876935',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'cookie': 'BIDUPSID=F2B9E50102E72EE4DB6902EE2EF00973; PSTM=1660272537; BAIDUID=F2B9E50102E72EE49286EEAF7C38D725:SL=0:NR=10:FG=1; MCITY=-340%3A; BDUSS=xTVENCSmZqfmFoUlpkNk85emZLT0E2alRsdlRYNDBEWkhqNmh3SGZjWDY0SDVqSVFBQUFBJCQAAAAAAAAAAAEAAAAOx~QgeXlzdXNlMTIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPpTV2P6U1djcU; BDUSS_BFESS=xTVENCSmZqfmFoUlpkNk85emZLT0E2alRsdlRYNDBEWkhqNmh3SGZjWDY0SDVqSVFBQUFBJCQAAAAAAAAAAAEAAAAOx~QgeXlzdXNlMTIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPpTV2P6U1djcU; PC_TAB_LOG=video_details_page; COMMON_LID=1fe1610709d5729660e16dfb18486acb; hkpcvideolandquery=%u96BE%u9053%u59D0%u59D0%u4E0D%u61C2%u56DE%u623F%u95F4%u7761%u89C9%u5417%uFF1F%u975E%u8981%u8DDF%u6211%u62A2%u6C99%u53D1; hkpcSearch=%u5C0F%u5E08%u59B9%24%24%24%u5305%u81C0%u88D9%24%24%24%u7F8E%u5973; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=E9-OJeC62Gs3PN7f2AB_UG91_gK5dk5TH6aoASxQBixOkqdZ0Js9EG0PXx8g0Kub6T3qogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJKf_DtKtKK3DbbwD5L_-JL3MMrXKC62aKDsaRR1BhcqEIL4jPJ2qfPqbG_J-J5P3b5EbxT-3p5OVfbSj4QoLR-pMJ600qc35TQbbnoaWp5nhMJkXj7JDMn3-xrMQDry523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DTjLDGKfJjks5IrH05r22Rj_jRTzbtOE-DCShUFs06FLB2Q-5KL-3-85Vhu6b65NLl4AQNuDy-biJCnW_xbdJJjoEfO90f5E2M4fKfOzJUTefmTxoUJ9MInJhhvG-6jxDn_ebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjDajTbP; PSINO=7; BA_HECTOR=agalah8l0k0g8020852g0h6k1i2l4qd1m; BAIDUID_BFESS=F2B9E50102E72EE49286EEAF7C38D725:SL=0:NR=10:FG=1; BDSFRCVID_BFESS=E9-OJeC62Gs3PN7f2AB_UG91_gK5dk5TH6aoASxQBixOkqdZ0Js9EG0PXx8g0Kub6T3qogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJKf_DtKtKK3DbbwD5L_-JL3MMrXKC62aKDsaRR1BhcqEIL4jPJ2qfPqbG_J-J5P3b5EbxT-3p5OVfbSj4QoLR-pMJ600qc35TQbbnoaWp5nhMJkXj7JDMn3-xrMQDry523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DTjLDGKfJjks5IrH05r22Rj_jRTzbtOE-DCShUFs06FLB2Q-5KL-3-85Vhu6b65NLl4AQNuDy-biJCnW_xbdJJjoEfO90f5E2M4fKfOzJUTefmTxoUJ9MInJhhvG-6jxDn_ebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjDajTbP; ZFY=MicpQ:BJ502C86qyTWsdiPbxttEiPrrjPz:BVWzd0ORQU:C; delPer=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1680521121; ab_sr=1.0.1_YmIzZjEzYjQwZThhODMyM2Q3NDU0NTc2OGIyNDMzY2RjODE2NmZjOGU0ZDEyNGQyM2Y3Zjk4YmUwM2E0MWJkZWRmNTJlOTA1ZjM3OTUxMmRhZDhkODAxNWVmMWQ4NTE2OGY1NTM4MTM4ODA4MGUyNzdhZDgyNDM1YzRjODljODhjNzdhYjMyMGI0MGJjOGY1YTEwMmE4ZTBiYTQzNGFlOA==; reptileData=%7B%22data%22%3A%2294ade6d3b91d9b0eb397b911cb6d6d70c3cab4675631f5807a889e15b99ec2b53a4db060480dec38a88c7e5895ba6728c918a1282b3e8daaeadad5d241d357bd290972cec1afd4766cee9dc6aa2c235bc6357f0e8f5f6d1c7ecd88dce05a5f0b%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%222a5cd79f%22%7D; H_PS_PSSID=38185_36547_38105_38470_38344_38398_38468_38290_38486_38261_37930_38382_26350_38420_38283_37881; ariaDefaultTheme=undefined; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1680526757; RT="z=1&dm=baidu.com&si=293c1a0a-478a-4dfc-8eda-a7fc0f24c0da&ss=lg0rvdk0&sl=1&tt=lw&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2dc0i"'
}

headers2 = {
    'authority': 'haokan.baidu.com',
    'method': 'GET',
    'path': '/v?vid=4397896741950603110&collection_id=',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'referer': 'https://haokan.baidu.com/author/1756519291876935',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'cookie': 'BIDUPSID=F2B9E50102E72EE4DB6902EE2EF00973; PSTM=1660272537; BAIDUID=F2B9E50102E72EE49286EEAF7C38D725:SL=0:NR=10:FG=1; MCITY=-340%3A; BDUSS=xTVENCSmZqfmFoUlpkNk85emZLT0E2alRsdlRYNDBEWkhqNmh3SGZjWDY0SDVqSVFBQUFBJCQAAAAAAAAAAAEAAAAOx~QgeXlzdXNlMTIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPpTV2P6U1djcU; BDUSS_BFESS=xTVENCSmZqfmFoUlpkNk85emZLT0E2alRsdlRYNDBEWkhqNmh3SGZjWDY0SDVqSVFBQUFBJCQAAAAAAAAAAAEAAAAOx~QgeXlzdXNlMTIzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPpTV2P6U1djcU; PC_TAB_LOG=video_details_page; COMMON_LID=1fe1610709d5729660e16dfb18486acb; hkpcvideolandquery=%u96BE%u9053%u59D0%u59D0%u4E0D%u61C2%u56DE%u623F%u95F4%u7761%u89C9%u5417%uFF1F%u975E%u8981%u8DDF%u6211%u62A2%u6C99%u53D1; hkpcSearch=%u5C0F%u5E08%u59B9%24%24%24%u5305%u81C0%u88D9%24%24%24%u7F8E%u5973; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=E9-OJeC62Gs3PN7f2AB_UG91_gK5dk5TH6aoASxQBixOkqdZ0Js9EG0PXx8g0Kub6T3qogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJKf_DtKtKK3DbbwD5L_-JL3MMrXKC62aKDsaRR1BhcqEIL4jPJ2qfPqbG_J-J5P3b5EbxT-3p5OVfbSj4QoLR-pMJ600qc35TQbbnoaWp5nhMJkXj7JDMn3-xrMQDry523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DTjLDGKfJjks5IrH05r22Rj_jRTzbtOE-DCShUFs06FLB2Q-5KL-3-85Vhu6b65NLl4AQNuDy-biJCnW_xbdJJjoEfO90f5E2M4fKfOzJUTefmTxoUJ9MInJhhvG-6jxDn_ebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjDajTbP; PSINO=7; BA_HECTOR=agalah8l0k0g8020852g0h6k1i2l4qd1m; BAIDUID_BFESS=F2B9E50102E72EE49286EEAF7C38D725:SL=0:NR=10:FG=1; BDSFRCVID_BFESS=E9-OJeC62Gs3PN7f2AB_UG91_gK5dk5TH6aoASxQBixOkqdZ0Js9EG0PXx8g0Kub6T3qogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJKf_DtKtKK3DbbwD5L_-JL3MMrXKC62aKDsaRR1BhcqEIL4jPJ2qfPqbG_J-J5P3b5EbxT-3p5OVfbSj4QoLR-pMJ600qc35TQbbnoaWp5nhMJkXj7JDMn3-xrMQDry523iob3vQpPMVhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DTjLDGKfJjks5IrH05r22Rj_jRTzbtOE-DCShUFs06FLB2Q-5KL-3-85Vhu6b65NLl4AQNuDy-biJCnW_xbdJJjoEfO90f5E2M4fKfOzJUTefmTxoUJ9MInJhhvG-6jxDn_ebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjDajTbP; ZFY=MicpQ:BJ502C86qyTWsdiPbxttEiPrrjPz:BVWzd0ORQU:C; delPer=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1680521121; H_PS_PSSID=38185_36547_38470_38344_38398_38468_38290_38486_38261_37930_38356_26350_38420_38283_37881; ab_sr=1.0.1_Mzg5OTkwMGI0M2Y2ZWNhZWM4N2RjZGVmOGYyZmM2MTVkNThiMGZkZGFkNGIzM2IxYjZmNTg4YzQxMzVkY2VlZDgyYTVjMDE3NzI1NThkZDk1YzE0NzZhNTdkMmY1ZmFmOTY2NDI1MGM0ZTM4OGZkYTZiNjI4ODVhNTlmZDE0MTQyYTVhMTYwYzAyMjdjOTMxNzE1NjQyYjIxMGZlOTNjNA==; reptileData=%7B%22data%22%3A%2294ade6d3b91d9b0eb397b911cb6d6d70c3cab4675631f5807a889e15b99ec2b53a4db060480dec38a88c7e5895ba6728c918a1282b3e8daaeadad5d241d357bd2c2188e5beb0b28e3d152b2bc62f093564711078e89b55b67524f7f5541d5b0d%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%228832e3f5%22%7D; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1680595089; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=293c1a0a-478a-4dfc-8eda-a7fc0f24c0da&ss=lg1x96vq&sl=b&tt=dcz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1fj2a&ul=22y24"'
}

time = time.time()
# datas = '1756519291876935&ctime=&video_type=pay_column&rn=40'
data = 'app_id=1756519291876935&ctime=16769890062173&rn=20&searchAfter=&_api=1'
response = requests.get(url=url, headers=headers)
# print(response.text)
selector = parsel.Selector(response.text)
list = selector.xpath('//div[@class="skeleton-video"]/a/@href').getagitll()
for url in list:
    req_url = 'https://haokan.baidu.com/' + url + '&collection_id='
    res = requests.get(req_url, headers=headers2)
    print(res.text)
    # selector = parsel.Selector(res.text)
    # video_url = selector.xpath('//div[@class="art-video-player art-subtitle-show art-layer-show art-control-show art-mask-show"]/video/@src').get()
    # print(video_url)
# print(list)
# print(len(response.json()['data']['results']))
