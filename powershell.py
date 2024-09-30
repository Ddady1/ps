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