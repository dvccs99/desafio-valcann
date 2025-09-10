import json
from typing import List, Optional
from segunda_questao.src.models.user import User

DATA_FILE = "segunda_questao/mock-users.json"


def load_users() -> List[User]:
    """Carrega os usuários do arquivo mock."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [User(**u) for u in data]


def get_user_by_id(user_id: int) -> Optional[User]:
    users = load_users()
    return next((u for u in users if u.id == user_id), None)
