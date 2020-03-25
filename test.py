


import dd_send_msg
import time

mobile = ['15***260','1343***946','1343***10',
            '153***22','17***197','187***23','186***36']

while True:
    if time.localtime(time.time()).tm_wday < 5:
        if time.localtime(time.time()).tm_hour == 8 and time.localtime(time.time()).tm_min == 54 :
                re_msg = dd_send_msg.send_Dingmsg(data = {"msgtype": "text", "text": { "content": "a"}, "at": {"atMobiles": mobile, "isAtAll": False}})
                print (re_msg)
                time.sleep(60)
        if time.localtime(time.time()).tm_hour == 17 and time.localtime(time.time()).tm_min == 29:
                re_msg = dd_send_msg.send_Dingmsg(data = {"msgtype": "text", "text": { "content": "a"}, "at": {"atMobiles": mobile, "isAtAll": False}})
                print (re_msg)
                time.sleep(60)
    time.sleep(30)