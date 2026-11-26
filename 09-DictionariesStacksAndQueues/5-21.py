import json

favourite = {
    "title": "Stargate",
    "year": 1994,
    "director": "Roland Emmerich",
    "genre": "Sci-Fi",
    "rating": 7.1,
    "main_characters": ["Daniel Jackson", "Jack O'Neil"],
}

with open("favourite.json", "w", encoding="utf-8") as f:
    json.dump(favourite, f)