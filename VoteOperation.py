import requests as r
import json as js
voteurl='http://api.bilibili.com/x/credit/jury/vote'

voteaction={
    'Break': 1,
    'Rule': 2,
    "GiveUp": 3,
    'Delete': 4
}

def Vote(opreation,cid,csrf,sessdata):
    headers={
        'cookie': 'SESSDATA={}'.format(sessdata),
        'referer': "https://www.bilibili.com/",
        'origin': "https://www.bilibili.com/",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
    }
    params={
        'cid': cid,
        'vote': voteaction[opreation],
        'attr': 0,
        'csrf': csrf
    }
    VoteReturn=r.post(voteurl,params=params,headers=headers).text
    VoteResult=js.dumps(VoteReturn)
    return VoteResult