from locust import HttpUser, task, between
import random

# Определяем класс пользователя, который будет имитировать действия
class PetStoreUser(HttpUser):
    wait_time = between(1, 3)  # Пауза между действиями: от 1 до 3 секунд

    # GET /v2/pet/{petId} — получение информации о питомце
    @task(3)  # Этот таск выполняется в 3 раза чаще других
    def get_pet(self):
        pet_id = random.choice([111, 222, 333, 444, 555])  # Выбираем случайный ID из списка
        self.client.get(f"/v2/pet/{pet_id}")

    # POST /v2/pet — добавление нового питомца
    @task(1)
    def add_pet(self):
        headers = {"Content-Type": "application/json"}
        pet_data = {
            "id": random.randint(10000, 99999),  # Случайный ID
            "name": f"TestPet_{random.randint(100, 999)}",  # Уникальное имя
            "photoUrls": [],
            "tags": [],
            "status": random.choice(["available", "pending", "sold"])
        }
        self.client.post("/v2/pet", json=pet_data, headers=headers)

    # PUT /v2/pet — обновление данных о питомце
    @task(1)
    def update_pet(self):
        headers = {"Content-Type": "application/json"}
        pet_data = {
            "id": random.randint(10000, 99999),
            "name": f"UpdatedPet_{random.randint(100, 999)}",
            "photoUrls": [],
            "tags": [],
            "status": random.choice(["available", "pending", "sold"])
        }
        self.client.put("/v2/pet", json=pet_data, headers=headers)

    # DELETE /v2/pet/{petId} — удаление питомца
    @task(1)
    def delete_pet(self):
        pet_id = random.randint(10000, 99999)
        self.client.delete(f"/v2/pet/{pet_id}")
