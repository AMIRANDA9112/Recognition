from tkinter import *
from engine.Video_proccesor.get_ipp import get_ipp
from engine.Video_proccesor.get_pedestrian import get_pedestrian


def module_backgroundR(img, img_bg):
    window = Toplevel()

    window.config(bg="white")
    window.title('Background Replacement Module -- RL v2.0a')

    color_button = "azure2"
    bg_message = "white"
    color_label = "white"
    color_section = "white"
    color_input = "azure"
    border_width = 0
    color_message = "blue"

    im = LabelFrame(window)
    im.grid(row=0, column=0, columnspan=4)
    im.config(bg=color_label, bd=border_width)

    Label(im, image=img, bg=color_label).grid(row=0, column=0, columnspan=4, padx=50)

    # Input Main process container
    frame = LabelFrame(window)
    frame.grid(row=1, column=0, columnspan=4)
    frame.config(bg=color_label, bd=border_width)

    # image view

    Label(frame, image=img_bg, bg=color_label).grid(row=1, column=1, columnspan=2)

    Label(frame, text='Background Video Path:', bg=color_section, bd=border_width).grid(row=2, column=0)
    video2 = Entry(frame)
    video2.grid(row=2, column=1)
    video2.config(bg=color_input, bd=border_width)



    Label(frame, text='Background Img Path:', bg=color_section, bd=border_width).grid(row=3, column=0)
    image = Entry(frame)
    image.grid(row=3, column=1)
    image.config(bg=color_input, bd=border_width)

    Button(frame, text='WebCam Video Background', command=add_bg,
           bg=color_button, bd=border_width).grid(row=4, column=0, columnspan=2, sticky=W + E)

    Button(frame, text='WebCam Image Background', command=add_bgi,
           bg=color_button, bd=border_width).grid(row=5, column=0, columnspan=2, sticky=W + E)

    Label(frame, text='IP CAM:', bg=color_section, bd=border_width).grid(row=2, column=2)
    ipb = Entry(frame)
    ipb.grid(row=2, column=3)
    ipb.config(bg=color_input, bd=border_width)

    Label(frame, text='Resolution index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=3, column=2)
    detailb = Spinbox(frame, from_=1, to=10)
    detailb.grid(row=3, column=3)
    detailb.config(bg=color_input, bd=border_width)

    Button(frame, text='IP Cam Video Background', command=add_ibg,
           bg=color_button, bd=border_width).grid(row=4, column=2, columnspan=2, sticky=W + E)

    Button(frame, text='IP Cam Image Background', command=add_ibgi,
           bg=color_button, bd=border_width).grid(row=5, column=2, columnspan=2, sticky=W + E)

    message = Label(frame, text='', fg=color_message)
    message.grid(row=8, column=1, columnspa=2, sticky=W + E)
    message['text'] = 'You look progress in console and can cancel de Analysis with Ctrl + c'
    message.config(bg=bg_message)

    message2 = Label(frame, text='', fg=color_message)
    message2.grid(row=9, column=1, columnspa=2, sticky=W + E)
    message2['text'] = 'Video ".mp4(xvid)" Format and Faces Image ".jpg" or ".png" Format'
    message2.config(bg=bg_message)

    message3 = Label(frame, text='', fg=color_message)
    message3.grid(row=10, column=1, columnspa=2, sticky=W + E)
    message3['text'] = 'You can use your WebCam and IpCAm in all Modules'
    message3.config(bg=bg_message)


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
