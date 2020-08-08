from engine.Video_proccesor.compile_video import compile_video
from get_web.download_video import download_video
from get_web.search_face import search_face
from tkinter import *
from tkinter import ttk


class interface_index:

    def __init__(self, window):

        self.wind = window
        self.wind.title('Recognition')

        # Output message
        self.message = Label(text='', fg='blue')
        self.message.grid(row=4, column=0, columnspa=2, sticky=W + E)
        self.message['text'] = 'Video .mp4 Format and Faces Image .jpg or .png Format'

        self.message2 = Label(text='', fg='black')
        self.message2.grid(row=3, column=0, columnspa=2, sticky=W + E)
        self.message2['text'] = 'You can Skip the video processing and the Match with ESC Key '

        # Input Main process container
        frame = LabelFrame(self.wind, text='Tag Faces in Video')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Path video Input
        Label(frame, text='Video Path:').grid(row=1, column=0)
        self.video = Entry(frame)
        self.video.focus()
        self.video.grid(row=1, column=1)

        # Url face input
        Label(frame, text='Faces Directory: ').grid(row=2, column=0)
        self.face = Entry(frame)
        self.face.grid(row=2, column=1)

        # detail of analyze input
        Label(frame, text='Detail index (Min1-Max10):').grid(row=3, column=0)
        self.detail = Spinbox(frame, from_=1, to=10)
        self.detail.grid(row=3, column=1)

        # start button
        ttk.Button(frame, text='Start Face Analysis', command=self.add_path).grid(row=4, columnspan=2, sticky=W + E)

        # Url video Input
        Label(frame, text='Video url:').grid(row=5, column=0)
        self.download = Entry(frame)
        self.download.grid(row=5, column=1)

        # download Button
        ttk.Button(frame, text='Download Video', command=self.get_url_video).grid(row=6, columnspan=2, sticky=W + E)

        # download face
        Label(frame, text='Name:').grid(row=7, column=0)
        self.search = Entry(frame)
        self.search.grid(row=7, column=1)

        # download Button
        ttk.Button(frame, text='Search Face', command=self.download_face).grid(row=8, columnspan=2, sticky=W + E)

    def validation_url_video(self):
        # validation url input
        return len(self.download.get()) != 0

    def validation_face(self):
        # validation url input
        return len(self.search.get()) != 0 and len(self.face.get()) != 0

    def validation(self):
        # validation paths input
        return len(self.video.get()) != 0 and len(self.face.get()) != 0

    def add_path(self):

        if self.validation():
            # get video
            dir_video = self.video.get()
            # get images
            dir_face = self.face.get()

            detail_process = self.detail.get()

            print(detail_process)

            detail_process = int(detail_process)/10

            details = detail_process

            print(details)

            compile_video(dir_video, dir_face, details)

            self.message['text'] = 'Video and Faces Image Analyze is Successfully'
        else:
            self.message['text'] = 'Video to Analyze and Faces Images is required'

    def get_url_video(self):
        # redirect to download video
        if self.validation_url_video():

            url_video = self.download.get()
            download_video(url_video)
            self.message['text'] = 'Redirecting to download page, write video path when download finish'

        else:
            self.message['text'] = 'Please enter a url web video'

    def download_face(self):
        # download a face of google image with a name input
        if self.validation_face():

            dir_face = self.face.get()
            name = self.search.get()
            if search_face(name, dir_face) == "fail":
                self.message['text'] = 'The automatic image download in fail format'

            else:
                self.message['text'] = 'face image save in faces directory successful'

        else:
            self.message['text'] = '"Faces directory" and "Name" of face to search is required'


if __name__ == '__main__':
    window = Tk()
    application = interface_index(window)
    window.mainloop()
