import os
import requests
from dotenv import load_dotenv

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)
        

def get_file_extension(url):
    return url.split('.')[-1:][0]       

def fetch_hubble_images(url, collections, path):
    print('Downloading from hubble site:' + ' ' * 20)
    for collection in collections:
        print(collection + ' collection...' + ' ' * 20)
        response = requests.get(url + '{}'.format(collection))
        if response.ok:
            response = response.json()
            hubble_images_ids = [image_info['id'] for image_info in response]
            iteration = len(hubble_images_ids)
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
                print(render_progressbar(len(hubble_images_ids), iteration))
                print('\u001b[2A')
                iteration -= 1      
        else:
            print('URL is not available')
    print('Done!' + ' ' * 40)

if __name__ == '__main__':
    load_dotenv()
    path = os.environ['PATH'] 
    if not os.path.exists(path):
      os.makedirs(path)
    
    hubble_images_url = 'http://hubblesite.org/api/v3/images/'
    collections = ['holiday_cards', 'wallpaper'] #['holiday_cards', 'wallpaper', 'spacecraft', 'news', 'printshop', 'stsci_gallery']
    fetch_hubble_images(hubble_images_url, collections, path)
    
