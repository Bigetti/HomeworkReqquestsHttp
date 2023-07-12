import requests
import pickle

import json

token = open("token").read()


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

        if response.status_code -- 201:
            print("File was successfully aploaded to YandexDisk")
        else:
            print("Mistake happend")

        dict = response.json()


        #Хочу выгрузить данные в файл  и посмотреть что там, но получаю какую-то ошибку внутри файла, сама выгрузка идет
        with open("file.txt", 'w') as f:
            json.dump(dict, f, ensure_ascii=False, indent=2)
        
        print(type(dict))
        #убеждаюсь, что это словарь

        for key, value in dict.items() :
            print (key, value)

        return dict
        

   
        


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'F:\\NETOLOGYPython\\HomeworkReqquestsHttp\\forUpload.txt'
    token = token
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    
    #Вроде все отрабатывает, File was successfully aploaded to YandexDisk, но мой файл не появился у меня в облаке и я не понимаю где его нужно искать
    # print(dict)
    