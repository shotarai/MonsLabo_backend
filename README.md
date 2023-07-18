# MonsLabo_backend
★をたくさん付けてあげてください！

# MonsLan_backendの使い方
以下ではローカルでの実行手順を記載します。

まず本レポジトリのクローンをお願いします。
```
git clone https://github.com/Yoh-lab/MonsLabo_backend
```

次に本プロジェクト直下に以下の`.env`ファイルが必要になります。<br>
（OpenAIのAPIキーが必要となるため、各自で取得をお願いします。）
```
OPENAI_API_KEY=
```

続いて環境構築が必要となるため、以下のコマンドを順にお願いします。

### 新しい仮想環境の作成
```
python -m venv env
```

### 作成した仮想環境のアクティブ化（Windowsの場合）
```
env\Scripts\activate
```

### 作成した仮想環境のアクティブ化（Mac/Linuxの場合）
```
source env/bin/activate
```

### 必要なパッケージのインストール
```
pip install -r requirements.txt
```

### 起動
```
uvicorn app:app --reload
```

## [MonsLab_frontend](https://github.com/Yoh-lab/MonsLabo_frontend)に関して
本プロジェクトで実装したAPIを利用したWebアプリケーションとなります。<br>
（そちらの使用方法などは向こうのREADME参照）
