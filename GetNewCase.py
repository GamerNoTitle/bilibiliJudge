import requests as r
import json as js

url='http://api.bilibili.com/x/credit/jury/caseObtain'

def GetNew(csrf,sessdata):
    headers={
        'cookie': 'bili_jct={}; SESSDATA={}'.format(csrf,sessdata),
        'referer': "https://www.bilibili.com/",
        'origin': "https://www.bilibili.com/",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
    }
    params={
        'csrf': csrf
    }
    data=r.post(url,headers=headers,params=params)
    dataloads=js.loads(data.text)
    # print(dataloads)
    if(dataloads['code']==25014 or dataloads['code']==25008): return True
    result=dataloads['data']['id']
    return result
