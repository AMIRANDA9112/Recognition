from icrawler.builtin import GoogleImageCrawler
from icrawler import ImageDownloader
import os


# search and download the front face image of google searcher

class PrefixNameDownloader(ImageDownloader):

    def get_filename(self, task, default_ext):
        filename = super(PrefixNameDownloader, self).get_filename(
            task, default_ext)
        return filename


def search_face(name, directory):
    google_crawler = GoogleImageCrawler(storage={'root_dir': directory}, downloader_cls=PrefixNameDownloader)
    filters = dict(size='medium', type='face')
    real_name = name
    name = name + "face jpg png"
    google_crawler.crawl(keyword=name, max_num=1, filters=filters, )

    for root, dirs, files in os.walk(directory):

        if "000001.jpg" in files:
            new_name = str(directory + real_name + ".jpg")
            path = directory + "000001.jpg"
            os.rename(path, new_name)
            return 0

        if "000001.npg" in files:

            new_name = str(directory + real_name + ".npg")
            path = directory + "000001.npg"
            os.rename(path, new_name)
            return 0
        else:
            pass
