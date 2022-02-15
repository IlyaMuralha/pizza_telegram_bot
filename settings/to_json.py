import json


with open('cenz.txt', encoding='utf-8') as r:
    ar = r.read().lower().split()

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)
