import json as js

def Parse(info):
    case=js.loads(info)['data']
    status={
        1: '投票中',
        2: '停止发放',
        3: '复核中（结案中）',
        4: '已裁决',
        5: '待重启',
        6: '未裁决',
        7: '冻结中',
        8: '队列中'
    }
    result=str({
        '案件ID': case['id'],
        '被举报用户ID': case['mid'],
        '裁决状态': status[int(case['status'])],
        '被举报原文': case['originContent'],
        '来源URL': case['originUrl'],
        '删除投票': case['voteDelete'],
        '封禁投票': case['voteBreak'],
        '合规投票': case['voteRule']
    })
    return result,int(case['status'])