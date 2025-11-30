def normalize_message(msg: str) -> str:
    return msg.strip()

def load_system_prompt(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception:
        return ''
