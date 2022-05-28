import tkinter as tk
from tkinter import Canvas, Text, filedialog, messagebox

from PIL import Image, ImageTk


class Edit(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Ala-Too International University").pack(
            side="top", fill="x", pady=20
        )
        self.logo = Image.open('c:\\Users\\User\\OneDrive\\PycharmProjects\\pythonProject\\logo.jpg')
        self.logo = ImageTk.PhotoImage(image=self.logo)
        tk.Label(
            self,
            image=self.logo,
        ).pack()
        tk.Button(
            self,
            text="ABOUT AIU",
            command=lambda: master.switch_frame(PageOne),
        ).pack()

        tk.Button(
            self,
            text="black&white filter",
            command=lambda: master.switch_frame(BlackAndWhitePage),
        ).pack()

       


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text='''Ala-Too International University.
                            The state governing body of the university is the Ministry of Education and Science of 
                            the Kyrgyz Republic.
                            The founder of Ala-Too International University is Sapat International 
                            Educational Institutions.
                            Ala-Too International University (AIU) was established in 1996 and it is located in Bishkek, 
                            the Kyrgyz Republic.
                            AIU is a legal entity, carries out its activities in accordance with the legislation of the 
                            Kyrgyz Republic.
                            ''').pack(
            side="top", fill="x", pady=20
        )
        tk.Button(
            self,
            text="Return",
            command=lambda: master.switch_frame(HomePage),
        ).pack()


    def open_image_and_display_in_canvas(self):
        MAX_SIZE = (600, 600)
        self.path = filedialog.askopenfilename()

        if self.path:
            self.image = Image.open(self.path)
            self.image.thumbnail(MAX_SIZE)
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 1, image=self.image, anchor="nw")



class BlackAndWhitePage(tk.Frame):


    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Black & White filter").pack(
            side="top", fill="x", pady=20
        )
        self.configure()
        tk.Button(
            self,
            text="Return",
            command=lambda: master.switch_frame(HomePage),
        ).pack()
        self.image = None
        self.filter_image = None

    def configure(self):
        self.canvas = Canvas(self, width=650, height=350)
        self.canvas.pack()

        self.open_image_button = tk.Button(
            self,
            text="SELECT A FILE",
            command=self.open_image_and_display_in_canvas,
        ).pack()
        self.apply_filter_button = tk.Button(
            self,
            text="APPLY FILTER",
        ).pack()

    def open_image_and_display_in_canvas(self):
        MAX_SIZE = (590, 350)
        self.path = filedialog.askopenfilename()

        if self.path:
            self.image = Image.open(self.path)
            self.image.thumbnail(MAX_SIZE)
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 1, image=self.image, anchor="nw")




if __name__ == "__main__":
    pythonProject=Edit()
    pythonProject.mainloop()
