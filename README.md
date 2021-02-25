# 风纪委员会自动投票

本脚本通过使用Github Action来实现B站风纪委员的自动投票功能，喜欢请给我点个STAR吧！

如果你不是风纪委员，在符合风纪委员申请条件的情况下，本脚本会自动帮你申请

**为了让其他风纪委员避免因为脚本而没有案子判**，本脚本的投票时间是中午12点到晚上22点每小时一次，如果有需要请自行修改`.github/workflows/Judge.yml`中的时间，时间是UTC时区的时间，需要将时位+8才是北京时间

## 免责声明

学习项目，请勿滥用！如果有因滥用造成的封号、删除账户等情况或违反相关法律所造成的责任，本人拒不承担！

## 赞助

点击下面的Badge其中一个就可以跳转到相应页面，感谢老板的支持！

<a href="https://afdian.net/@GamerNoTitle"><img src="https://img.shields.io/badge/%E7%88%B1%E5%8F%91%E7%94%B5-GamerNoTitle-%238e8cd8?style=for-the-badge" alt="前往爱发电赞助" width=auto height=auto border="0" /></a> <a href="https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo@master/img/Donate/WeChatPay.png"><img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1%E6%94%AF%E4%BB%98-GamerNoTitle-%2304BE02?style=for-the-badge" alt="使用微信赞助" width=auto height=auto border="0" /></a> <a href="https://cdn.jsdelivr.net/gh/GamerNoTitle/Picture-repo@master/img/Donate/AliPay.jpg"><img src="https://img.shields.io/badge/%E6%94%AF%E4%BB%98%E5%AE%9D%E6%94%AF%E4%BB%98-GamerNoTitle-%231678FF?style=for-the-badge" alt="使用支付宝赞助" width=auto height=auto border="0" /></a>

## 目录

- [使用方法](#使用方法)
- [保活策略](#保活策略)
- [变量获取](#变量获取)
    - [csrf与sessdata](#csrf与sessdata)
    - [giveup与delay](#giveup与delay)
    - [JudgeProportion](#JudgeProportion)
- [脚本测试](#脚本测试)
- [脚本更新](#脚本更新)
- [Q&A](#QA)
- [免责声明](#免责声明)

## 从零开始的使用指北☞

### 使用方法

1、Fork本仓库，直接点击右上角的Fork图标，然后将项目选择到你的账户下即可

![](https://upimage.alexhchu.com/2021/01/26/55beb284a6a45.png)

2、进入设置，添加变量必需变量`csrf`和`sessdata`，另有`giveup`和`delay`可选变量可以添加

**请注意：你无需在仓库的secrets内设置名为`GITHUB_TOKEN`的变量，该名称本身就是指定为自己账户下名为`GITHUB_TOKEN`的密钥，如果你在仓库的secrets内设置将会被Github提示无效**

[如何获取变量内容？请点这里](#变量获取)

![](https://upimage.alexhchu.com/2021/01/26/404fb80a80b5a.png)

![](https://upimage.alexhchu.com/2021/01/26/b2d3f92a2a9c3.png)

### 保活策略

因为Github Action在仓库60天内没有任何Push的时候会禁用你的Action，这时候我们就要进行保活

保活Action已经写好了，但是这里有一些步骤是需要你进行的，请看下面的图片生成GITHUB_TOKEN以便让脚本造成的更改能够正常推送入你的仓库

![](https://upimage.alexhchu.com/2020/12/27/dce7070ae625c.png)

![](https://upimage.alexhchu.com/2020/12/27/f82f6505503ed.png)

![](https://upimage.alexhchu.com/2020/12/27/9cff0436399b7.png)

到这里勾选完以后点绿绿的Generate token就可以了

### 变量获取

#### csrf与sessdata

首先我们打开B站，直接在B站的网址后面加上`/judgement`，或者直接访问[https://bilibili.com/judgement](https://bilibili.com/judgement)，按下键盘上的<kbd>F12</kbd>，打开开发者工具

接着我们点到上面的`Network`（有些写的是`网络`，例如Edge），在左边找到index项，然后点击它，在右侧找到cookie这一个键，然后复制`SESSDATA=`到`;`的内容作为`sessdata`和`bili_jct=`到`;`的内容作为csrf

**请注意：不要把分号弄进去了！不要分号！不要分号！（重要的事情说三遍）**

![](https://upimage.alexhchu.com/2021/01/26/a892c4e380db5.png)

#### giveup与delay

这是两个我设定的值，因为B站对于案件有`放弃`这一说，所以我对它特别加了个开关

如果你不想让脚本对案件采用放弃的操作，那么就要添加Giveup这个值，而且必须填上`False`，否则一律当允许放弃处理；还有一个delay是不放弃的话等待多长时间以后再次进行操作计算，以秒为单位，必须是整数，不填就默认为`300`秒

#### JudgeProportion

这是一个设定赞成比例的值，默认设定的是0.7，即赞成票占全部的70%就选择赞成中票数较高的操作，或合规票占全部的70%（即违规占30%）时就投合规，否则进入放弃/等待阶段，这个数字必须是大于0且小于1的小数！若输入无效数字按默认值处理！

### 脚本测试

我们先进入Action界面，启用Action（因为我这里忘记截图了，所以用我隔壁的那个[网易云游戏签到脚本](https://github.com/GamerNoTitle/wyycg-autocheckin/)来顶一下）

![](https://upimage.alexhchu.com/2020/11/22/70dd262ae54f0.png)

然后我们进入对应的脚本，启用脚本，并进行测试

![](https://upimage.alexhchu.com/2021/01/26/d5399493a1f5f.png)

![](https://upimage.alexhchu.com/2021/01/26/9c9dfd7b61e15.png)

只要打了绿色的勾勾就是成功了，然后你就不用管它了，它会自己运行的

![](https://upimage.alexhchu.com/2021/01/26/8efbde4e57684.png)

### 脚本更新

#### 自动更新（推荐）

[点击这里](https://github.com/apps/pull)安装插件，可以选择所有仓库，也可以指选择你Fork的仓库（当然至少要选择fork的仓库对吧，要不然怎么更新），然后不管它就好了

详细步骤可以看下面的图片

![](https://upimage.alexhchu.com/2020/12/26/4c0d02795a38c.png)

![](https://upimage.alexhchu.com/2020/12/26/1800e5609a365.png)

![](https://upimage.alexhchu.com/2021/01/26/6231f85828022.png)

#### 手动更新

具体看图，**请注意：以下操作均在自己的仓库进行！**

![](https://upimage.alexhchu.com/2021/01/26/b53b4f1301be5.png)

![](https://upimage.alexhchu.com/2021/01/26/5d7656029f6ed.png)

![](https://upimage.alexhchu.com/2021/01/26/ae3350e1b41ea.png)

![](https://upimage.alexhchu.com/2021/01/26/623081081b089.png)

![](https://upimage.alexhchu.com/2021/01/26/99c5b116e6f53.png)

![](https://upimage.alexhchu.com/2021/01/26/a75295ba9c1bc.png)

这样你就完成了手动更新操作！

#### Q&A

##### __main__.VariableError: Essential variable(s) not available!

这种情况下请检查你的变量是否填好，如果`csrf`和`sessdata`不填好就会出现这个错误

如何检查自己的变量是否填好？你可以点开当次Action记录中的`Run Script`这一节，然后点击`Run python3 Main.py "$csrf" "$sessdata" "$giveup" "$delay" "$JudgeProportion"`这一行把它展开，看看自己的变量是否填写完整，它不会显示你填写的变量，但是填了的变量会以`***`来显示来告诉你你填写了

##### 用户名一节：KeyError

```
Traceback (most recent call last):
  File "Main.py", line 112, in <module>
    Main()
  File "Main.py", line 67, in Main
    Userinfo,UserinfoParsed=GetInfo(sessdata)
  File "/home/runner/work/bilibiliJudge/bilibiliJudge/GetJudgerInfo.py", line 18, in GetInfo
    '用户名': info_loads['data']['uname'][0]+ ('*' * int(len(info_loads['data']['uname'])-2)) +info_loads['data']['uname'][len(info_loads['data']['uname'])-1:],
KeyError: 'data'
```

在`GetJudgerInfo.py`文件中，第十二行

```python
    info_loads=js.loads(info.text)
```

下面加多一行`print(info_loads)`，如下面这样

```python
    info_loads=js.loads(info.text)
    print(info_loads)
```

并发起issue询问（当然你能自己看懂是什么情况是最好的）

## 免责声明


