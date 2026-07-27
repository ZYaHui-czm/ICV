# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.json)# 问题1
import itertools
passwords = ["".join(map(str, p)) for p in itertools.product(range(10), repeat=6)]
print(passwords)