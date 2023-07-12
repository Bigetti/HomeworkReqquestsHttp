import requests
import pickle

import json

token = open("token").read()

dict_responce ={}

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика

        # Не совсем поимаю как я должен был понять что путь именно такой, ГПТ чат.
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {self.token}"}
        
        #Только благодаря ГПТ чату понял ято понадобится имя файла и как его добыть
        file_name = path_to_file.split('\\')[-1]

        with open(file_path, "rb") as file:
            data = file.read()

       
        # Отправляем запрос на загрузку файла, это ГПТ чат, сам я не понимаю как такой код писать
        response = requests.put(
            url,
            headers=headers,
            params={"path": file_name},
            data=data
        )

        if response.status_code == 201:
            print("File was successfully aploaded to YandexDisk")
            # Извлекаем ссылку на загруженный файл
            upload_info = response.json()
            file_link = upload_info.get("href")
            if file_link:
                print("Ссылка на загруженный файл:", file_link)
            else:
                print("Не удалось получить ссылку на загруженный файл")
        else:
            print("Mistake happend")

        dict_responce = response.json()


        #Хочу выгрузить данные в файл  и посмотреть что там, но получаю какую-то ошибку внутри файла, сама выгрузка идет
        with open("file.txt", 'w') as f:
            json.dump(dict_responce, f, ensure_ascii=False, indent=2)
        
        print(type(dict_responce))
        #убеждаюсь, что это словарь

        return dict_responce
    
    def __str__(self):
        return json.dumps(self.dict_responce, indent=4)
        

   
        


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'F:\\NETOLOGYPython\\HomeworkReqquestsHttp\\forUpload.txt'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    
    
    print(result)
    