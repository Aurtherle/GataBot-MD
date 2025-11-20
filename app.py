# install_requirements.py
import subprocess
import sys

# قائمة المكتبات المطلوبة
required_libraries = [
    "Pillow",
    "arabic-reshaper",
    "aiohttp",
    "zipfile36",
    "requests",
    "beautifulsoup4",
    "lxml",
    "replicate",
    "opencv-python",
    "fonttools",
    "scikit-image",
    "shapely",
    "numpy"
]

# تثبيت المكتبات
print("📥 جاري تثبيت المكتبات المطلوبة...")
for lib in required_libraries:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
        print(f"✅ تم تثبيت {lib} بنجاح!")
    except Exception as e:
        print(f"❌ حدث خطأ أثناء تثبيت {lib}: {e}")

print("✅ تم تثبيت جميع المكتبات المطلوبة!")
