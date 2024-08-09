# 匿名で質問できる Discord Bot

## GUI でポチポチすること

1. Discord Developer Portal [アプリケーションページ](https://discord.com/developers/applications)より新規のアプリケーションを作成（New Application）
1. [Optional] General Information タブより画像を指定
1. OAuth2 タブより OAuth2 URL Generator -> Bot にチェック -> Send Messages にチェック -> URL を開いて bot をサーバに追加
1. Bot タブより Reset Token -> Token をコピー（.env にあとで記載するので控える）
1. 環境構築（下記参照）
1. `/ama "大規模言語モデルとはなんですか？"` のように質問を入力

## CUI でカタカタすること

```
git clone git@github.com:schroneko/askmeanything.git
cd askmeanything
rye sync
cp .env.example .env
vim .env
python main.py
```

### rye がない場合

```
brew install rye
```

## ライセンス

MIT ライセンスとしています。詳細は[LICENSE](https://github.com/schroneko/askmeanything/blob/main/LICENSE) にて。
