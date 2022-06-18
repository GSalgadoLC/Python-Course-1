from pathlib import Path
#Path(r"C:\Program Files\Microsoft")
path = Path("ecommerce/__init__.py")

path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute())
