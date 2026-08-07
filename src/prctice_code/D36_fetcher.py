'''
写 fetcher.py 完整模块，要求：

定义函数 fetch_top_repos(top: int) -> list[dict]
从环境变量读 token(用 os.getenv)
用 requests.get 请求 GitHub 搜索 API(q=language:python&sort=stars)
timeout=10,超时/网络错误抛自定义 ApiError
非 2xx 状态码抛 ApiError(带状态码信息)
返回 data["items"] 列表
'''

import requests
import os

class ApiError(Exception):
    def __init__(self, status_code, message=""):
        self.status_code = status_code
        self.message = message
        super().__init__(f'ApiError:[{status_code}:{message}]')

def fetcher_top_repos(top: int)->list[dict]:
    GITHUB_API = "https://api.github.com/search/repositories"
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    params = {"q": "language:python", "sort": "stars"}
    headers = {"Anthorization": GITHUB_TOKEN}

    try:
        resp = requests.get(GITHUB_API, params=params, headers=headers, timeout=10)
        if not(200 <= resp.status_code < 300):
            raise ApiError(resp.status_code, resp.text)
        
    except requests.exceptions.Timeout:
        raise ApiError(resp.status_code)

    data = resp.json()
    return data["items"]
