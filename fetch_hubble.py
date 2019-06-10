import os
import requests
from dotenv import load_dotenv


def get_hubble_images_ids(url, collection):
    response = requests.get('{url}{colection}'.format(url=url,
                                                      collection=collection))
    if response.ok:
        response = response.json()
        hubble_images_ids = [image_info['id'] for image_info in response]
        return hubble_images_ids


def fetch_hubble_images(url, images_ids, path):
    for image_id in images_ids:
        response = requests.get(url + '{}'.format(image_id))
        if response.ok:
            response = response.json()
            last_image_url = response['image_files'][-1:][0]['file_url']
            _, extension = os.path.splitext(last_image_url)
            filename = '{path}/{image_id}.{extension}'.format(path=path,
                                                              image_id=image_id,
                                                              extension=extension)
            response = requests.get(last_image_url)
            if response.ok:
                with open(filename, 'wb') as file:
                    file.write(response.content)

if __name__ == '__main__':
    load_dotenv()
    path = os.environ['PATH_TO_IMAGES']
    os.makedirs(path, exist_ok=False)

    hubble_images_url = 'http://hubblesite.org/api/v3/images/'
    hubble_image_url = 'http://hubblesite.org/api/v3/image/'

    collections = ['holiday_cards', 'wallpaper']
    for collection in collections:
        images_ids = get_hubble_images_ids(hubble_images_url, collection)
        fetch_hubble_images(hubble_images_url, images_ids, path)
