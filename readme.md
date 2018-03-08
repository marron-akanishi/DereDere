# DereDere
このスクリプトは[IM@S CG DB](http://imas.cg.db.n-hokke.com/)からカード画像を自動回収するものです。  

## 動作環境
python 3を使用しています。  
pipを用いて、requestsとbs4とwgetをインストールしてください。

## 使い方
まず、chara.jsonにキャラ名と保存先フォルダー名を対応させてJSONファイルに書きます。  
例としてリポジトリに置いてあるファイルは765PRO組のみ書いてあります。  
その後、main.pyを実行すればchara.jsonに基づいてダウンロードを行います。  
wgetのダウンロードバーがバグりますが、きちんと保存できると思います。
