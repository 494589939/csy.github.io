#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# zabbix notification confirmation script
# python3.6 or above
# python 企业微信接口测试,需要注意的是，所有的接口需使用Https协议、Json数据格式、UTF8编码。

import requests
import json
import os
import sys


# POST发送信息
def send_message(access_token, title, message):
    # 定义POST请求字典
    data = {
        "touser": "这里填自己的用户名",
        "toparty": "这里填要接收部门",
        "msgtype": "text",
        "agentid": 这里填部门ID,
        "text": {
            "content": '故障标题：' + title + '\n' + '故障详情：' + message
        },
        "safe": 0
    }

    # 用 json 将 dict转换成json格式传给微信服务器
    payload = json.dumps(data)
    post_message = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(
        access_token)
    p = requests.post(post_message, payload)
    print(p.json())


if __name__ == '__main__':
    # 获取access_token
    get_https = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww7aa25663557cd46b&corpsecret=HiF-uxZotGbMoeLmBgjjWuuz3SBRIalNnKolNO7A4mA"
    g = requests.get(get_https)
    access_token = g.json()['access_token']

    title = sys.argv[1]  # 获取第一个参数
    message = sys.argv[2]  # 获取第二个参数

    send_message(access_token, title, message)
