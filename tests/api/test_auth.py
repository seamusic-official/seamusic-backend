import pytest
from fastapi import UploadFile, Response
from fastapi.testclient import TestClient

from src.schemas.auth import SUserResponse, SRegisterUserRequest, Role

email = 'test_email2@example.com'
password = 'test_password'


@pytest.mark.parametrize(
    'roles,expected_status_code,username,email_',
    [
        ([Role.listener, Role.moder], 201, 'test_username2', email),
        (['fake_role'], 400, 'test_username3', 'fake_test_email@example.com'),
        ([Role.listener], 403, 'test_username2', email)
    ]
)
def test_register(client: TestClient, roles: list[Role], expected_status_code: int, username: str, email_: str) -> None:
    user = SRegisterUserRequest(
        username=username,
        password=password,
        email=email_,
        roles=roles,
        birthday=None,
        tags=['supertrap', 'newjazz', 'rage', 'hyperpop']
    )
    response: Response = client.post(url='/auth/register', json=user.model_dump())
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    'password_,expected_status_code',
    [(password, 200), ('wrong_password_1', 401), ('wrong_password_2', 401)]
)
def test_login(client: TestClient, password_: str, expected_status_code: int) -> None:
    response: Response = client.post(
        url='/auth/login',
        json={
            'email': 'test_email@test.test',
            'password': password_
        }
    )
    assert response.status_code == expected_status_code


def test_get_me(client: TestClient, expected_status_code: int) -> None:
    response: Response = client.get('/auth/users/me')
    assert response.status_code == expected_status_code


def test_get_users(client: TestClient) -> None:
    response: Response = client.get('/auth/users/')
    assert response.status_code == 200


def test_get_one(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.get(f'/auth/users/{user.id}')
    assert response.status_code == 200


def test_update_user_picture(client: TestClient, user: SUserResponse) -> None:
    with open('some_file', 'rb') as file:
        response: Response = client.put(
            url=f'/auth/users/picture/{user.id}',
            json={'file': UploadFile(file=file)}
        )
    assert response.status_code == 200


def test_update_user(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.put(
        url=f'/auth/users/{user.id}',
        json={
            'username': '',
            'email': '',
            'picture_url': '',
            'tags': ['supertrap, newjazz, rage'],
            'roles': ['artist', 'producer', 'listener']
        }
    )
    assert response.status_code == 200


def test_delete_user(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.delete(f'/auth/users/{user.id}')
    assert response.status_code == 200


def test_get_me_as_artist(client: TestClient) -> None:
    response: Response = client.get('/auth/users/artists/me')
    assert response.status_code == 200


def test_get_artists(client: TestClient) -> None:
    response: Response = client.get('/auth/users/artists')
    assert response.status_code == 200


def test_get_one_artist(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.get(f'/auth/users/artists/{user.id}')
    assert response.status_code == 200


def test_update_artists(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.put(
        url=f'/auth/users/artists/{user.id}',
        json={'description': 'new_description'}
    )
    assert response.status_code


def test_deactivate_artists(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.delete(f'/auth/users/artists/{user.id}')
    assert response.status_code == 200


def test_get_me_as_producer(client: TestClient) -> None:
    response: Response = client.get('/auth/users/producers/me')
    assert response.status_code == 200


def test_get_all_producers(client: TestClient) -> None:
    response: Response = client.get('/auth/users/producers')
    assert response.status_code == 200


def test_get_one_producer(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.get(f'/auth/users/producers/{user.id}')
    assert response.status_code == 200


def test_update_one_producer(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.put(
        url=f'/auth/users/producers/{user.id}',
        json={'description': 'new_description'}
    )
    assert response.status_code == 200


def test_deactivate_one_producer(client: TestClient, user: SUserResponse) -> None:
    response: Response = client.post(f'/auth/users/producers/{user.id}')
    assert response.status_code == 200


def test_refresh(client: TestClient) -> None:
    response: Response = client.post('/auth/refresh')
    assert response.status_code == 200


def test_spotify_callback(client: TestClient) -> None:
    response: Response = client.post('/auth/callbcak')
    assert response.status_code == 200
