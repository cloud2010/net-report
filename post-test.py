# -*- coding: utf-8 -*-
"""
模拟POST请求
"""
import http.client
import time
import json


def vote_number_four(counts):

    conn = http.client.HTTPConnection("xhsdz.echaokj.cn")

    payload = "VoteID=%2C4&Ip=0.0.0.0"

    headers = {
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
    }
    for i in range(1, counts+1):
        conn.request("POST", "/Vote/GetAdd", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print('\n已投票:{0}张\n'.format(i))
        result_json = json.loads(data)
        print('投票状态：', result_json)
    
    # 查看最新票数
    conn.request("GET", "/Vote/GetVoteCountList")
    res = conn.getresponse()
    data = res.read()
    result_json = json.loads(data)
    nums_vote = result_json['data'][3]
    print("\n组别：{0} ==> 当前票数：{1}".format(nums_vote['VoteID'], nums_vote['Count']))


if __name__ == '__main__':
    start_time = time.time()
    vote_number_four(589)
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
