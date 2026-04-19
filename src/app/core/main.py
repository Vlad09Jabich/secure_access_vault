import json
import random
from pathlib import Path

ENCODING = 'utf-8'
CONFIG_FOLDER_PATH = Path('src/app/configs')
CONFIG_FILE_NAME = Path('user_db.json')
CONFIG_ALL_PATH = Path(CONFIG_FOLDER_PATH) / CONFIG_FILE_NAME
LOGS_FILE_NAME = Path('vault_log.txt')
KEYS_FOLDER_PATH = Path('src/app/keys')
KEYS_FOLDER_PATH.mkdir(exist_ok=True)


def generate_token(access_level: int) -> str:
    token = f'{access_level * random.randint(1, 10)}'
    return token


def save_token (user_name: str, token: str) -> None:
    with open(Path(KEYS_FOLDER_PATH) / Path(f'{user_name}.txt'), 'w', encoding=ENCODING) as f:
        f.write(token)


with open(CONFIG_ALL_PATH, 'r', encoding=ENCODING) as f:
    users_data = json.load(f)

logs: list[str] = []
for user in users_data:
    try:
        user_name = user['user']
        if user['is_active']:
            token = generate_token(user['access_level'])
            save_token(user_name, token)
            logs.append(f'[OK] {user_name} processed \n')
        else:
            logs.append(f'[SKIP] {user_name} is inactive \n')
            
    except KeyError as err:
        logs.append(f'[ERROR] ID {user['uid']}: {err}\n')
    except TypeError as err:
        logs.append(f'[ERROR] ID {user['uid']}: {err}\n')

with open(Path(CONFIG_FOLDER_PATH) / LOGS_FILE_NAME, 'w', encoding=ENCODING) as f:
    f.writelines(logs)

print(f'Security Audit Complete. Check {LOGS_FILE_NAME}')
