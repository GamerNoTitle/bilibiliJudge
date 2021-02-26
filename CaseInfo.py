import requests as r

caseurl='http://api.bilibili.com/x/credit/jury/caseInfo'

def GetCase(cid):
    params={'cid': cid}
    info=r.get(caseurl,params=params,headers=headers)
    return info