import re

API_ID = 30036820
API_HASH = '02566bf224a9c7615aad843c7b87db89'
TARGET_CHAT = -1003609605227
SOURSE_CHAT = -1003848748310
TOKEN = '8666935199:AAHaK55wmXyw5yn659COUlXceHqbp8Uk_HU'
MAIN_BOT_TOKEN = '8141725422:AAEOHdnOV5DlWA3dQjPT_3zIZ3ZQEv6z_9o'

def update_config(key, new_value, filename='config.py'):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    val_str = str(new_value)
    if not val_str.replace('-', '').isdigit():
        val_str = f"'{val_str}'"

    new_lines = []
    found = False
    for line in lines:
        if re.match(rf'^{key}\s*=', line.strip()):
            new_lines.append(f"{key} = {val_str}\n")
            found = True
        else:
            new_lines.append(line)

    if not found:
        new_lines.append(f"{key} = {val_str}\n")

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
