# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.json)# 问题1


# import itertools
# passwords = ["".join(map(str, p)) for p in itertools.product(range(10), repeat=6)]
# print(passwords)

# 问题1：找2个bug
from collections import defaultdict
d = defaultdict(list)
pairs = [("a", 1), ("a", 3), ("b", 2)]
for k, v in pairs:
    d[k] += v          # bug在这里
print(dict(d))