# -*- coding:utf-8 -*-
"""
一段小爬虫
"""
from urllib.request import urlopen
url = "https://t.bilibili.com/?spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.31"
resp = urlopen(url)
with open("mybilibili.html", "w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
print("over!")