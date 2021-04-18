from CaseInfo import GetCase
from VoteOperationCalculate import VoteCalculate
from VoteOperation import Vote
from CaseParser import Parse
from GetJudgerInfo import GetInfo
from GetNewCase import GetNew
from JudgementApply import Apply
import sys
import json as js
import time
import random
import os

class VariableError(Exception):
    pass

csrf=os.environ.get("csrf","")
sessdata=os.environ.get("SESSDATA","")
if(csrf=='' or sessdata==''):
    print('必要变量未设置！程序即将退出！')
    raise(VariableError('Essential variable(s) not available!'))
    sys.exit()

try:
    GiveUpEnable=os.environ.get("GiveUpEnable","")
    GiveUpEnableDisplay='是'
    if GiveUpEnable=='False':
        GiveUpEnable=False
        GiveUpEnableDisplay='否'
except:
    GiveUpEnable=True
    GiveUpEnableDisplay='是'

try:
    delay=int(os.environ.get("delay",""))
except:
    delay=300

try:
    JudgeProportion=float(os.environ.get("JudgeProportion",""))
    if not(JudgeProportion<1 and JudgeProportion>0):
        JudgeProportion=0.7
except:
    JudgeProportion=0.7

GiveupConfig='检测到放弃选项的开启状态为：{}，判定比例为：{}%，即将开始运行判定程序！'.format(GiveUpEnableDisplay,JudgeProportion*100)
print(GiveupConfig)
ApplyResult=None
cannotJudge=False

def GetAndCal(cid):
    case=GetCase(cid).text
    caseinfo=js.loads(case)
    printinfo,casestatus=Parse(case)
    toprint='''
获取到风纪委员案件（ID：{}），具体信息如下：
{}
    '''.format(cid,printinfo)
    print(toprint)
    voteBreak=caseinfo['data']['voteBreak']
    voteDelete=caseinfo['data']['voteDelete']
    voteRule=caseinfo['data']['voteRule']
    return voteBreak,voteDelete,voteRule,caseinfo,casestatus


def Main():
    Userinfo,UserinfoParsed=GetInfo(sessdata)
    print('获取到用户信息，具体如下：')
    print(UserinfoParsed)
    if(Userinfo['data']['status']==2):
        print('检测到未具有风纪委员资格，正在尝试申请……')
        global ApplyResult
        ApplyResult,ApplyMsg=Apply(sessdata,csrf)
        if(ApplyResult):
            print('风纪委员资格申请成功，正在执行脚本操作……')
        elif(not ApplyResult):
            print('申请风纪委员资格失败，{}，脚本即将退出！'.format(ApplyMsg))
            sys.exit()
    while True:
        print('正在进行下一案件的获取……')
        cid=GetNew(csrf,sessdata)
        if(cid==True):
            print('今天案件已经审核满或没有需要仲裁的案件了，明天我们再继续吧~')
            sys.exit()
        voteBreak,voteDelete,voteRule,caseinfo,casestatus=GetAndCal(cid)
        operation,operation_print=VoteCalculate(voteBreak,voteDelete,voteRule,GiveUpEnable,JudgeProportion)
        if casestatus==4:
            print('当前案件已裁决完毕，即将进行下一案件的审理……')
            continue
        while True:
            if(operation=='CannotJudge'):
                print('目前案件{}的投票数量不足以判定操作，将在{}秒钟后重试！'.format(caseinfo['data']['id'],delay))
                global cannotJudge
                cannotJudge=True
                time.sleep(delay)
                voteBreak,voteDelete,voteRule,caseinfo,caseStatus=GetAndCal(cid)
                operation,operation_print=VoteCalculate(voteBreak,voteDelete,voteRule,GiveUpEnable,JudgeProportion)
            else:
                cannotJudge=False
                break
        randomtime=random.randint(10,600)
        print('将等待{}秒后进行判定'.format(randomtime))
        time.sleep(randomtime)
        operation_output='案件{}的投票结果计算为{}，正在进行投票操作……'.format(caseinfo['data']['id'],operation_print)
        print(operation_output)
        Vote(operation,cid,csrf,sessdata)
        print('已完成投票操作！')
        
    

if __name__ == "__main__":
    Main()
