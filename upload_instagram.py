import os
from dotenv import load_dotenv
from instabot import Bot
from os import listdir
from os.path import isfile
from os.path import join as joinpath


def upload_images_to_instagram(path, bot_obj):
    files = os.listdir(path)
    images = filter(lambda x: x.endswith(('.jpg', '.png')), files)
    for image in images:
        bot_obj.upload_photo(os.path.join(path, image), caption=image)

if __name__ == '__main__':
    load_dotenv()

    path = os.getenv('PATH_TO_IMAGES', 'images')

    username = os.environ['LOGIN']
    password = os.environ['PASSWORD']
    bot = Bot()
    bot.login(username=username, password=password)
    upload_images_to_instagram(path, bot)
