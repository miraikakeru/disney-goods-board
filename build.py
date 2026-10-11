# src/page.html と data.json から index.html（GitHub Pages用）と artifact.html（claude.ai用）を作る
import json,pathlib
here=pathlib.Path(__file__).parent
page=(here/"src/page.html").read_text(encoding="utf-8")
data=json.loads((here/"data.json").read_text(encoding="utf-8"))
blob=json.dumps(data,ensure_ascii=False).replace("</","<\\/")
body=page.replace("/*__DATA__*/null",blob)
(here/"artifact.html").write_text(body,encoding="utf-8")
head='''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#141a46">
<style>img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
'''
(here/"index.html").write_text(head+body+"\n</body>\n</html>\n",encoding="utf-8")
print("ok",len(data["items"]))
