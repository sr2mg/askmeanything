# 匿名で Discord で質問できるボット

## 使い方

1. Discord Developer [アプリケーション](https://discord.com/developers/applications)より新規のアプリケーションを作成
2. bot 権限で管理者権限のある Discord サーバにインストール
3. 下記の「動かし方」を参照
4. `/ama "大規模言語モデルとはなんですか？"`あるいは DM より利用

## 動かし方

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
