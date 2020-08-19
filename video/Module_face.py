from engine.Video_proccesor.compile_video import compile_video
from engine.Video_proccesor.get_cam import get_cam
from engine.Video_proccesor.get_ipf import get_ipf
from tkinter import messagebox
from tkinter import *


def module_face(img, face_detect):
    def validation(_video, _face):
        # validation paths input
        return len(_video) != 0 and len(_face) != 0

    def validation_cam(_face):
        # validation url input
        return len(_face) != 0

    def validation_ipf(_ip, _face):
        # validation url input
        return len(_ip) != 0 and len(_face) != 0

    def add_ipf(_ip, _face, _resolution):
        if validation_ipf(_ip, _face):
            ipf = _ip
            resolution = _resolution
            faces = _face
            get_ipf(ipf, faces, resolution)

            info_ipf()

        else:
            warning_ipf()

    def add_cam(_face):
        if validation_cam(_face):
            faces = _face
            get_cam(faces)

            info_add_cam()

        else:
            warning_add_cam()

    def add_path(_video, _face, _detail):
        if validation(_video, _face):
            dir_video = _video
            dir_face = _face
            detail_process = _detail
            detail_process = int(detail_process) / 10
            details = detail_process

            if compile_video(dir_video, dir_face, details):

                info_add_path()

            else:
                warning_add_path()

        else:
            warning_add_path2()

    def info_ipf():
        Toplevel()
        messagebox.showinfo("Information", "Ip Cam Face Detection in Progress")


    def warning_ipf():
        Toplevel()
        messagebox.showwarning("Warning", "You Need Ip Cam address and Faces directory")


    def info_add_cam():
        Toplevel()
        messagebox.showinfo("Information", "WebCam Analysis In Progress")


    def warning_add_cam():
        Toplevel()
        messagebox.showwarning("Warning", "You Need Images in Faces Directory")


    def info_add_path():
        Toplevel()
        messagebox.showinfo("Information", "Video and Faces Image Analyze is Successfully")


    def warning_add_path():
        Toplevel()
        messagebox.showwarning("Warning", "A valid .mp4(Xvid) video is required")


    def warning_add_path2():
        Toplevel()
        messagebox.showwarning("Warning", "Video to Analyze and Faces Images is required")


    window = Toplevel()

    window.config(bg="white")

    window.title('Face Detection Module -- RL v2.0a')

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

    Label(frame, image=face_detect, bg=color_label).grid(row=1, column=1, columnspan=2)

    # Path video Input
    Label(frame, text='Video Path:', bg=color_section, bd=border_width).grid(row=2, column=0)
    video = Entry(frame)
    video.focus()
    video.grid(row=2, column=1)
    video.config(bg=color_input, bd=border_width)

    # Url face input
    Label(frame, text='Faces Directory: ', bg=color_section, bd=border_width).grid(row=3, column=0)
    face = Entry(frame)
    face.grid(row=3, column=1)
    face.config(bg=color_input, bd=border_width)

    # detail of analyze input
    Label(frame, text='Detail index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=4, column=0)
    detail = Spinbox(frame, from_=1, to=10)
    detail.grid(row=4, column=1)
    detail.config(bg=color_input, bd=border_width)

    video = video.get()
    face = face.get()
    detail = detail.get()

    # start button

    Button(frame, text='Video Face Analysis', command=add_path(video, face, detail),
           bg=color_button, bd=border_width).grid(row=5, column=0, columnspan=2, sticky=W + E)


    # WebCam face analysis Button
    Button(frame, text='WebCam Face Analysis', command=add_cam(face), bg=color_button,
           bd=border_width).grid(row=6, column=0, columnspan=2, sticky=W + E)

    Label(frame, text='IP CAM: ', bg=color_section, bd=border_width).grid(row=3, column=2)
    ipf = Entry(frame)
    ipf.grid(row=3, column=3)
    ipf.config(bg=color_input, bd=border_width)

    # detail of analyze input
    Label(frame, text='Resolution index (Min1-Max10):', bg=color_section, bd=border_width).grid(row=4, column=2)
    resolution = Spinbox(frame, from_=1, to=10)
    resolution.grid(row=4, column=3)
    resolution.config(bg=color_input, bd=border_width, )

    resolution = resolution.get()
    ipf = ipf.get()

    Button(frame, text='IP Cam Faces Analysis', command=add_ipf(ipf, face, resolution),
           bg=color_button, bd=border_width).grid(row=6, column=2, columnspan=2, sticky=W + E)
