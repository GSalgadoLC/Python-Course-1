import json
from pathlib import Path

movies = [
    {"id": 1, "title": "terminator", "year": 1993},
    {"id": 2, "title": "mall cop", "year": 2009}
]

data = json.dumps(movies)
print(data)
Path("movies.json").write_text(data)


data2 = Path("movies.json").read_text()
boviesdict = json.loads(data)
print(boviesdict)
