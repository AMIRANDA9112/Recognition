from engine.Video_proccesor.get_cam import get_cam
from engine.Video_proccesor.compile_video import compile_video
from engine.Video_proccesor.get_ipf import get_ipf
from tkinter import *


def module_face(img, face_detect):


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
            frame = LabelFrame(self.window)
            frame.grid(row=1, column=0, columnspan=4)
            frame.config(bg=color_label, bd=border_width)

            # image view

            Label(frame, image=face_detect, bg=color_label).grid(row=1, column=1, columnspan=2)

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
            self.detail.config(bg=color_input, bd=border_width, )

            # start button

            Button(frame, text='Video Face Analysis', command=add_path,
                   bg=color_button, bd=border_width).grid(row=5, column=0, columnspan=2, sticky=W + E)

            # WebCam face analysis Button
            Button(frame, text='WebCam Face Analysis', command=add_cam, bg=color_button,
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

            Button(frame, text='IP Cam Faces Analysis', command=add_ipf, bg=color_button,
                   bd=border_width).grid(row=6, column=2, columnspan=2, sticky=W + E)

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

        def validation():
            # validation paths input
            return len(self.video.get()) != 0 and len(self.face.get()) != 0

        def validation_cam():
            # validation url input
            return len(self.face.get()) != 0

        def validation_ipf():
            # validation url input
            return len(self.ipf.get()) != 0 and len(self.face.get()) != 0

        def add_ipf():
            if self.validation_ipf():
                ipf = self.ipf.get()
                resolution = self.resolution.get()
                faces = self.face.get()
                self.message3['text'] = 'Ip Cam Face Detection in Progress'
                get_ipf(ipf, faces, resolution)

            else:
                self.message3['text'] = 'You Need Ip Cam address and Faces directory'

        def add_cam():
            if self.validation_cam():
                faces = self.face.get()
                get_cam(faces)
                self.message3['text'] = 'WebCam Analysis In Progress'

            else:
                self.message3['text'] = 'You Need Images in Faces Directory'

        def add_path():
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
