from pathlib import Path
from zipfile import ZipFile
import zipfile

with ZipFile("files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)

with zipfile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
