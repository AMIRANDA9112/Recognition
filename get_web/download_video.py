from webbrowser import open


def download_video(url):
    download = url[:12] + "ss" + url[12:]

    open(download)
