# -*- coding: UTF-8 -*-

# Author:awen
# Blog:https://awen.me
# E-mail: hi@awen.me



import sys
try:
    import requests
    import fire
    import tldextract

except ImportError:

    print("Please install requests fire tldextract ")
    sys.exit(1)
    
import logging

logging.getLogger("tldextract").setLevel(logging.CRITICAL)

def query(domain):

        tld_domain = tldextract.extract(domain)

        domain = "{}.{}".format(tld_domain.domain, tld_domain.suffix)

        print("正在查询域名:"+domain)
        
        url = "https://sapi.k780.com"

        querystring = {"app": "domain.beian", "domain": domain, "appkey": "xxx",
                       "sign": "xxx", "format": "json"}

        headers = {

            'Cache-Control': "no-cache",
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res_json = response.json()

        issuccess = int(res_json['success'])

        isstatus = res_json['result']["status"]

        if issuccess == 1:

            if isstatus == "ALREADY_BEIAN":

                print("域名已备案")


            elif isstatus == "NOT_BEIAN":

                print("域名未备案")

            elif isstatus == "WAIT_PROCESS":

                print("等待系统处理")

        elif issuccess == 0:

            print("系统错误")


if __name__ == '__main__':

    fire.Fire(query)
