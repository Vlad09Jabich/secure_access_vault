import json
import random
from pathlib import Path

ENCODING = 'utf-8'

CONFIG_FOLDER_PATH = Path('src/app/configs')
CONFIG_FILE_NAME = Path('user_db.json')
CONFIG_ALL_PATH = Path(CONFIG_FOLDER_PATH) / CONFIG_FILE_NAME

KEYS_FOLDER_PATH = Path('src/app/keys')


def generate_token(user_name: str, access_level: int) -> str:
    token = access_level * random.randint(1, 10)
    log_string = f'TOKEN-{user_name.upper()}-{token}'
    return log_string


def save_token (log_string: str) -> str:
    token = log_string.split('-')[2]
    user_name = log_string.split('-')[0]
    with open(Path(KEYS_FOLDER_PATH) / Path(f'{user_name}.txt'), 'w', encoding=ENCODING) as f:
        f.write()


with open(CONFIG_ALL_PATH, 'r', encoding=ENCODING) as f:
    users_data = json.load(f)

print(users_data)