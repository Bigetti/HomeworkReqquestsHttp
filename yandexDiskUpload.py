import requests
import os

token = open("token").read()

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {self.token}"}
        
        file_name = os.path.basename(file_path)
        target_url = f'{url}?path={file_name}&overwrite=true'

        with open(file_path, "rb") as file:
            response = requests.get(target_url, headers=headers)
            
            if response.status_code == 200:
                upload_info = response.json()
                upload_url = upload_info.get("href")
                if upload_url:
                    with open(file_path, "rb") as file:
                        response = requests.put(upload_url, headers=headers, data=file)
                        print("Upload Response Status Code:", response.status_code)
                        print("Upload Response Content:", response.text)
                        if response.status_code == 201:
                            print("Successfully uploaded")
                            file_link = response.json().get("href")
                            if file_link:
                                print("Ссылка на загруженный файл:", file_link)
                            else:
                                print("Не удалось получить ссылку на загруженный файл")
                        else:
                            print("Произошла ошибка при загрузке файла")
                else:
                    print("Не удалось получить URL-адрес для загрузки файла")
            else:
                print("Произошла ошибка при получении URL-адреса для загрузки файла")

if __name__ == '__main__':
    path_to_file = r'F:\NETOLOGYPython\HomeworkReqquestsHttp\forUpload.txt'
    token = token
    uploader = YaUploader(token)
    uploader.upload(path_to_file)