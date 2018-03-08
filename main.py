import sys
import os
import json
import re
import requests
from bs4 import BeautifulSoup
import wget

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
LIST_FILE = "./chara.json"
CARD_URL= re.compile(r"/cards/\d+")

# json読み込み
search = json.load(open(LIST_FILE, encoding="utf-8"))
for folder in search.values():
    save = "./" + folder + "/"
    if os.path.exists(save) == False:
        os.mkdir(save)

for chara in search.keys():
    print("キャラ:{}".format(chara))
    # キャラ詳細ページ
    url = "http://imas.cg.db.n-hokke.com/idols/{}".format(chara)
    res = requests.get(url)
    chara_html = BeautifulSoup(res.content, "html.parser")
    # リンク全部取得
    card_urls = chara_html.findAll('a')
    for card_url in card_urls:
        # リンクURL取得
        href = card_url.get("href")
        # URLチェック
        if CARD_URL.match(href):
            # カード詳細ページ
            url = "http://imas.cg.db.n-hokke.com{}".format(href)
            res = requests.get(url)
            card_html = BeautifulSoup(res.content, "html.parser")
            # カード画像を取得
            img_url = card_html.find('img')
            src = img_url.get("src")
            out_path = "./{}/{}".format(search[chara], src.split("/")[-1])
            print(out_path)
            wget.download(src, out=out_path)
            print("")

print("取得完了")