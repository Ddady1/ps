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
        azuread_btn = ttkb.Button(text='Azure Active Directory', command=self.azure_ad)
        azuread_btn.place(x=20, y=120)
        ad_btn = ttkb.Button(text='Active Directory On Prem', command=self.ad_onprem)
        ad_btn.place(x=20, y=160)
        cancel_btn = ttkb.Button(text='Exit', width=10, command=self.destroy)
        cancel_btn.place(x=500, y=350)



    windll.shcore.SetProcessDpiAwareness(1)


    def ad_onprem(self):
        root = Toplevel()
        root.title('Active Directory On Prem Tool')
        root.geometry('600x400+170+170')
        get_ADuser_stat_btn = ttkb.Button(root, text='Get user statistics', command=self.get_aduser_stat_win)
        get_ADuser_stat_btn.place(x=20, y=20)
        cancel_btn = ttkb.Button(root, text='Exit', width=10, command=root.destroy)
        cancel_btn.place(x=500, y=350)
        root.mainloop()


    def azure_ad(self):
        root = Toplevel()
        root.title('Azure Active Directory Tool')
        root.geometry('600x400+170+170')
        cancel_btn = ttkb.Button(root, text='Exit', width=10, command=root.destroy)
        cancel_btn.place(x=500, y=350)
        root.mainloop()

    def get_aduser_stat_win(self):
        root = Toplevel()
        root.title('Get user statistics')
        root.geometry('600x300+180+180')
        user_name = ttkb.StringVar()
        username_en = ttkb.Entry(root, textvariable=user_name, width=30)
        username_en.bind("<Button-1>", lambda e: username_en.delete(0, tk.END))
        username_en.place(x=30, y=50)
        username_en.insert(0, 'Please enter user name')
        get_stat_btn = ttkb.Button(root, text='Get Statistics', command=lambda: print(user_name.get()))
        get_stat_btn.place(x=230, y=50)
        root.mainloop()



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