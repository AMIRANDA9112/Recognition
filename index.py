from get_web.download_video import download_video
from get_web.search_face import search_face
from engine.Video_proccesor.get_cam import get_cam
from engine.Video_proccesor.compile_video import compile_video
from tkinter import *


class interface_index:

    def __init__(self, window):

        self.wind = window
        self.wind.title('Recognition Laboratory -- Version 1.3a')

        # Colors Style

        color_button = "azure2"
        bg_message = "white"
        color_label = "white"
        color_section = "white"
        color_input = "azure"

        # border style

        border_width = 0

        # border_syle =

        # Text Style

        # font =

        # color_font = "black"
        color_message = "blue"

        # Output message
        self.message = Label(text='', fg=color_message)
        self.message.grid(row=7, column=0, columnspa=2, sticky=W + E)
        self.message['text'] = 'You see progress in console and can cancel de Analysis with Ctrl + c'
        self.message.config(bg=bg_message)

        self.message2 = Label(text='', fg=color_message)
        self.message2.grid(row=6, column=0, columnspa=2, sticky=W + E)
        self.message2['text'] = 'Video ".mp4(xvid)" Format and Faces Image ".jpg" or ".png" Format'
        self.message2.config(bg=bg_message)

        self.message3 = Label(text='', fg=color_message)
        self.message3.grid(row=4, column=0, columnspa=2, sticky=W + E)
        self.message3['text'] = 'You can use your WebCam'
        self.message3.config(bg=bg_message)

        # Input Main process container
        frame = LabelFrame(self.wind)
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        frame.config(bg=color_label)

        # image view

        Label(frame, image=img, bg=color_label).grid(row=1, columnspan=2, pady=10)

        # Path video Input
        Label(frame, text='Video Path:', bg=color_section, bd=border_width).grid(row=2, column=0)
        self.video = Entry(frame)
        self.video.focus()
        self.video.grid(row=2, column=1)
        self.video.config(bg=color_input, bd=border_width)

        # Url face input
        Label(frame, text='Faces Directory: ', bg=color_section, bd=border_width).grid(row=3, column=0)
        self.face = Entry(frame)
        self.face.grid(row=3, column=1)
        self.face.config(bg=color_input, bd=border_width)

        # detail of analyze input
        Label(frame, text='Detail index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=4, column=0)
        self.detail = Spinbox(frame, from_=1, to=10)
        self.detail.grid(row=4, column=1)
        self.detail.config(bg=color_input, bd=border_width)

        # start button

        Button(frame, text='Start Face Analysis', command=self.add_path,
               bg=color_button, bd=border_width).grid(row=5, columnspan=2, sticky=W + E)

        # Convert video Button
        Button(frame, text='WebCam Face Analysis', command=self.add_cam, bg=color_button,
               bd=border_width).grid(row=6, columnspan=2, sticky=W + E)

        # Tools section

        frame2 = LabelFrame(self.wind, text='Tools')
        frame2.grid(row=5, column=0, columnspan=3, pady=20)
        frame2.config(bg=color_label, bd=border_width)

        # intput video to convert

        # Url video Input
        Label(frame2, text='Video url:', bg=color_section, bd=border_width).grid(row=3, column=0)
        self.download = Entry(frame2)
        self.download.grid(row=3, column=1)
        self.download.config(bg=color_input, bd=border_width)

        # download Button
        Button(frame2, text='Download Video from Youtube', command=self.get_url_video, bg=color_button,
               bd=border_width).grid(row=4, columnspan=2, sticky=W + E)

        # download face
        Label(frame2, text='Name of celebrity or famous:', bg=color_section, bd=border_width).grid(row=5, column=0)
        self.search = Entry(frame2)
        self.search.grid(row=5, column=1)
        self.search.config(bg=color_input, bd=border_width)

        # download face Button
        Button(frame2, text='Search Face', command=self.download_face,
               bg=color_button, bd=border_width).grid(row=6, columnspan=2, sticky=W + E)

    # Validations methods

    def validation_url_video(self):
        # validation url input
        return len(self.download.get()) != 0

    def validation_face(self):
        # validation url input
        return len(self.search.get()) != 0 and len(self.face.get()) != 0

    def validation(self):
        # validation paths input
        return len(self.video.get()) != 0 and len(self.face.get()) != 0

    def validation_cam(self):
        # validation url input
        return len(self.face.get()) != 0

    def add_cam(self):

        if self.validation_cam():
            faces = self.face.get()
            get_cam(faces)
            self.message3['text'] = 'WebCam Analysis In Progress'

        else:
            self.message3['text'] = 'You Need Images in Faces Directory'

    def add_path(self):

        if self.validation():
            # get video
            dir_video = self.video.get()
            # get images
            dir_face = self.face.get()
            # get details
            detail_process = self.detail.get()

            detail_process = int(detail_process) / 10

            details = detail_process

            if compile_video(dir_video, dir_face, details):

                self.message['text'] = 'Video and Faces Image Analyze is Successfully'
            else:
                self.message['text'] = 'A valid .mp4(Xvid) video is required'

        else:
            self.message['text'] = 'Video to Analyze and Faces Images is required'

    def get_url_video(self):
        # redirect to download video
        if self.validation_url_video():

            url_video = self.download.get()
            download_video(url_video)
            self.message['text'] = 'Redirecting to download page'

        else:
            self.message['text'] = 'Please enter a valid YouTube Link'

    def download_face(self):
        # download a face of google image with a name input
        if self.validation_face():

            dir_face = self.face.get()

            name = self.search.get()

            if search_face(name, dir_face) == "fail":
                self.message['text'] = 'Automatic image download in fail format, search other name'

            else:
                self.message['text'] = 'face image save in faces directory successful'

        else:
            self.message['text'] = '"Faces directory" and "Name" of face to search is required'


if __name__ == '__main__':
    window = Tk()
    img = Image("photo", file='icon.png')
    window.tk.call('wm', 'iconphoto', window._w, img)
    window.config(bg="white")
    application = interface_index(window)
    window.mainloop()
