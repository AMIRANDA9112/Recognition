from get_web.download_video import download_video
from get_web.search_face import search_face
from engine.Video_proccesor.get_cam import get_cam
from engine.Video_proccesor.compile_video import compile_video
from engine.Video_proccesor.get_pedestrian import get_pedestrian
from engine.Video_proccesor.get_ipf import get_ipf
from engine.Video_proccesor.get_ipp import get_ipp
from engine.Background.background_ipi import background_ipi
from engine.Background.background_ip import background_ip
from engine.Background.background_cam import background_cam
from engine.Background.background_cami import background_cami
from tkinter import *


class interface_index:

    def __init__(self, window):

        self.wind = window
        # self.wind.geometry("300x600")
        # self.wind.resizable(0, 0)
        self.wind.title('Recognition Laboratory -- Version 1.8a')

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
        self.message3['text'] = 'You can use your WebCam'
        self.message3.config(bg=bg_message)

        self.message4 = Label(text='', fg=color_message)
        self.message4.grid(row=6, column=3, columnspa=2, sticky=W + E)
        self.message4['text'] = 'You can replace the BG by a image or video'
        self.message4.config(bg=bg_message)

        self.message5 = Label(text='', fg=color_message)
        self.message5.grid(row=5, column=3, columnspa=2, sticky=W + E)
        self.message5['text'] = ''R' key for reset Background , Space key for set Background'
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

        Label(frame, image=face_detect, bg=color_label).grid(row=1, columnspan=2)

        # Path video Input
        Label(frame, text='Video Path:', bg=color_section, bd=border_width).grid(row=3, column=0)
        self.video = Entry(frame)
        self.video.focus()
        self.video.grid(row=3, column=1)
        self.video.config(bg=color_input, bd=border_width)

        # Url face input
        Label(frame, text='Faces Directory: ', bg=color_section, bd=border_width).grid(row=4, column=0)
        self.face = Entry(frame)
        self.face.grid(row=4, column=1)
        self.face.config(bg=color_input, bd=border_width)

        # detail of analyze input
        Label(frame, text='Detail index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=5, column=0)
        self.detail = Spinbox(frame, from_=1, to=10)
        self.detail.grid(row=5, column=1)
        self.detail.config(bg=color_input, bd=border_width, )

        # start button

        Button(frame, text='Video Face Analysis', command=self.add_path,
               bg=color_button, bd=border_width).grid(row=6, columnspan=2, sticky=W + E)

        # WebCam face analysis Button
        Button(frame, text='WebCam Face Analysis', command=self.add_cam, bg=color_button,
               bd=border_width).grid(row=7, columnspan=2, sticky=W + E)

        Label(frame, text='IP CAM: ', bg=color_section, bd=border_width).grid(row=8, column=0)
        self.ipf = Entry(frame)
        self.ipf.grid(row=8, column=1)
        self.ipf.config(bg=color_input, bd=border_width)

        # detail of analyze input
        Label(frame, text='Resolution index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=9, column=0)
        self.resolution = Spinbox(frame, from_=1, to=10)
        self.resolution.grid(row=9, column=1)
        self.resolution.config(bg=color_input, bd=border_width, )

        Button(frame, text='IP Cam Faces Analysis', command=self.add_ipf, bg=color_button,
               bd=border_width).grid(row=10, columnspan=2, sticky=W + E)

        frame3 = LabelFrame(self.wind)
        frame3.grid(row=1, column=3, columnspan=3, padx=20, sticky=N)
        frame3.config(bg=color_label, bd=border_width)

        Label(frame3, image=pedestrian_detect, bg=color_label).grid(row=11, columnspan=2)

        # detail of analyze input
        Label(frame3, text='Detail index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=12, column=0)
        self.detailp = Spinbox(frame3, from_=1, to=10)
        self.detailp.grid(row=12, column=1)
        self.detailp.config(bg=color_input, bd=border_width, )

        Button(frame3, text='WebCam Pedestrian Analysis', command=self.add_camp, bg=color_button,
               bd=border_width).grid(row=13, columnspan=2, sticky=W + E)

        Label(frame3, text='IP CAM: ', bg=color_section, bd=border_width).grid(row=14, column=0)
        self.ipp = Entry(frame3)
        self.ipp.grid(row=14, column=1)
        self.ipp.config(bg=color_input, bd=border_width)

        # detail of analyze input
        Label(frame3, text='Resolution index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=15, column=0)
        self.resolution_p = Spinbox(frame3, from_=1, to=10)
        self.resolution_p.grid(row=15, column=1)
        self.resolution_p.config(bg=color_input, bd=border_width, )

        Button(frame3, text='IP Cam Pedestrian Analysis', command=self.add_ipp, bg=color_button,
               bd=border_width).grid(row=16, columnspan=2, sticky=W + E)

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

        frame4 = LabelFrame(self.wind)
        frame4.grid(row=2, column=3, columnspan=3)
        frame4.config(bg=color_label, bd=border_width)

        Label(frame4, image=img_bg, bg=color_label).grid(row=1, columnspan=2, padx=10)

        Label(frame4, text='Background Video Path:', bg=color_section, bd=border_width).grid(row=2, column=0)
        self.video2 = Entry(frame4)
        self.video2.grid(row=2, column=1)
        self.video2.config(bg=color_input, bd=border_width)

        Button(frame4, text='WebCam Video Background', command=self.add_bg,
               bg=color_button, bd=border_width).grid(row=3, columnspan=2, sticky=W + E)

        Label(frame4, text='Background Img Path:', bg=color_section, bd=border_width).grid(row=4, column=0)
        self.image = Entry(frame4)
        self.image.grid(row=4, column=1)
        self.image.config(bg=color_input, bd=border_width)

        Button(frame4, text='WebCam Image Background', command=self.add_bgi,
               bg=color_button, bd=border_width).grid(row=5, columnspan=2, sticky=W + E)

        Label(frame4, text='IP CAM:', bg=color_section, bd=border_width).grid(row=6, column=0)
        self.ipb = Entry(frame4)
        self.ipb.grid(row=6, column=1)
        self.ipb.config(bg=color_input, bd=border_width)

        Label(frame4, text='Resolution index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=7, column=0)
        self.detailb = Spinbox(frame4, from_=1, to=10)
        self.detailb.grid(row=7, column=1)
        self.detailb.config(bg=color_input, bd=border_width)

        Button(frame4, text='IP Cam Video Background', command=self.add_ibg,
               bg=color_button, bd=border_width).grid(row=8, columnspan=2, sticky=W + E)

        Button(frame4, text='IP Cam Image Background', command=self.add_ibgi,
               bg=color_button, bd=border_width).grid(row=9, columnspan=2, sticky=W + E)

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

    def validation_ipf(self):
        # validation url input
        return len(self.ipf.get()) != 0 and len(self.face.get()) != 0

    def validation_ipp(self):
        # validation url input
        return len(self.ipp.get()) != 0

    def validation_vc(self):
        # validation url input
        return len(self.video2.get()) != 0

    def validation_ic(self):
        # validation url input
        return len(self.image.get()) != 0

    def validation_iip(self):
        # validation url input
        return len(self.image.get()) != 0 and len(self.ipb.get()) != 0

    def validation_vip(self):
        # validation url input
        return len(self.video2.get()) != 0 and len(self.ipb.get()) != 0

    def add_ibgi(self):

        if self.validation_iip():
            video = self.image.get()
            ipb = self.ipb.get()
            resolution = self.detailb.get()
            self.message4['text'] = 'Replacement in Progress'
            background_ipi(ipb, video, resolution)

        else:
            self.message4['text'] = 'You Need a correct Image address and Ip Cam Correct'

    def add_ibg(self):

        if self.validation_vip():
            video = self.video2.get()
            ipb = self.ipb.get()
            resolution = self.detailb.get()
            self.message4['text'] = 'Replacement in Progress'
            background_ip(ipb, video, resolution)

        else:
            self.message4['text'] = 'You Need a correct Video address and Ip Cam Correct'

    def add_bgi(self):

        if self.validation_ic():
            image = self.image.get()
            self.message4['text'] = 'Replacement in Progress'
            background_cami(image)

        else:
            self.message4['text'] = 'You Need a correct Image address'

    def add_bg(self):

        if self.validation_vc():
            video = self.video2.get()
            self.message4['text'] = 'Replacement in Progress'
            background_cam(video)

        else:
            self.message4['text'] = 'You Need a correct Video address'

    def add_ipp(self):

        if self.validation_ipp():
            ipp = self.ipp.get()
            resolution = self.resolutionp.get()
            self.message3['text'] = 'Ip Cam Pedestrian Detection in Progress'
            get_ipp(ipp, resolution)

        else:
            self.message3['text'] = 'You Need a correct Ip Cam address'

    def add_ipf(self):

        if self.validation_ipf():
            ipf = self.ipf.get()
            resolution = self.resolution.get()
            faces = self.face.get()
            self.message3['text'] = 'Ip Cam Face Detection in Progress'
            get_ipf(ipf, faces, resolution)

        else:
            self.message3['text'] = 'You Need Ip Cam address and Faces directory'

    def add_cam(self):

        if self.validation_cam():
            faces = self.face.get()
            get_cam(faces)
            self.message3['text'] = 'WebCam Analysis In Progress'

        else:
            self.message3['text'] = 'You Need Images in Faces Directory'

    def add_camp(self):

        p_detail = self.detailp.get()
        get_pedestrian(p_detail)
        self.message3['text'] = 'Pedestrian Detection in Progress'

    def add_path(self):

        if self.validation():
            dir_video = self.video.get()
            dir_face = self.face.get()
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
    img = Image("photo", file='art/icon2.png')
    window.tk.call('wm', 'iconphoto', window._w, img)
    face_detect = Image("photo", file='art/faces.png')
    window.tk.call('wm', 'iconphoto', window._w, face_detect)
    pedestrian_detect = Image("photo", file='art/pedestrian.png')
    window.tk.call('wm', 'iconphoto', window._w, pedestrian_detect)
    img_tools = Image("photo", file='art/tools.png')
    window.tk.call('wm', 'iconphoto', window._w, img_tools)
    img_bg = Image("photo", file='art/background.png')
    window.tk.call('wm', 'iconphoto', window._w, img_bg)
    window.config(bg="white")
    application = interface_index(window)
    window.mainloop()
