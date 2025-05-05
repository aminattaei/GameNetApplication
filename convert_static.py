import os
import re

# تنظیم مسیر پوشه قالب‌ها
TEMPLATES_DIR = os.path.abspath("templates")

# الگوی regex برای پیدا کردن مسیرهای استاتیک
STATIC_PATTERN = re.compile(r'(["\'])(?:/?|\./)?static/([^"\']+)(["\'])')

def convert_static_paths(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        print(f"📂 Opened file: {file_path}")
        print(f"📜 Original content:\n{content[:200]}...")  # فقط 200 کاراکتر اول برای تست

        if not STATIC_PATTERN.search(content):
            print(f"⚠️ No static paths found in: {file_path}")
            return

        new_content = STATIC_PATTERN.sub(r'\1{% static "\2" %}\3', content)

        if "{% load static %}" not in new_content:
            new_content = "{% load static %}\n" + new_content

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)

        print(f"✅ Saved changes to: {file_path}")
        print(f"📜 New content:\n{new_content[:200]}...")
    except Exception as e:
        print(f"❌ Error: {type(e).__name__} - {str(e)}")

def process_templates():
    if not os.path.exists(TEMPLATES_DIR):
        print(f"❌ Directory '{TEMPLATES_DIR}' not found!")
        return

    html_files = [os.path.join(root, file) for root, _, files in os.walk(TEMPLATES_DIR) for file in files if file.endswith(".html")]

    if not html_files:
        print("⚠️ No HTML files found.")
        return

    print(f"🔄 Found {len(html_files)} files: {html_files}")
    for file_path in html_files:
        convert_static_paths(file_path)

if __name__ == "__main__":
    process_templates()