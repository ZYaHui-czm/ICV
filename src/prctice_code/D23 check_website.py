'''
写一个函数 check_website(url)：

尝试 GET 请求该 URL
如果成功，返回 {"status": "ok", "code": 状态码}
超时返回 {"status": "timeout"}
连接失败返回 {"status": "error", "message": 错误信息}
'''
import requests
def check_website(url):
    try:
        response = requests.get(url , timeout=20)
        response.raise_for_status()                                     #访问不成功主动抛出异常
        return {"status" : "ok" , "code" : response.status_code}
    
    except requests.exceptions.Timeout:
        return {"status" : "timeout"}
    
    except requests.exceptions.ConnectionError as e:
        return {"status" : "connection error" , "message" : e}

    except requests.exceptions.HTTPError as e:
        return {"status" : "http error" , "message" : e}

    except requests.exceptions.RequestException as e:
        return {"status" : "error" , "message" : e}