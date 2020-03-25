基于Python3的推送信息至钉钉群
===
参考钉钉机器人开发文档  
https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq  
注意：开发文档上的签名计算代码示例代码基于Python2.7  

1.在钉钉群中添加机器人（参考钉钉机器人开发文档），获取Webhook及安全设置加签。 

2.在自己的程序导入  

```Python
import dd_send_msg
```  

3.消息类型  
```
data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"MarkDown 测试",
         "text": "# 一级标题 \n" +
                 "## 二级标题 \n" +
                 "### 三级标题 \n" +
                 "#### 四级标题 \n" +
                 "##### 五级标题 \n" +
                 "###### 六级标题 \n" +
                 "**bold** \n"+
                 "*italic* \n"+
                 "![](http://name.com/pic.jpg) \n"+
                 ">- 无序列表1  \n"+
                 ">- 无序列表2  \n"+
                 "1. 有序列表1  \n"+
                 "2. 有序列表2  \n"+
                 "> A man who stands for nothing will fall for anything.\n"
     }}
```


```
data = {
    "msgtype": "text", 
    "text": {
        "content": "我就是我, 是不一样的烟火@156xxxx8827"
    }, 
    "at": {
        "atMobiles": [
            "156xxxx8827", 
            "189xxxx8325"
        ], 
        "isAtAll": false
    }
}
```

```
data = {
    "msgtype": "link", 
    "link": {
        "text": "这个即将发布的新版本，创始人xx称它为“红树林”。
而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？", 
        "title": "时代的火车向前开", 
        "picUrl": "", 
        "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI"
    }
}
```

4.示例代码
```Python
'''
上下班打卡提醒机器人
'''
import dd_send_msg
import time

mobile = ['15***0','1***6','13***10',
            '153***122','173***197','187***323','186***636']

while True:
    if time.localtime(time.time()).tm_wday < 5:#周一到周五
        if time.localtime(time.time()).tm_hour == 8:#8点
            if time.localtime(time.time()).tm_min == 54:#54分
                re_msg = dd_send_msg.send_Dingmsg(data = {"msgtype": "text", "text": { "content": "温馨提示：疫情填报，上班打卡！"}, "at": {"atMobiles": mobile, "isAtAll": False}})
                print (re_msg)
                time.sleep(60)
        if time.localtime(time.time()).tm_hour == 17:#17点
            if time.localtime(time.time()).tm_min == 29:#29分
                re_msg = dd_send_msg.send_Dingmsg(data = {"msgtype": "text", "text": { "content": "温馨提示：下班打卡，填写日报！"}, "at": {"atMobiles": mobile, "isAtAll": False}})
                print (re_msg)
                time.sleep(60)
    time.sleep(30)

``` 
