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

def fetch_spacex_last_launchage(url, path):
    print('Downloading from spacex site...')
    response = requests.get(url)
    if response.ok:
      images_urls = [url for url in response.json()['links']['flickr_images']]
      iteration = len(images_urls)
      for index, url in enumerate(images_urls):
        filename = path + '/' + 'space_{}.jpg'.format(index+1)
        response = requests.get(url)
        if response.ok:
          with open(filename, 'wb') as file:
            file.write(response.content)
        else:
          print('URL is not available')
        print(render_progressbar(len(images_urls), iteration))
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

    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    fetch_spacex_last_launchage(spacex_url, path)