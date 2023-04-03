# pythonProject
python


常用的爬虫工具汇总 https://blog.csdn.net/mouday/article/details/83026074  
parsel标签选择器使用方式 https://blog.csdn.net/zxctime/article/details/106962727

安装镜像：pip install parsel -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com

python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ttkbootstrap



python帮助文档
https://docs.python.org/zh-cn/3.10/index.html

ttk帮助文档
https://docs.python.org/zh-cn/3/library/tkinter.ttk.html

tkinter帮助文档
https://tkdocs.com/shipman/


aiohttp get没有stream=True这个属性

同步方式下载文件：
```angular2html
with open(dir_path + name + '.jpg', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
同步方式没有response.content.iter_chunked(1024)
```
        

异步方式下载文件：
```angular2html
with open(dir_path + name + '.mp4', 'wb') as file:
    async for chunk in down_response.content.iter_chunked(1024):
        file.write(chunk)


下载类似m3u8格式的文件：
with open(dir_path + name, 'ab') as file:
    while True:
        chunk = await down_response.content.read(1024)
        if not chunk:
            break
        file.write(chunk)
```


