# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 16:06
# @Author  : Magic
# @File    : http.py

# url
# requests
import requests


class HTTP:
    def get(self, url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''
