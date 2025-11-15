# MkDocs の使い方ガイド

## python venv

python -m venv .venv

## venv の有効化(Windows)

.\.venv\Scripts\activate

## Mkdocs のインストール

pip install mkdocs
pip install mkdocs-material

## 参考にしたページ

https://smartscope.blog/Tips/Mkdocs/mkdocs%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9FGitHubPages/

## mkdocs serve

mkdocs serve

## GitHub Pages にデプロイ

mkdocs gh-deploy

# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

- `mkdocs new [dir-name]` - Create a new project.
- `mkdocs serve` - Start the live-reloading docs server.
- `mkdocs build` - Build the documentation site.
- `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
