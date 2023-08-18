import os

# Naziv JavaScript datoteke
js_file_name = 'main.js'

# Napravite putanju do JavaScript datoteke koristeći samo naziv
js_file_path = os.path.join(js_file_name)

# Otvorite datoteku u načinu čitanja
with open(js_file_path, 'r') as js_file:
    js_code = js_file.read()

# Ispišite sadržaj JavaScript datoteke
print(js_code)
