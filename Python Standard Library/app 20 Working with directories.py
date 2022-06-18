from pathlib import Path
from struct import pack_into

path = Path("Ecommerce")
path.exists()
path.mkdir()
path.rmdir()
# path.rename("ecommerce2")

for p in path.iterdir():
    print(p)
# This will iterate over files inside a directory
# A generator object returns a new value everytime you iterate, more efficient

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob("*.py")]
print(py_files)
