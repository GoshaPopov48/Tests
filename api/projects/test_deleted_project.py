from conftest import api_client, project_id
import time 

def test_deleted_project(api_client, project_id):
    response = api_client.delete(f"/api/admin/projects/{project_id}")
    
    assert response.status_code == 200
    print("Проект удален")
    
    # Таймер засыпания необходим, т.к проект сначала попадает в Архив и спустя секунду или обновление страницы интерфейса исчезает
    time.sleep(1)
    # Проверка что проект не существует
    check_project = api_client.get(f"/api/admin/projects/{project_id}")
    
    assert check_project.status_code == 404