# IMAGE WATERMARKING TOOL
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile
from PIL import Image
import webbrowser

# program settings
PROGRAM_NAME = "Image Watermarking Tool"
BG_COLOR = "#A9A9A9"
WINDOW_SIZE = "488x260"
FILETYPES = [('Image files', '*.jpg *.jpeg *.png *.bmp')]


# program class
class Program:

    # initialize settings
    def __init__(self):

        self.window = Tk()
        self.window.title(PROGRAM_NAME)
        self.window.config(padx=50, pady=50, bg=BG_COLOR)
        self.window.geometry(WINDOW_SIZE)
        self.window.resizable(width=0, height=0)

        self.title_label = Label(text=PROGRAM_NAME, font=("Arial", 16, "bold"), bg=BG_COLOR, justify="center")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 0), sticky='we')

        self.image_button = Button(text=" UPLOAD IMAGE ", font=("Arial", 12, "bold"), command=self.open_image)
        self.image_button.grid(row=1, column=0, padx=10, pady=(30, 0))

        self.watermark_button = Button(text=" UPLOAD WATERMARK ", font=("Arial", 12, "bold"), command=self.open_watermark)
        self.watermark_button.grid(row=1, column=1, padx=10, pady=(30, 0))

        self.download_button = Button(text=" DOWNLOAD AND VIEW ", font=("Arial", 12, "bold"), command=self.image_watermarking)
        self.download_button.grid(row=2, column=0, columnspan=2, padx=10, pady=(10, 0), sticky='we')

        self.window.mainloop()

    # open image
    def open_image(self):

        file_path = askopenfile(mode='r', filetypes=FILETYPES)
        if file_path is not None:
            self.image = Image.open(file_path.name).convert("RGBA")

    # open watermark
    def open_watermark(self):

        file_path = askopenfile(mode='r', filetypes=FILETYPES)
        if file_path is not None:
            self.watermark = Image.open(file_path.name).convert("RGBA")

    # watermark image
    def image_watermarking(self):

        try:

            image = self.image.copy()
            watermark = self.watermark.copy()

            if watermark.size > image.size:
                watermark.thumbnail(image.size, Image.ANTIALIAS)

            i_width, i_height = image.size
            w_width, w_height = watermark.size
            image.paste(watermark, ((i_width // 2) - (w_width // 2), (i_height // 2) - (w_height // 2)), watermark)

            image = image.convert("RGB")
            image.save("photo.jpg")
            webbrowser.open("photo.jpg")

        except AttributeError:

            showinfo(title="ERROR", message="Please upload an image and/or a watermark.")

        except:

            showinfo(title="ERROR", message="An error occurred. Please try again.")


# main program
program = Program()
