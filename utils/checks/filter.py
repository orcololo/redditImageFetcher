import os
from urllib.parse import urlparse
import wordninja
import pyimgur


def redgifs_handler(link):
    url_info = urlparse(link)
    words = wordninja.split(url_info.path.split("/")[-1])
    for index in range(3):
        words[index] = words[index].capitalize()
    return f'https://thumbs2.redgifs.com/{"".join(words)}.mp4'


def imgur_handler(link):
    im = pyimgur.Imgur(os.getenv('imgur_cliend_id'))
    img = im.get_image(link.split(".")[-2].split("/")[-1])
    print(img.link)


def filter_links(links):
    new_links = list()
    domains = list()
    for item in links:
        i = urlparse(item)
        if i.netloc not in domains:
            domains.append(i.netloc)
        if i.netloc == 'redgifs.com':
            new_links.append(redgifs_handler(item))
        if i.netloc == 'i.imgur.com':
            imgur_handler(i.path)
        if i.netloc != ('redgifs.com' or 'i.imgur.com'):
            print('add', item)
    print(domains)
    return new_links
