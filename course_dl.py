import requests
import json
import os

def sec(course_id):
    url1=f'https://kpapiop.ckjr001.com/api/column/getCourses/{course_id}?limit=10000'
    #添加请求头
    headers = {
        'authorization': 'Bearer 在此处填入你的Bearer，可以从浏览器的开发者工具中获取。'
    }
    response_1=requests.get(url1, headers=headers)
    response_1.encoding='utf-8'
    c=response_1.text
    d=json.loads(c)
    print(c)
    for i in d['data']['data']:
        os.system(f"youtube-dl -o{i['name']}.mp4 {i['assets']['items'][0]['videoUrl']}")

sec(input('course_id:'))
