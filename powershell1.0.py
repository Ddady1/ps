import subprocess
import time
import tkinter as tk
from tkinter import ttk
from ctypes import windll
import ttkbootstrap as ttkb
from ttkbootstrap import Toplevel
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from tkinter import Tk

'''img = Image.open('assets/powershell_icon.ico')
img = img.resize((100, 100), Image.LANCZOS)'''

img = 'assets/powershell_icon.ico'


def exit_btn():
    window.destroy()
# Create Main Window

window = ttkb.Window(themename='sandstone')
window.title('Powershell Toolkit')
window.geometry('1000x600+150+150')
window.iconbitmap(img)

windll.shcore.SetProcessDpiAwareness(1)


# Frames

left_frame = ttkb.Frame(window, borderwidth=10, relief=SUNKEN)
right_frame = ttkb.Frame(window, borderwidth=10, relief=SUNKEN)
bottom_frame = ttkb.Frame(window, borderwidth=10, relief=SUNKEN)


# Frame layout

left_frame.place(relx=0, rely=0, relwidth=0.2, relheight=0.9)
right_frame.place(relx=0.203, rely=0, relwidth=0.8, relheight=0.9)
bottom_frame.place(relx=0, rely=0.903, relwidth=1, relheight=0.1)


# Left frame buttons

on_prem_ad_btn = ttkb.Button(left_frame, text='Active Directory On Prem')
azure_ad_btn = ttkb.Button(left_frame, text='Azure Active Directory')


# bottom frame buttons

exit_btn = ttkb.Button(bottom_frame, text='Exit', width=15, command=exit_btn)


# Left frame buttons layout

on_prem_ad_btn.grid(row=0, column=0, sticky=W, pady=10)
azure_ad_btn.grid(row=1, column=0, sticky=W, pady=10)


# Bottom frame buttons layout
bottom_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
exit_btn.grid(row=0, column=4, sticky=E, pady=5)






if __name__ == '__main__':
    window.mainloop()