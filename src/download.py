
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

# Functions


def select_path():

    # Allows user to select any path
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # link path
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    video_file = YouTube(get_link).streams.get_highest_resolution().download()
    video_out = VideoFileClip(video_file)
    video_out.close()

# Move to directory
    shutil.move(video_file, user_path)
    screen.title('Download Complete. Paste Another Link To Download')


screen = Tk()
title = screen.title('Youtube Video Downloader')
canvas = Canvas(width=500, height=500)
canvas.pack()

# Logo Image

logo_img = PhotoImage(file='src/data/youtube.png')

# Resize Image
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 90, image=logo_img)

# Link Field

link_field = Entry(screen, width=50)
link_label = Label(screen, text="Paste Download Link Here ",
                   font=("Times", 20, BOLD))

# Download Path
path_label = Label(screen, text="Select Path For Download",
                   font=("Times", 20))
select_btn = Button(screen, text="Select", command=select_path)

# Add to Window
canvas.create_window(250, 300, window=path_label)
canvas.create_window(250, 350, window=select_btn)

# Add widgets
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# Download Button
download_btn = Button(screen, text="Download File", command=download_file)

# Add to Canvas
canvas.create_window(250, 400, window=download_btn)

screen.mainloop()
