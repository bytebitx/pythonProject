import requests

url = "https://www.poco.cn/?classify_type=1&works_type=medal"

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '393',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'web-api.poco.cn',
    'Origin': 'https://www.poco.cn',
    'Referer': 'https://www.poco.cn/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

response = requests.get("https://www.poco.cn/?classify_type=1&works_type=medal", headers=headers)
print(response.text)