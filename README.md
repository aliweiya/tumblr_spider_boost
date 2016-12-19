# tumblr_spider_boost
汤不热 python 多线程爬虫增强版
1. 增加了二级解析,最终获取可以下载的 url 地址
2. 增加图片解析

#### install
> pip install -r requirements.txt


#### run
> python tumblr.py username (usename 为任意一个热门博主的 usename)

#### 爬取结果
> `user.txt` 是爬取的博主用户名结果， `source.txt` 是视频地址集, `img.txt` 图片地址集

#### 原理
> 根据一个热门博主的 usename, 脚本自动会获取博主转过文章的其他博主的 username，并放入爬取队列中，递归爬取。

#### 申明
> 这是一个正经的爬虫（严肃脸），爬取的资源跟你第一个填入的 username 有很大关系，另外由于某些原因，导致 tumblr 被墙，所以最简单的方式就是用国外 vps 去跑。

此项目是 fork `https://github.com/facert/tumblr_spider` 然后修改了一下,感谢原作者

#### 文件说明
1. tumblr.py 主程序, 爬取关联的用户名, video 地址,图片地址
2. analysis.py 将原来还没有二级解析出来的 url 地址进行二次解析获取可下载的 url 地址
3. analysis_html.py 测试
4. filtrate.py 将原来二次解析的结果再次处理一下,不然下载的时候名字会乱
5. image.py 图片解析测试
6. mysql.py 测试 
7. thread_demo.py 测试
