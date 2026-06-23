from pathlib import Path

ADSENSE = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5818703186403843"
     crossorigin="anonymous"></script>
"""

files = list(Path(".").glob("*.html"))
files += list(Path("posts").glob("*.html"))

count = 0

for file in files:
    text = file.read_text(encoding="utf-8", errors="ignore")

    if "ca-pub-5818703186403843" in text:
        continue

    if "</head>" in text:
        text = text.replace("</head>", ADSENSE + "\n</head>")
        file.write_text(text, encoding="utf-8")
        count += 1

print(f"AdSense inserted into {count} files")