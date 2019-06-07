# Space-instagram

* The script fetch_spacex.py downloads latest images from spacex site.
* The script fetch_hubble.py downloads high quality images from hubble site.
* The script upload_instagram.py uploads images to instagram account.


# How to start

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

### Environment variables.

- LOGIN
- PASSWORD
- PATH_TO_IMAGES

Default value of `PATH_TO_IMAGES` is `images`

.env example:

```
LOGIN=user
PASSWORD=PassWord
PATH_TO_IMAGES=images
```
### How to get

* Sign up [instagram](https://www.instagram.com/).

### Note

You can use more collections, for example followed list:
['holiday_cards', 'wallpaper', 'spacecraft', 'news', 'printshop', 'stsci_gallery']

### Run

Launch on Linux(Python 3.5) or Windows as simple

```bash
$ python fetch_spacex.py
$ python fetch_hubble.py
$ python upload_instagram.py

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)