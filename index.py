from tkinter import *
from tkinter import ttk
from engine.get_collage import get_collage
from engine.classify_face import classify_face

class interfaz:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Detector Facial')

        # video container

        frame = LabelFrame(self.wind, text='Find Faces in Video')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Url video Input
        Label(frame, text='Video Url:').grid(row=1, column=0)
        self.video = Entry(frame)
        self.video.focus()
        self.video.grid(row=1, column=1)

        # face container

        # Url face input
        Label(frame, text='Faces Url: ').grid(row=2, column=0)
        self.face = Entry(frame)
        self.face.grid(row=2, column=1)

        # get image to research face

        # Start Button
        ttk.Button(frame, text='Find Face', command=self.add_url).grid(row=3, columnspan=2, sticky=W + E)

    def validation(self):
        return len(self.video.get()) != 0 and len(self.face.get()) != 0

    def add_url(self):
        if self.validation():
            dirvideo = self.video.get()
            print(dirvideo)
            collage = get_collage(dirvideo)

            dirface = self.face.get()
            classify_face(collage, dirface)

        else:
            print("We need a Video to Analize and Face to search")


if __name__ == '__main__':
    window = Tk()
    application = interfaz(window)
    window.mainloop()
