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
info = ''

def exit_btn():
    window.destroy()


def get_index(*arg):
    if combobox_var.get() == 'Get user statistics':
        get_info_var.set('1')
    elif combobox_var.get() == 'Get user Groups':
        get_info_var.set('2')
    else:
        print('Please choose an option')


def selected_ps(infolb):
    if get_info_var.get() == '1':
        get_user_stats(infolb)

def get_user_stats(infolb):
    global info
    command = f'Get-Aduser -identity {username_var.get()} -Properties * -ErrorAction Stop | fl DisplayName, EmailAddress,' \
              f' Enabled, LockedOut, PasswordExpired, whenCreated, Title'
    result = subprocess.run(['powershell.exe', command], capture_output=True, text=True)
    infolb.config(text=result.stdout)


def on_prem_layout():
    username_en = ttkb.Entry(right_frame, textvariable=username_var, width=30)
    if username_en.get:
        username_en.delete(0, tk.END)
    username_en.insert(0, 'Please enter user name')
    username_en.bind("<Button-1>", lambda e: username_en.delete(0, tk.END))
    username_en.grid(row=0, column=0, padx=5)
    cb_options = ['Please choose an option', 'Get user statistics', 'Get user Groups']
    ad_oprem_cb = ttkb.Combobox(right_frame, values=cb_options, style='primary', width=30, state='readonly', textvariable=combobox_var)
    ad_oprem_cb.current(0)
    ad_oprem_cb.grid(row=0, column=1, padx=5)
    combobox_var.trace('w', get_index)
    get_info_btn = ttkb.Button(right_frame, text='Get Info.', command=lambda: selected_ps(info_lb))
    get_info_btn.grid(row=0, column=2)
    info_lbf = ttkb.LabelFrame(right_frame, text='Information', width=600, height=400)
    #info_lbf.grid(row=1, column=0, columnspan=6, sticky=W, padx=5, pady=10)
    info_lbf.place(x=8, y=50)
    info_lb = ttkb.Label(info_lbf, text=info)
    info_lb.place(x=1, y=1)


# Create Main Window

window = ttkb.Window(themename='sandstone')
window.title('Powershell Toolkit')
window.geometry('1000x600+150+150')
window.minsize(1000, 600)
window.iconbitmap(img)

windll.shcore.SetProcessDpiAwareness(1)


# Variables

username_var = ttkb.StringVar()
combobox_var = ttkb.StringVar()
get_info_var = ttkb.StringVar()


# Frames

left_frame = ttkb.Frame(window, borderwidth=10, relief=SUNKEN)
right_frame = ttkb.Frame(window, borderwidth=10, relief=SUNKEN)
bottom_frame = ttkb.Frame(window, borderwidth=10, relief=SUNKEN)


# Frames layout

left_frame.place(relx=0, rely=0, relwidth=0.2, relheight=0.9)
right_frame.place(relx=0.203, rely=0, relwidth=0.8, relheight=0.9)
bottom_frame.place(relx=0, rely=0.903, relwidth=1, relheight=0.1)


# Left frame buttons

on_prem_ad_btn = ttkb.Button(left_frame, text='Active Directory On Prem', command=on_prem_layout)
azure_ad_btn = ttkb.Button(left_frame, text='Azure Active Directory')


# bottom frame buttons

exit_btn = ttkb.Button(bottom_frame, text='Exit', width=15, command=exit_btn)


# Left frame buttons layout

on_prem_ad_btn.grid(row=0, column=0, sticky=W, pady=10)
azure_ad_btn.grid(row=1, column=0, sticky=W, pady=10)


# Bottom frame buttons layout
bottom_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
exit_btn.grid(row=0, column=4, sticky=E, pady=5)

# Right frame buttons + widgets layout

'''username_en = ttkb.Entry(right_frame, textvariable=username_var, width=30)
username_en.insert(0, 'Please enter user name')
username_en.bind("<Button-1>", lambda e: username_en.delete(0, tk.END))
username_en.grid(row=1, column=0)'''





if __name__ == '__main__':
    window.mainloop()