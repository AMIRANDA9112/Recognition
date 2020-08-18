import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

app = tk.Tk()
buttonExample = tk.Button(app,
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()
