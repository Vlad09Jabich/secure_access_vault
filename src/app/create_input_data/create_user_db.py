import random
import json
from typing import Any
from pathlib import Path

USERS = ['vlad', 'Sally', 'BOB', 'qwerty', 'Jon', '1234', 'Zeus', 'Apocriton', 'Arch']

def create_user_info(name: str, id: int) -> dict[str, any]:
    user_ifo = {}
    user_ifo['id'] = None
    user_ifo['user'] = None
    user_ifo['access_level'] = None
    user_ifo['is_active'] = None


db = []
first_id = 1
id = first_id

for user in USERS:
    create_user_info(user, id)
    id += 1

print(db)
