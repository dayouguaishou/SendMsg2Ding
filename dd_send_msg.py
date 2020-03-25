# coding=utf-8
'''
日志：
0.新建测试代码。 By wei.wei in 202003041850
1.修改导入库至Python3.X版本。 By wei.wei in 202003052247
2.将测试文件dd_test.py转为函数，方便调用。By wei.wei in 202003232033

说明：
实际调用库及测试代码。
Python3.X测试通过
修改为调用参数的函数。


使用方法：
0.导入库
1.调用函数

'''

import d_key
import d_send


def send_Dingmsg(url = 'https://oapi.dingtalk.com/robot/send?access_token=*******************',
                keys_str = 'SEC**************239a',
                data = {"msgtype": "text","text": {"content": "这是一条测试消息"},}):
    keys = str(d_key.signs(keys_str))
    send_url = url+keys
    return (d_send.send_msg(send_url,data))#返回服务参数


#print (send_Dingmsg(url = 'https://oapi.dingtalk.com/robot/send?access_token=6*******1',keys_str = 'SEC****239a',))
