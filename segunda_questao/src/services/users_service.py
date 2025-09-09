from typing import List, Optional, Tuple
from segunda_questao.src.models.user import User
from segunda_questao.src.repositories.user_repository import (
    load_users,
    get_user_by_id,
)


def list_users(
    page: int = 1,
    page_size: int = 10,
    q: Optional[str] = None,
    role: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Tuple[List[User], int]:
    """
    Retorna a lista de usuários com filtros, busca e paginação.
    """
    users = load_users()
    if q:
        q_lower = q.lower()
        users = [
            u
            for u in users
            if q_lower in u.name.lower() or q_lower in u.email.lower()
        ]
    if role:
        users = [u for u in users if u.role == role]
    if is_active is not None:
        users = [u for u in users if u.is_active == is_active]

    total = len(users)
    start = (page - 1) * page_size
    end = start + page_size
    return users[start:end], total


def get_user(user_id: int) -> Optional[User]:
    return get_user_by_id(user_id)
