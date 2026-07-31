'''
统计 GitHub 仓库的 Python 项目：

用 requests 访问 https://api.github.com/search/repositories，参数 q=python, sort=stars, per_page=10
从返回的 JSON 中提取每个仓库的 name、stars、language
用 pandas 创建 DataFrame
用 Counter 统计各种 language 的出现次数
找出 stars 最多的仓库名
'''
import requests
import pandas as pd
from collections import Counter

def count_py():
    try:
        params = {"q": "python" , "sort": "stars" , "per_page": 10}
        response = requests.get("https://api.github.com/search/repositories" , params=params)
        response.raise_for_status()
        repos = response.json()["items"]

        rows = []
        for repo in repos:
            rows.append({
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "language": repo["language"] or "N/A"
            })

        df = pd.DataFrame(rows)

        languages = [r["language"] for r in rows]
        count_language = Counter(languages)

        top_repo = max(rows , key=lambda x: x["stars"])
    except requests.Timeout:
        print("timeout")
    except requests.HTTPError as e:
        print(f'http error statu:{e}')
    except requests.ConnectionError as e:
        print(f'connection error statu:{e}')
    except requests.exceptions.RequestException as e:
        print(f"error statu:{e}")

        
    #测试
    print(df)
    print(rows)
    print("-" * 40)
    print("语言分布:", count_language)
    print("Stars 最多:", top_repo["name"], "⭐", top_repo["stars"])

count_py()