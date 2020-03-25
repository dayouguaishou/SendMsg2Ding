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

3.示例代码
```Python
'''
上下班打卡提醒机器人
'''
import dd_send_msg
import time

mobile = ['15***0','1***6','13***10',
            '153***122','173***197','187***323','186***636']

while True:
    if time.localtime(time.time()).tm_wday < 5:
        if time.localtime(time.time()).tm_hour == 8:
            if time.localtime(time.time()).tm_min == 54:
                re_msg = dd_send_msg.send_Dingmsg(data = {"msgtype": "text", "text": { "content": "温馨提示：疫情填报，上班打卡！"}, "at": {"atMobiles": mobile, "isAtAll": False}})
                print (re_msg)
                time.sleep(60)
        if time.localtime(time.time()).tm_hour == 17:
            if time.localtime(time.time()).tm_min == 29:
                re_msg = dd_send_msg.send_Dingmsg(data = {"msgtype": "text", "text": { "content": "温馨提示：下班打卡，填写日报！"}, "at": {"atMobiles": mobile, "isAtAll": False}})
                print (re_msg)
                time.sleep(60)
    time.sleep(30)

``` 
