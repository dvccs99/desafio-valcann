from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from segunda_questao.src.services.users_service import list_users, get_user

router = APIRouter()


@router.get("/users")
def get_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    q: Optional[str] = None,
    role: Optional[str] = None,
    is_active: Optional[bool] = None,
):
    users, total = list_users(page, page_size, q, role, is_active)
    return {
        "data": users,
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": (total + page_size - 1) // page_size,
        },
    }


@router.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"data": user}
