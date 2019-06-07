import os
import requests
from dotenv import load_dotenv


def get_file_extension(url):
    return url.split('.')[-1:][0]


def fetch_hubble_images(url, collections, path):
    for collection in collections:
        print(collection + ' collection...')
        response = requests.get(url + '{}'.format(collection))
        if response.ok:
            response = response.json()
            hubble_images_ids = [image_info['id'] for image_info in response]
            for image_id in hubble_images_ids:
                image_url = 'http://hubblesite.org/api/v3/image/'
                response = requests.get(image_url + '{}'.format(image_id))
                if response.ok:
                    response = response.json()
                    last_image_url = response['image_files'][-1:][0]['file_url']
                    extension = get_file_extension(last_image_url)
                    filename = path + '/' + str(image_id) + '.' + extension
                    response = requests.get(last_image_url)
                    if response.ok:
                        with open(filename, 'wb') as file:
                            file.write(response.content)
                    else:
                        print('URL is not available')
                else:
                    print('URL is not available')
        else:
            print('URL is not available')
    print('Done!')

if __name__ == '__main__':
    load_dotenv()
    path = os.environ['PATH_TO_IMAGES']
    os.makedirs(path, exist_ok=False)

    hubble_images_url = 'http://hubblesite.org/api/v3/images/'
    collections = ['holiday_cards', 'wallpaper']
    fetch_hubble_images(hubble_images_url, collections, path)
