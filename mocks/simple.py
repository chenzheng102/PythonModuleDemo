#-*- coding:utf-8 -*-
# 文件名：client
import requests


def send_requestr(url):
    r = requests.get(url)
    return r.status_code

def visit_ustack():
    return send_requestr("http://www.ustack.com")

import unittest
from unittest import mock

class TestClient(object):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        send_request = success_send
        # self.assertEqual(visit_ustack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        send_request = fail_send
        print(visit_ustack())
        # self.assertEqual(visit_ustack(), '404')

if __name__ == '__main__':
    unittest.main()