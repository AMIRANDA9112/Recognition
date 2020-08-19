from tkinter import *
import PIL.Image
import PIL.ImageTk
from modules.Module_face import module_face
from modules.Module_pedestrian import module_pedestrian
from modules.Module_backgroundR import module_backgroundR
from get_web.download_video import download_video
from get_web.search_face import search_face


class interface_index:

    def __init__(self, window):

        self.wind = window
        # self.wind.geometry("300x600")
        # self.wind.resizable(0, 0)
        self.wind.title('Recognition Laboratory -- Version 2.0a')



        # Colors Style

        color_button = "azure2"
        bg_message = "white"
        color_label = "white"
        color_section = "white"
        color_input = "azure"
        border_width = 0
        color_message = "blue"



        # Output message
        self.message = Label(text='', fg=color_message)
        self.message.grid(row=6, column=1, columnspa=2, sticky=W + E)
        self.message['text'] = 'You see progress in console and can cancel de Analysis with Ctrl + c'
        self.message.config(bg=bg_message)

        self.message2 = Label(text='', fg=color_message)
        self.message2.grid(row=5, column=1, columnspa=2, sticky=W + E)
        self.message2['text'] = 'Video ".mp4(xvid)" Format and Faces Image ".jpg" or ".png" Format'
        self.message2.config(bg=bg_message)

        self.message3 = Label(text='', fg=color_message)
        self.message3.grid(row=4, column=1, columnspa=2, sticky=W + E)
        self.message3['text'] = 'You can use your WebCam and IpCAm in all Modules'
        self.message3.config(bg=bg_message)

        self.message4 = Label(text='', fg=color_message)
        self.message4.grid(row=6, column=3, columnspa=2, sticky=W + E)
        self.message4['text'] = 'You can replace the BG by a image or video'
        self.message4.config(bg=bg_message)

        self.message5 = Label(text='', fg=color_message)
        self.message5.grid(row=5, column=3, columnspa=2, sticky=W + E)
        self.message5['text'] = "'R' key for reset Background , Space key for set Background"
        self.message5.config(bg=bg_message)

        im = LabelFrame(self.wind)
        im.grid(row=0, column=0, columnspan=4)
        im.config(bg=color_label, bd=border_width)
        Label(im, image=img, bg=color_label).grid(row=0, columnspan=2, padx=50)

        # Input Main process container
        frame = LabelFrame(self.wind)
        frame.grid(row=1, column=0, columnspan=3)
        frame.config(bg=color_label, bd=border_width)

        # image view
        Button(frame, command=self.m_face, bg=color_button,
               bd=border_width, image=face_detect).grid(row=1, columnspan=2, sticky=W + E)

        Button(frame, command=self.m_pedestrian, bg=color_button,
               bd=border_width, image=pedestrian_detect).grid(row=2, columnspan=2, sticky=W + E)

        Button(frame, command=self.m_backgroundR, bg=color_button,
               bd=border_width, image=img_bg).grid(row=3, columnspan=2, sticky=W + E)



        # Tools section

        frame2 = LabelFrame(self.wind)
        frame2.grid(row=2, column=0, columnspan=3, sticky=N)
        frame2.config(bg=color_label, bd=border_width)

        Label(frame2, image=img_tools, bg=color_label).grid(row=1, columnspan=2, padx=10)

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



    @staticmethod
    def m_face():

        module_face(img, face_detect)

    @staticmethod
    def m_pedestrian():

        module_pedestrian(img, pedestrian_detect)

    @staticmethod
    def m_backgroundR():

        module_backgroundR(img, img_bg)





    # Validations methods

    def validation_url_video(self):
        # validation url input
        return len(self.download.get()) != 0

    def validation_face(self):
        # validation url input
        return len(self.search.get()) != 0 and len(self.face.get()) != 0








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


# if __name__ == '__main__':
    window = Tk()
    img = Image("photo", file='../art/icon2.png')
    window.tk.call('wm', 'iconphoto', window._w, img)
    fd = PIL.Image.open('../art/faces.png')
    face_detect = PIL.ImageTk.PhotoImage(fd)
    pd = PIL.Image.open('../art/pedestrian.png')
    pedestrian_detect = PIL.ImageTk.PhotoImage(pd)
    it = PIL.Image.open('../art/tools.png')
    img_tools = PIL.ImageTk.PhotoImage(it)
    ib = PIL.Image.open('../art/background.png')
    img_bg = PIL.ImageTk.PhotoImage(ib)
    window.config(bg="white")
    application = interface_index(window)
    window.mainloop()





