import requests
import os

def download_image(urls,save_path):
    for i,url in enumerate(urls,start=1):
        img_data = requests.get(url)
        print(img_data)
        with open(f'{save_path}/download_{i}.jpg','wb') as f:
            f.write(img_data.content)
        print("images downloaded")
def delete_images(urls,save_path):
    for i ,url in enumerate(urls,start=1):
        os.remove(f'{save_path}/download_{i}.jpg')

    print("images deleted successfully")

def main():
    urls = [
        'https://images.pexels.com/photos/28495472/pexels-photo-28495472.jpeg?cs=srgb&dl=pexels-karanghadi-28495472.jpg&fm=jpg&w=2977&h=3970',
        'https://unsplash.com/photos/BjEKmyBGl8g/download?ixid=M3wxMjA3fDB8MXxhbGx8fHx8fHx8fHwxNzQ4NzMxMTMyfA&force=true',
        'https://unsplash.com/photos/a-statue-of-a-woman-with-a-colorful-headdress-t36nG76zVKI?modal=%5B%22Subscribe%22%2C%7B%22sourceAsset%22%3A%5B%22Photos%22%2C%7B%22slug%22%3A%22a-statue-of-a-woman-with-a-colorful-headdress-t36nG76zVKI%22%7D%5D%7D%5D'
    ]
    save_path = 'C:/Users/HP/Downloads/'
    download_image(urls,save_path)
    delete_images(urls,save_path)

if __name__ == "__main__":
    main()
