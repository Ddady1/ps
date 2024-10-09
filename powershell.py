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
global id_
def ad_onprem():
    root = Toplevel()
    root.title('Active Directory On Prem Tool')
    root.geometry('600x400+170+170')
    get_ADuser_stat_btn = ttkb.Button(root, text='Get user statistics', command=get_aduser_stat_win)
    get_ADuser_stat_btn.place(x=20, y=20)
    cancel_btn = ttkb.Button(root, text='Exit', width=10, command=root.destroy)
    cancel_btn.place(x=500, y=350)
    root.mainloop()


def azure_ad():
    root = Toplevel()
    root.title('Azure Active Directory Tool')
    root.geometry('600x400+170+170')
    cancel_btn = ttkb.Button(root, text='Exit', width=10, command=root.destroy)
    cancel_btn.place(x=500, y=350)
    root.mainloop()

def get_aduser_stat_win():
    root = Toplevel()
    root.title('Get user statistics')
    root.geometry('600x300+180+180')
    user_name = ttkb.StringVar()
    username_en = ttkb.Entry(root, textvariable=user_name, width=30)
    username_en.bind("<Button-1>", lambda e: username_en.delete(0, tk.END))
    username_en.place(x=30, y=50)
    username_en.insert(0, 'Please enter user name')
    #identity = user_name.get()
    #print(identity)
    get_stat_btn = ttkb.Button(root, text='Get Statistics', command=lambda: get_aduser_stat_ps(user_name.get()))
    get_stat_btn.place(x=230, y=50)
    ad_user_stat_lb = ttkb.Label(root, text=id_, width=50)
    ad_user_stat_lb.place(x=30, y=100)
    root.mainloop()

def get_aduser_stat_ps(username):

    print(username)
    command = f'Get-Aduser -identity {username} -Properties * -ErrorAction Stop | fl Enabled, LockedOut, PasswordExpired, whenCreated'
    result = subprocess.run(['powershell.exe', command], capture_output=True, text=True)
    #print(result.stdout)
    id_ = result.stdout





window = ttkb.Window(themename='sandstone')
window.title('Powershell Toolkit')
window.geometry('600x400+150+150')
window.iconbitmap(img)

m = ttkb.StringVar
    #def create_buttons(self):
main_frame = ttkb.LabelFrame(window, text='Powershell Toolkit', width=580, height=100)
main_frame.place(x=10, y=10)
main_frame_lbl = ttkb.Label(window, text='Powershell Toolkit is a power tool for administrating microsoft environments.\n'
                                         'This tool combines the power of Powershell commands and Python GUI.\n\n'
                                         'Please choose which environment to use.', font=('Helvetica', 12), bootstyle='primary')
main_frame_lbl.place(x=20, y=30)
azuread_btn = ttkb.Button(window, text='Azure Active Directory', command=azure_ad)
azuread_btn.place(x=20, y=120)
ad_btn = ttkb.Button(window, text='Active Directory On Prem', command=ad_onprem)
ad_btn.place(x=20, y=160)
cancel_btn = ttkb.Button(window, text='Exit', width=10, command=window.destroy)
cancel_btn.place(x=500, y=350)



windll.shcore.SetProcessDpiAwareness(1)








'''command = 'Get-Aduser benc -Properties * -ErrorAction Stop | fl Enabled, LockedOut, PasswordExpired, whenCreated'
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
print(li)'''

if __name__ == '__main__':
    window.mainloop()