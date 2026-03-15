# Raspberry Pi Cat Detector (個人開発)

## 最新エッジAIとDiscordを統合した、リアルタイム猫見守りシステム

![Cat Detector System](../assets/cat_detection/main_visual.svg)

### プロジェクト概要

　「身近な猫が外から帰宅した瞬間を把握したい」という動機から開発した、プッシュ型通知システムです。
市販の監視カメラのような常時録画ではなく、最新のAIモデル（YOLO26）を用いることで「猫が活動した瞬間」のみを判定し、Discordへ即座に通知を送信します。

| 項目 | 内容 |
| --- | --- |
| **開発期間** | 2026年1月3日 〜 |
| **開発構成** | 個人開発 |
| **使用技術** | Python (3.13), uv, OpenCV, Ultralytics YOLO26n, OpenVINO, Discord Webhook |
| **役割・実装** | システム設計、AIモデル選定・最適化 |

YOLO26は2026年1月にリリースされた最新のエッジ向けモデルを採用。低電力デバイスであるRaspberry Piにおいて、高精度かつ軽量な推論だと思い採用をしました。

### 精度実験(WIP)

### リポジトリ
https://github.com/YukkiMoru/cat_detection