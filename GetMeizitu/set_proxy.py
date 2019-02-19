import requests
from requests.exceptions import ConnectionError
from urllib.parse import urlencode
import re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'referer' : 'https://www.mzitu.com/'

}
proxy_pool_url = 'http://127.0.0.1:5000/get'

proxy = None
def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_content(url):
    print('Crawling',url)
    global proxy
    try:
        if proxy:
            proxies = {
                'http':'http://'+proxy
            }
            response = requests.get(url,allow_redirects=False,headers=headers,proxies=proxies)
        else:
            response = requests.get(url,allow_redirects=False,headers=headers)
        if response.status_code == 200:
            return response.content
        if response.status_code == 302:
            # 设置代理
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy',proxy)
                return get_content(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occured',e.args)
        proxy = get_proxy()
        return get_content(url)
