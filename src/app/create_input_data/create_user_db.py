import random
import json
from typing import Any
from pathlib import Path

ENCODING = 'utf-8'
FOLDER_PATH = Path('src/app/configs')
FILE_NAME = Path('user_db.json')
ALL_PATH = Path(FOLDER_PATH) / FILE_NAME

USERS = ['vlad', 'Sally', 'BOB', 'qwerty', 'Jon', '1234', 'Zeus', 'Apocriton', 'Arch']
FIRST_ID = 1

def create_user_info(user_name: str, id: int) -> dict[str, any]:
    user_ifo = {}
    user_ifo['id'] = id
    user_ifo['user'] = user_name
    user_ifo['access_level'] = random.randint(1, 10)
    user_ifo['is_active'] = random.choice([True, False])
    db.append(user_ifo)


db = []
id = FIRST_ID

for user in USERS:
    create_user_info(user, id)
    id += 1

with open(ALL_PATH, 'w', encoding=ENCODING) as f:
    json.dump(db, f, indent=4)

print(db)
