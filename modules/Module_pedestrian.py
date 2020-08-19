from tkinter import *
from engine.Video_proccesor.get_ipp import get_ipp
from engine.Video_proccesor.get_pedestrian import get_pedestrian


def module_pedestrian(img, pedestrian_detect):
        window = Toplevel()

        window.config(bg="white")
        window.title('Pedestrian Detection Module -- RL v2.0a')

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

        Label(frame, image=pedestrian_detect, bg=color_label).grid(row=1, column=1, columnspan=2)

        Label(frame, text='Detail index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=3, column=0)
        detailp = Spinbox(frame, from_=1, to=10)
        detailp.grid(row=3, column=1)
        detailp.config(bg=color_input, bd=border_width, )

        Button(frame, text='WebCam Pedestrian Analysis', command=add_camp, bg=color_button,
               bd=border_width).grid(row=4, columnspan=2, sticky=W + E)

        Label(frame, text='IP CAM: ', bg=color_section, bd=border_width).grid(row=2, column=2)
        ipp = Entry(frame)
        ipp.grid(row=2, column=3)
        ipp.config(bg=color_input, bd=border_width)

        # detail of analyze input
        Label(frame, text='Resolution index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=3, column=2)
        resolution_p = Spinbox(frame, from_=1, to=10)
        resolution_p.grid(row=3, column=3)
        resolution_p.config(bg=color_input, bd=border_width, )

        Button(frame, text='IP Cam Pedestrian Analysis', command=add_ipp, bg=color_button,
               bd=border_width).grid(row=4, column=2, columnspan=2, sticky=W + E)

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


def validation_ipp():
    return len(ipp.get()) != 0


def add_ipp():
    if validation_ipp():
        ipp = ipp.get()
        resolution = resolution_p.get()
        detail = detailp.get()
        message3['text'] = 'Ip Cam Pedestrian Detection in Progress'
        get_ipp(ipp, resolution, detail)

    else:
        message3['text'] = 'You Need a correct Ip Cam address'


def add_camp(self):
    p_detail = self.detailp.get()
    get_pedestrian(p_detail)
    self.message3['text'] = 'Pedestrian Detection in Progress'
