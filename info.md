# MkDocs の使い方ガイド

## uv のインストール (インストールされていない場合)
### [公式ドキュメント](https://docs.astral.sh/uv/getting-started/installation/)

### Windows
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## プロジェクトのセットアップ・同期 (`pyproject.toml` を使用)
uvコマンドを用いると、インストールと仮想環境の作成が一度に行われます。
```bash
uv sync
```

## アクティベート (必要な場合)
※ `uv run mkdocs serve` のようにコマンドの頭に `uv run` を付ける場合はアクティベート不要です。直接仮想環境に入りたい場合は以下を実行します。

### Windowsの場合
```powershell
.venv\Scripts\activate
```
### macOS/Linuxの場合
```bash
source .venv/bin/activate
```

## 参考にしたページ
https://smartscope.blog/Tips/Mkdocs/mkdocs%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9FGitHubPages/

## 開発サーバーの立ち上げ

```bash
uv run mkdocs serve
```

## GitHub Pages にデプロイ

```bash
uv run mkdocs gh-deploy
```

# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

- `uv run mkdocs new [dir-name]` - Create a new project.
- `uv run mkdocs serve` - Start the live-reloading docs server.
- `uv run mkdocs build` - Build the documentation site.
- `uv run mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
