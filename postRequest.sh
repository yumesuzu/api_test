#/bin/bash

# APIにPOSTリクエストする

### 引数一覧
# $1 : エンドポイント
# $2 : リクエストボディ(JSON)

### 変数定義

# エンドポイント
ENDPOINT="http://127.0.0.1:5000/yumesuzu/${1}"

# リクエストボディ(JSON形式で受け取る)
JSON="${2}"

# リクエストを出す
curl -X POST -H "Content-Type: application/json" -d "${JSON}" "${ENDPOINT}"