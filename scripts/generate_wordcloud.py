import os
import re
import urllib.request
from wordcloud import WordCloud
from janome.tokenizer import Tokenizer

FONT_URL = "https://github.com/googlefonts/noto-cjk/raw/main/Sans/OTF/Japanese/NotoSansCJKjp-Regular.otf"
FONT_FILE = "scripts/NotoSansCJKjp-Regular.otf"
DOCS_DIR = "docs"
EXCLUDE_DIRS = ["site", "overrides", "assets"]
OUTPUT_FILE = "docs/assets/wordcloud/wordcloud.svg"

def download_font():
    """フォントが存在しない場合のみダウンロード"""
    if not os.path.exists(FONT_FILE):
        print("Downloading Japanese font...")
        req = urllib.request.Request(FONT_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res, open(FONT_FILE, 'wb') as f:
            f.write(res.read())
    return FONT_FILE

def get_markdown_files(root_dir):
    """Markdownファイルの一覧を取得"""
    md_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        md_files.extend([os.path.join(root, f) for f in files if f.endswith(".md")])
    return md_files

def read_and_clean_text(file_path):
    """ファイルの読み込みと不要なテキスト（コード、HTMLタグなど）の除去"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        text = re.sub(r'^---\n[\s\S]*?\n---\n', '', text) # Frontmatter
        text = re.sub(r'```[\s\S]*?```', '', text)        # Code blocks
        text = re.sub(r'<[^>]+>', ' ', text)              # HTML tags (div, spanなど)
        text = re.sub(r'http[s]?://\S+', '', text)        # URLs
        
        return text
    except Exception:
        return ""

def tokenize_japanese(text):
    """形態素解析して名詞のみを抽出"""
    t = Tokenizer()
    # Web用語や不要な単語を除外
    stop_words = {
        'こと', 'もの', 'ため', 'よう', 'それ', 'これ', 'あれ', 'ここ', 'そこ', 
        'div', 'class', 'span', 'id', 'html', 'img', 'src', 'href', 'style', 'script',
        'align', 'center', 'width', 'height', 'br', 'md', 'png', 'jpg',
        'assets'
    }
    
    words = []
    for token in t.tokenize(text):
        if token.part_of_speech.startswith('名詞'):
            surface = token.surface
            if surface.lower() not in stop_words and len(surface) > 1 and not surface.isdigit():
                words.append(surface)
                
    return " ".join(words)

def main():
    font_path = download_font()
    
    print("Reading markdown files...")
    text = "".join(read_and_clean_text(f) + "\n" for f in get_markdown_files(DOCS_DIR))
        
    print("Tokenizing text...")
    words = tokenize_japanese(text)
    
    if words.strip():
        print("Generating an awesome WordCloud...")
        os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
        
        wc = WordCloud(
            width=1200, height=600, 
            background_color=None, mode="RGBA", 
            colormap="cool",                    
            font_path=font_path,
            regexp=r"[\w']+"
        ).generate(words)

        svg_data = wc.to_svg(embed_font=True)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(svg_data)
            
        print(f"Word cloud saved to {OUTPUT_FILE}")
    else:
        print("No words extracted.")

if __name__ == "__main__":
    main()
