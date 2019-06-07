import os
from dotenv import load_dotenv
from instabot import Bot
from os import listdir
from os.path import isfile
from os.path import join as joinpath


def upload_images_to_instagram(path, bot_obj):
    path = path + '/'
    for image_file in listdir(path):
        if isfile(joinpath(path, image_file)):
            filename = image_file.replace(path, '')
            bot_obj.upload_photo(path + image_file, caption=filename)
    return True

if __name__ == '__main__':
    load_dotenv()

    path = os.getenv('PATH_TO_IMAGES', 'images')
    os.makedirs(path, exist_ok=False)

    username = os.environ['LOGIN']
    password = os.environ['PASSWORD']
    bot = Bot()
    bot.login(username=username, password=password)
    if upload_images_to_instagram(path, bot):
        print('Done!')
    else:
        print('Error during uploading!')
