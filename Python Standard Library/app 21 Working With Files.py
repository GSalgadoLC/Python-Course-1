from pathlib import Path
from time import ctime


path = Path("ecommerce/__init__.py")
print(path.exists())
print(ctime(path.stat().st_ctime))

path.read_text()

with open("__init__.py", "r") as file:
    ...

path.write_text("....")
path.write_bytes()


source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

target.write_text(source.read_text())
