import os
import urllib.request, zipfile,shutil

urllib.request.urlretrieve("https://github.com/upx/upx/releases/download/v4.2.3/upx-4.2.3-win32.zip",
                           "upx-4.2.3-win32.zip")
zip = zipfile.ZipFile("upx-4.2.3-win32.zip")
zip.extract("upx-4.2.3-win32/upx.exe", path=os.getcwd())
shutil.move("upx-4.2.3-win32/upx.exe", os.path.join(os.getcwd(), "upx.exe"))
with open("utils.py", "r", encoding="utf8") as util:
    util_context = util.read()
for file in os.listdir(os.getcwd()):
    if file != "utils.py" and file != "generate-bundle.py" and file.endswith(".py") and not os.path.isdir(file):
        print(f"build {file}")
        os.system(f"pyarmor gen --enable-jit --assert-call --assert-import --pack onefile {file} ")
# 傻逼
# 狗屎代碼


