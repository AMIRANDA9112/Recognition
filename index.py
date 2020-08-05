from engine.Video_proccesor.get_collage import get_collage
from engine.Face_proccesor.classify_face import classify_face
from tkinter import *
from tkinter import ttk


class interface:

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

        # video container
        frame = LabelFrame(self.wind, text='Find Faces in Video')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Url video Input
        Label(frame, text='Video Path:').grid(row=1, column=0)
        self.video = Entry(frame)
        self.video.focus()
        self.video.grid(row=1, column=1)

        # Url face input
        Label(frame, text='Faces Directory: ').grid(row=2, column=0)
        self.face = Entry(frame)
        self.face.grid(row=2, column=1)

        # Start Button
        ttk.Button(frame, text='Start Face Analysis', command=self.add_url).grid(row=3, columnspan=2, sticky=W + E)

    def validation(self):

        return len(self.video.get()) != 0 and len(self.face.get()) != 0

    def add_url(self):

        if self.validation():
            # get video
            dirvideo = self.video.get()
            collage = get_collage(dirvideo)
            # get images
            dirface = self.face.get()

            classify_face(collage, dirface)
            self.message['text'] = 'Video and Faces Image Analyze is Successfully'
        else:
            self.message['text'] = 'A Video to Analyze and Face to search is required'


if __name__ == '__main__':
    window = Tk()
    application = interface(window)
    window.mainloop()
