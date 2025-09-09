from fastapi.testclient import TestClient
from segunda_questao.src.main import app

client = TestClient(app)


# ---------- /users ----------
def test_list_users_default():
    """Deve retornar a primeira página com 10 usuários por padrão."""
    response = client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "pagination" in data
    assert data["pagination"]["page"] == 1
    assert data["pagination"]["page_size"] == 10


def test_list_users_with_pagination():
    """Deve respeitar page e page_size."""
    response = client.get("/users?page=1&page_size=1")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 1
    assert data["pagination"]["page_size"] == 1


def test_list_users_with_filter_q():
    """Deve filtrar usuários pelo nome/email."""
    response = client.get("/users?q=bruno")
    assert response.status_code == 200
    data = response.json()
    assert any("bruno" in u["name"].lower() for u in data["data"])


def test_list_users_with_filter_role():
    """Deve filtrar por role."""
    response = client.get("/users?role=admin")
    assert response.status_code == 200
    data = response.json()
    for user in data["data"]:
        assert user["role"] == "admin"


def test_list_users_with_filter_is_active():
    """Deve filtrar por is_active."""
    response = client.get("/users?is_active=true")
    assert response.status_code == 200
    data = response.json()
    for user in data["data"]:
        assert user["is_active"] is True


# ---------- /users/{id} ----------
def test_get_user_by_id_existing():
    """Deve retornar um usuário existente."""
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert data["data"]["id"] == 1


def test_get_user_by_id_not_found():
    """Deve retornar 404 se usuário não existir."""
    response = client.get("/users/9999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"


# ---------- /users?page=x ----------
def test_invalid_page_zero():
    response = client.get("/users?page=0")
    assert response.status_code == 422


def test_invalid_page_negative():
    response = client.get("/users?page=-1")
    assert response.status_code == 422


def test_invalid_page_size_zero():
    response = client.get("/users?page_size=0")
    assert response.status_code == 422


def test_invalid_page_size_too_large():
    response = client.get("/users?page_size=100")
    assert response.status_code == 422


def test_valid_pagination_request():
    response = client.get("/users?page=1&page_size=5")
    assert response.status_code == 200
    data = response.json()
    assert data["pagination"]["page"] == 1
    assert data["pagination"]["page_size"] == 5
    assert "data" in data
    assert isinstance(data["data"], list)
