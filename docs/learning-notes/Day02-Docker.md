# Day02 Docker Compose・PostgreSQL環境構築

**学習日**：2026-06-28

---

# 1. 本日の目標

- Docker Composeの役割を理解する。
- Docker Composeを利用してPostgreSQL環境を構築する。
- `docker-compose.yml` の構成要素と役割を理解する。
- Dockerコンテナの起動・確認・ログ確認を行う。
- Dockerコンテナ内へ入り、PostgreSQLへ接続する。
- SQLを実際に実行し、DockerとPostgreSQLの連携を理解する。

---

# 2. 実施内容

## 2.1 Docker Composeの学習

DockerとDocker Composeの違いについて学習した。

- Docker：コンテナを作成・実行・管理するプラットフォーム
- Docker Compose：複数のコンテナを設定ファイル（docker-compose.yml）でまとめて管理する仕組み

---

## 2.2 docker-compose.ymlの作成

プロジェクト直下に `docker-compose.yml` を作成した。

以下の設定項目について学習した。

- services
- image
- container_name
- environment
- ports
- volumes

各設定項目の役割を理解し、PostgreSQLコンテナの設定を作成した。

---

## 2.3 Docker Composeの構文チェック

以下のコマンドを実行した。

```bash
docker compose config
```

構文エラーを確認・修正し、正常な設定ファイルであることを確認した。

---

## 2.4 PostgreSQLコンテナの起動

以下のコマンドを実行した。

```bash
docker compose up -d
```

Docker Composeの設定どおりにPostgreSQLコンテナを作成・起動した。

---

## 2.5 コンテナの確認

以下のコマンドを実行した。

```bash
docker ps
```

起動しているコンテナを確認した。

確認内容

- PostgreSQLコンテナが正常に起動していること
- ポート5432で待機していること
- コンテナ名が設定どおりであること

---

## 2.6 PostgreSQLのログ確認

以下のコマンドを実行した。

```bash
docker logs postgres-db
```

ログを確認し、

- PostgreSQLの初期化
- sample_dbの作成
- PostgreSQLの起動
- 接続待機状態

まで正常に実行されていることを確認した。

---

## 2.7 Dockerコンテナへ入る

以下のコマンドを実行した。

```bash
docker exec -it postgres-db bash
```

Dockerコンテナ内のLinux環境へ入り、コンテナ内部を操作できることを確認した。

---

## 2.8 PostgreSQLへ接続

以下のコマンドを実行した。

```bash
psql -U postgres -d sample_db
```

Dockerコンテナ内からPostgreSQLへ接続した。

各オプションの意味

- psql：PostgreSQLクライアント
- -U：接続ユーザー
- -d：接続するデータベース

---

## 2.9 初めてのSQL実行

以下のSQLを実行した。

```sql
SELECT version();
```

結果

```text
PostgreSQL 16.14
```

Docker上で動作しているPostgreSQLへ初めてSQLを実行できた。

---

# 3. 学んだこと

## DockerとDocker Compose

Dockerはコンテナを実行するための基盤であり、Docker Composeは複数のコンテナを一括管理するための仕組みである。

---

## docker-compose.yml

設定ファイルには以下の項目を記述する。

### services

起動するサービスを定義する。

### image

利用するDockerイメージを指定する。

### container_name

コンテナ名を指定する。

### environment

環境変数を設定する。

例

- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD

### ports

ホスト(Mac)とコンテナを接続するためのポート番号を設定する。

例

```
5432:5432
```

左側：Mac側

右側：Dockerコンテナ側(PostgreSQL)

### volumes

データを永続化するために利用する。

コンテナを削除してもデータは保持される。

---

## Dockerの操作手順

実務では一度にすべてを確認するのではなく、

1. docker-compose.ymlを作成
2. docker compose configで構文確認
3. docker compose upで起動
4. docker psで状態確認
5. docker logsでログ確認

という流れで段階的に確認することが重要である。

---

## PostgreSQL

Dockerコンテナ内へ入り、

```bash
psql -U postgres -d sample_db
```

でPostgreSQLへ接続した。

SQLを実行することで、Docker上のデータベースを操作できることを理解した。

---

# 4. 感想・気づき

Day2ではDocker・Docker Compose・Containerの役割や関係性を理解することができた。

特に印象に残ったことは、

- Docker Composeによって環境構築を自動化できること
- コンテナは自由に作成・削除できること
- Volumeによってデータを永続化できること
- コンテナ内で実行するものと、ホスト側で管理するものを明確に分けること

である。

また、環境構築では一気に作業を進めるのではなく、

- 設定を書く
- 構文チェック
- 起動
- 状態確認
- ログ確認

というように段階ごとに確認することが重要であることを学んだ。

最後にDockerコンテナへ入り、PostgreSQLへ接続し、SQLを実行できたことは非常に達成感があった。

DockerとPostgreSQLの全体像を理解できたことで、今後のSQL学習やデータエンジニアリングの基礎を築くことができた。

---

# 5. 次回の目標

- PostgreSQLの基本操作を理解する。
- テーブルとは何かを理解する。
- CREATE TABLEを学ぶ。
- INSERT文でデータを登録する。
- SELECT文でデータを取得する。
- SQLの基本構文に慣れる。

---

# 6. 本日の学習コマンド

```bash
docker compose config

docker compose up -d

docker ps

docker logs postgres-db

docker exec -it postgres-db bash

psql -U postgres -d sample_db

SELECT version();
```
