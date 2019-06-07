import os
import requests
from dotenv import load_dotenv


def fetch_spacex_last_launchage(url, path):
    response = requests.get(url)
    if response.ok:
        images_urls = [url for url in response.json()['links']['flickr_images']]
        for index, url in enumerate(images_urls):
            filename = path + '/' + 'space_{}.jpg'.format(index+1)
            response = requests.get(url)
            if response.ok:
                with open(filename, 'wb') as file:
                    file.write(response.content)
            else:
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    load_dotenv()

    path = os.getenv('PATH_TO_IMAGES', 'images')
    os.makedirs(path, exist_ok=False)

    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    if fetch_spacex_last_launchage(spacex_url, path):
        print('Done!')
    else:
        print('URL is not available')
