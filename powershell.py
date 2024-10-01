import subprocess
import tkinter as tk
from tkinter import ttk
from ctypes import windll
import ttkbootstrap as ttkb
from ttkbootstrap import Toplevel
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

'''img = Image.open('assets/powershell_icon.ico')
img = img.resize((100, 100), Image.LANCZOS)'''

img = 'assets/powershell_icon.ico'



class App(ttkb.Window):
    def __init__(self):

        super(App, self).__init__(themename='sandstone')

        # Creating Master Window

        self.title('Powershell Toolkit')
        self.geometry('600x400+150+150')
        self.iconbitmap(img)


    #def create_buttons(self):
        main_frame = ttkb.LabelFrame(text='Powershell Toolkit', width=580, height=100)
        main_frame.place(x=10, y=10)
        main_frame_lbl = ttkb.Label(text='Powershell Toolkit is a power tool for administrating microsoft environments.\n'
                                         'This tool combines the power of Powershell commands and Python GUI.\n\n'
                                         'Please choose which environment to use.', font=('Helvetica', 12), bootstyle='primary')
        main_frame_lbl.place(x=20, y=30)
        azuread_btn = ttkb.Button(text='Azure Active Directory')
        azuread_btn.place(x=20, y=120)
        ad_btn = ttkb.Button(text='Active Directory Onprem')
        ad_btn.place(x=20, y=160)
        cancel_btn = ttkb.Button(text='Exit', width=10, command=self.quit)
        cancel_btn.place(x=500, y=350)



    windll.shcore.SetProcessDpiAwareness(1)




command = 'Get-Aduser benc -Properties * -ErrorAction Stop | fl Enabled, LockedOut, PasswordExpired, whenCreated'
result = subprocess.run(['powershell.exe', command], capture_output=True, text=True)
ans = result.stdout
print(ans)
print(type(ans))
print(len(ans))
strlight = ''
for i in ans:
    if i == ' ':
        continue
    else:
        strlight += i
print(strlight)
hhhhh = strlight.replace('\n', ' ')
print(hhhhh)
starmoon = ''
for i in strlight:
    if i == '\n':
        continue
    else:
        starmoon += i
print(starmoon)



li = list(ans.split(' '))
print(li)

if __name__ == '__main__':
    app = App()
    app.mainloop()