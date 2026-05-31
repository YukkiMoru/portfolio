from pathlib import Path

# 設定: プロジェクトのルートディレクトリからの相対パス
DOCS_DIR = "docs"
OUTPUT_FILE = "scripts/merged_docs.md"


def merge_markdown_files(docs_dir, output_file):
    docs_path = Path(docs_dir)
    markdown_files = sorted(docs_path.glob("**/*.md"))

    # index.md を最初にするためのソート（簡易的）
    def sort_key(path):
        rel_path = path.relative_to(docs_path)
        # index.md は最優先
        if rel_path.name == "index.md":
            return (0, rel_path)
        return (1, rel_path)

    markdown_files.sort(key=sort_key)

    with open(output_file, "w", encoding="utf-8") as outfile:
        for md_file in markdown_files:
            relative_path = md_file.relative_to(docs_path)
            outfile.write(f"\n\n<!-- SOURCE: {relative_path} -->\n")
            outfile.write(f"# File: {relative_path}\n\n")

            with open(md_file, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())

            outfile.write("\n\n---\n")

    print(f"Merged {len(markdown_files)} files into {output_file}")


if __name__ == "__main__":
    # プロジェクトのルートディレクトリを基点にパスを解決
    base_dir = Path(__file__).parent.parent
    docs_path = base_dir / DOCS_DIR
    output_path = base_dir / OUTPUT_FILE

    merge_markdown_files(docs_path, output_path)
