# -*- coding: utf-8 -*-
"""
模拟POST请求
"""
import http.client
import time


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
        print('\n已投票:{0}张'.format(i))
        print(data.decode("utf-8"))


if __name__ == '__main__':
    start_time = time.time()
    vote_number_four(278)
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
