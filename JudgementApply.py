import requests as r
import json as js

checkurl='http://api.bilibili.com/x/credit/jury/requirement'
applyurl='http://api.bilibili.com/x/credit/jury/apply'
avaliability=False

def Apply(sessdata,csrf):
    headers={
        'cookie': 'SESSDATA={}'.format(sessdata),
        'referer': "https://www.bilibili.com/",
        'origin': "https://www.bilibili.com/",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
    }
    result=js.loads(r.get(checkurl,headers=headers).text)
    blocked,cert,level,rule=result['data']['blocked'],result['data']['cert'],result['data']['level'],result['data']['rule']
    if(not blocked and cert and level and rule):
        global avaliability
        avaliability=True
    headers={
        'cookie': 'bili_jct={}; SESSDATA={}'.format(csrf,sessdata)
    }
    params={
        'csrf': csrf
    }
    if(avaliability):
        print('检测到未有风纪委员资格但具有申请资格，正在尝试申请……')
        result=js.loads(r.post(applyurl,headers=headers,params=params).text)
        print(result)
        if result['code']==0:
            returnmsg='申请成功'
            return True,returnmsg
        else:
            status={
                -101: '返回错误码-101，账号未登录，请检查sessdata和csrf是否有效',
                -111: '返回错误码-111，csrf校验失败，请检查csrf是否有效',
                25016: '返回错误码25016，当天的风纪委员资格已经发放完成'
            }
            returnmsg=status[result['code']]
            return False,returnmsg

