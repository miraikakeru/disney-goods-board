# ディズニーグッズ速報ボード

東京ディズニーリゾートのパーク内グッズ、ディズニーストアなど公式ストアのグッズ、他ブランドとのコラボグッズを発売日順にまとめるサイトです。

- 公開URL: https://miraikakeru.github.io/disney-goods-board/
- `data.json` は毎朝5時（日本時間）に自動で更新され、新しいグッズがあった日だけメールで通知されます。
- 画面は `src/page.html` と `data.json` から `python3 build.py` で `index.html`（GitHub Pages用）と `artifact.html`（claude.ai用）を作ります。`index.html` は表示時に `data.json` を読み込むので、日々の更新は `data.json` だけで済みます。
- お気に入りは閲覧しているブラウザ内に保存されます。
