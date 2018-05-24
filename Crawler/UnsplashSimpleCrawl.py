# -*- coding:UTF-8 -*-
import json
import requests

if __name__ == '__main__':
    target = 'http://unsplash.com/napi/feeds/home'
    # client-ID 替换为抓取到的
    CLIENT_ID = 'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'
    headers = {'authorization': CLIENT_ID}
    req = requests.get(url=target, headers=headers, verify=False)
    jsonData = json.loads(req.text)
    next_page = jsonData['next_page']
    print('下一页地址:', next_page)
    for each in jsonData['photos']:
        print('图片ID:', each['id'])
