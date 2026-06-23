from pathlib import Path

GA_TAG = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NNTE50GLPT"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-NNTE50GLPT');
</script>
"""

files = list(Path(".").glob("*.html"))
files += list(Path("posts").glob("*.html"))

count = 0

for file in files:
    text = file.read_text(encoding="utf-8")

    if "G-NNTE50GLPT" not in text:
        text = text.replace("</head>", GA_TAG + "\n</head>")
        file.write_text(text, encoding="utf-8")
        count += 1

print(f"GA4 inserted into {count} files")