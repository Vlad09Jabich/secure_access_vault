import random
import json
from typing import TypedDict
from pathlib import Path

ENCODING = 'utf-8'
FOLDER_PATH = Path('src/app/configs')
FILE_NAME = Path('user_db.json')
ALL_PATH = Path(FOLDER_PATH) / FILE_NAME

USERS = ['vlad', 'Sally', 'BOB', 'qwerty', 'Jon', '1234', 'Zeus', 'Apocriton', 'Arch']
FIRST_UID = 1


class UserInfo(TypedDict):
    uid: int
    user: str
    access_level: int
    is_active: bool


def create_user_info(user_name: str, uid: int) -> UserInfo:
    return {
        'uid': uid,
        'user': user_name,
        'access_level': random.randint(1, 10),
        'is_active': random.choice([True, False])
    }


db: list[UserInfo] = []
uid = FIRST_UID
for user in USERS:
    new_user = create_user_info(user, uid)
    db.append(new_user)
    uid += 1

with open(ALL_PATH, 'w', encoding=ENCODING) as f:
    json.dump(db, f, indent=4)
