from conftest import api_client



def test_autohorization(api_client):
    response = api_client.get(
        "/api/users/me",
        params={"fields": "id,login,fullName"}
        )
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data['login']
    assert data['fullName']
    
    print("Успешная авторизация")
    print(data['login'])
    print(data['fullName'])
    print(data['id'])
    
