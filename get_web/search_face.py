#!/usr/bin/env
from icrawler.builtin import BingImageCrawler
from icrawler import ImageDownloader
import cv2
import os


# search and download the front face image of google searcher

class PrefixNameDownloader(ImageDownloader):

    def get_filename(self, task, default_ext):
        filename = super(PrefixNameDownloader, self).get_filename(
            task, default_ext)
        return filename


def search_face(name, directory):

    bing_crawler = BingImageCrawler(storage={'root_dir': directory}, downloader_cls=PrefixNameDownloader)
    filters = dict(size='medium', type='photo', color='color', people='face')
    real_name = name
    name = name
    bing_crawler.crawl(keyword=name, max_num=1, filters=filters)

    for root, dirs, files in os.walk(directory):

        if "000001.jpg" in files:
            new_name = str(directory + real_name + ".jpg")
            path = directory + "000001.jpg"
            os.rename(path, new_name)
            return 0

        elif "000001.png" in files:

            new_name = str(directory + real_name + ".png")
            path = directory + "000001.png"
            os.rename(path, new_name)
            return 0

        elif "000001.jpeg" in files:
            path = directory + "000001.jpeg"
            new_name = str(directory + real_name + ".png")
            img = cv2.imread(path)
            cv2.imwrite(new_name, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            return 0

        else:
            pass
