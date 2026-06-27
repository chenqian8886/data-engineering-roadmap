# Day01 Git・開発環境構築

**日付**：2026年6月27日

---

# 1. 本日の目標

本日の目標は以下の4つです。

1. データエンジニアの開発環境を構築する
2. プロジェクトを作成する
3. Gitの基本操作を理解する
4. 今後24か月使用するプロジェクトの基盤を完成させる

---

# 2. 本日実施した内容

- Gitの動作確認
- Pythonの動作確認
- Docker Desktopのインストール・動作確認
- Docker Composeの動作確認
- VS Codeの動作確認
- Gitリポジトリの作成
- プロジェクトディレクトリの作成
- README.mdの作成
- docsフォルダの作成
- Gitの初回コミット

---

# 3. 開発環境の確認

## 実施したコマンド

```bash
git --version
python3 --version
docker --version
docker compose version
code --version
```

## なぜ確認するのか

環境に問題があると開発を進められないため、最初に確認します。

---

# 4. プロジェクトの作成

## 実施したコマンド

```bash
mkdir ~/data-engineering-roadmap
cd ~/data-engineering-roadmap
pwd
```

結果

```text
/Users/qianchen/data-engineering-roadmap
```

## なぜ作成するのか

毎回新しいフォルダを作るのではなく、一つのプロジェクトを継続して改善することで、実務に近い開発スタイルを身につけます。

---

# 5. Gitの初期化

## 実施したコマンド

```bash
git init
```

## なぜ実施するのか

Gitに

> このフォルダを管理してください

と伝えるためです。

実行すると `.git` フォルダが作成されます。

このフォルダにはGitの履歴や管理情報が保存されています。

---

# 6. プロジェクト構成

```text
data-engineering-roadmap/
│
├── docker/
├── python/
├── sql/
├── data/
│   ├── raw/
│   ├── staging/
│   └── mart/
├── docs/
├── scripts/
├── tests/
├── logs/
├── README.md
└── .gitignore
```

## なぜこの構成にするのか

データエンジニアはPythonだけを書く仕事ではありません。

以下のような成果物を管理します。

- Python
- SQL
- Docker
- データ
- テスト
- ドキュメント

そのため、最初から整理されたディレクトリ構成を採用します。

---

# 7. README.md

READMEは

**このプロジェクトの説明書**です。

GitHubで最初に表示される重要なファイルです。

採用担当者も最初にREADMEを見ることが多いため、今後充実させていきます。

---

# 8. docsフォルダ

作成したファイル

```text
architecture.md

database-design.md

learning-log.md
```

## architecture.md

システム全体の構成をまとめます。

例

```text
CSV

↓

Python

↓

PostgreSQL

↓

Dashboard
```

---

## database-design.md

データベース設計書です。

今後以下を記録します。

- ER図
- テーブル設計
- カラム定義
- 主キー
- 外部キー

---

## learning-log.md

毎日の学習記録です。

例

```text
Day1

・Docker導入

・Git学習

・プロジェクト作成
```

---

# 9. Gitの基本

Gitには3つの重要な場所があります。

```text
Working Directory（作業中）

        │
        │ git add
        ▼

Staging Area（コミット待ち）

        │
        │ git commit
        ▼

Repository（保存済み）
```

---

## Working Directory

ファイルを作成・編集した状態です。

まだGitには保存されていません。

---

## git add

```bash
git add .
```

Gitへ

> この変更を次回保存してください

と伝えます。

この状態を **Staging** と呼びます。

---

## git commit

```bash
git commit -m "メッセージ"
```

変更内容をGitへ保存します。

ここではじめて履歴が残ります。

---

# 10. git status

最も重要なGitコマンドです。

```bash
git status
```

現在の状態を確認できます。

---

## Untracked

```text
Untracked files
```

意味

Gitがまだ管理していない新しいファイル

---

## Modified

```text
modified:
```

意味

Gitが管理しているファイルを変更した状態

---

## Changes to be committed

意味

git add が完了し、コミット待ちの状態

---

## Working tree clean

```text
nothing to commit, working tree clean
```

意味

すべて保存済みで、作業ツリーが最新の状態

---

# 11. Vimの基本

今回は

```bash
git commit
```

を実行したため、Vimエディタが起動しました。

学んだ操作

| 操作 | コマンド |
|------|----------|
| 編集開始 | i |
| 編集終了 | Esc |
| 保存して終了 | :wq |
| 保存せず終了 | :q! |

---

# 12. 初回コミット

実行結果

```text
[main 76a2902]
docs: add initial project documentation
```

意味

- main：現在のブランチ
- 76a2902：Commit ID
- docs: add initial project documentation：コミットメッセージ

---

# 13. 今日学んだ最重要ポイント

Gitは

**ファイルを管理しているのではありません。**

Gitは

**ファイルの状態（State）** を管理しています。

状態は次のように変化します。

```text
ファイル作成

↓

Untracked

↓

git add

↓

Staged

↓

git commit

↓

Tracked

↓

編集

↓

Modified

↓

git add

↓

Commit
```

---

# 14. 本日の成果

本日は以下を理解・実践しました。

- 開発環境の構築
- Gitの初期化
- Gitの基本操作
- Gitの状態管理
- プロジェクト構成の設計
- ドキュメント管理の考え方

---

# 15. Day2の予定

次回はデータベース環境を構築します。

予定内容

1. Docker Composeの作成
2. PostgreSQLコンテナの構築
3. pgAdminの導入
4. データベース作成
5. ER図作成
6. SQL（DDL）の作成

ここから本格的なデータエンジニアリングの学習を開始します。

---

# 今日の振り返り

今日は環境構築だけでなく、Gitの基本的な考え方を理解することができた。

特に、「Gitはファイルそのものではなく、ファイルの状態（State）を管理する」という考え方を学んだことが大きな収穫だった。

今後は毎日の学習内容を記録し、コードだけでなく設計書や学習ノートも継続して蓄積していく。