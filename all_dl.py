import requests
import json
import os

headers = {
    'authorization': 'Bearer 在此处填入你的Bearer，可以从浏览器的开发者工具中获取。'
}


def sec(course_id, dir):
    url1 = f'https://kpapiop.ckjr001.com/api/column/getCourses/{course_id}?limit=10000'
    response_1 = requests.get(url1, headers=headers)
    response_1.encoding = 'utf-8'
    c = response_1.text
    d = json.loads(c)
    id = 0
    for i in d['data']['data']:
        id += 1
        file_name = os.path.join(dir, str(id).zfill(4)+'-'+i['name']+'.mp4')
        if os.path.exists(file_name):
            continue
        os.system(f"yt-dlp -N 16 -o {file_name} {i['assets']['items'][0]['videoUrl']}")


def get_all():
    url1 = 'https://kpapiop.ckjr001.com/api/company/customTemplates?themeName=mb8&fromApp=oa'
    response_1 = requests.get(url1, headers=headers)
    response_1.encoding = 'utf-8'
    c = json.loads(response_1.text)
    for i in c['data']['modules']:
        if i['modelType'] == 7:
            for prod in i['items']['prods']:
                pat = os.path.join(i['name'], prod['name'])
                os.makedirs(pat, exist_ok=True)
                r = requests.get(prod['cover'])
                if r.status_code == 200:
                    with open(os.path.join(pat, 'cover.jpg'), 'wb') as f:
                        f.write(r.content)
                sec(prod['columnId'], pat)


get_all()
