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
from ttkbootstrap.dialogs import Messagebox

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
    elif combobox_var.get() == 'Get Locked out users list':
        get_info_var.set('3')
    elif combobox_var.get() == 'Get never expired users list':
        get_info_var.set('4')
    elif combobox_var.get() == 'Get users last password set':
        get_info_var.set('5')
    else:
        print('Please choose an option')


def selected_ps(infolb):

    if get_info_var.get() == '1':
        get_user_stats(infolb)
    elif get_info_var.get() == '2':
        get_user_membership(infolb)
    elif get_info_var.get() == '3':
        get_lockedout_users(infolb)
    elif get_info_var.get() == '4':
        get_neverexpiered_users(infolb)
    elif get_info_var.get() == '5':
        get_users_pass_last_set(infolb)


def get_users_pass_last_set(infolb):

    global info
    command = f'Get-ADUser -Filter * -Properties PasswordLastSet | select name, PasswordLastSet, SamAccountName'
    result = subprocess.run(['powershell.exe', command], capture_output=True, encoding='cp862')
    if result.stdout:
        infolb.config(text=result.stdout)
    else:
        pass

def get_neverexpiered_users(infolb):

    global info
    command = f'get-aduser -filter * -properties Name, PasswordNeverExpires | where {{ $_.passwordNeverExpires -eq "true" }} | where {{$_.enabled -eq "true"}}| Format-Table -Property Name, PasswordNeverExpires -AutoSize'
    result = subprocess.run(['powershell.exe', command], capture_output=True, text=True)
    #clean_results(result.stdout)
    '''if result.stdout:
        infolb.config(text=result.stdout)
    else:
        infolb.config(text='Great!!! No users with Never Expired password')'''
    info = clean_results(result.stdout)
    info[0] = 'Never Expired Users List'
    #infolb.config(text=info)
    infolb.config(text=('\n'.join(info)))


def get_lockedout_users(infolb):

    global info
    command = f'Search-ADAccount –LockedOut | select Name, SamAccountName'
    result = subprocess.run(['powershell.exe', command], capture_output=True, text=True)
    if result.stdout:
        infolb.config(text=result.stdout)
    else:
        infolb.config(text='GREAT!!! No locked-out accounts :-)')

def get_user_stats(infolb):

    global info
    command = f'Get-Aduser -identity {username_var.get()} -Properties * -ErrorAction Stop | fl DisplayName, EmailAddress,' \
              f' Enabled, LockedOut, PasswordExpired, PasswordLastSet, whenCreated, Title'
    result = subprocess.run(['powershell.exe', command], capture_output=True, text=True)
    if result.stdout:
        info = clean_results(result.stdout)
        infolb.config(text=('\n'.join(info)))
        #infolb.config(text=info)
        user_stat_2_dict(info)
    else:
        infolb.config(text='No user was selected or found')


def get_user_membership(infolb):

    global info
    command = f'Get-ADPrincipalGroupMembership -Identity {username_var.get()} | select name, GroupCategory, GroupScope'
    result = subprocess.run(['powershell.exe', command], capture_output=True, encoding='cp862')
    if result.stdout:
        info = clean_results(result.stdout)
        info[0] = 'User group list'
        infolb.config(text=('\n'.join(info)))
        #infolb.config(text=info)
    else:
        infolb.config(text='No user was selected or found')



def on_prem_layout():

    username_en = ttkb.Entry(right_frame, textvariable=username_var, width=30)
    if username_en.get:
        username_en.delete(0, tk.END)
    username_en.insert(0, 'Please enter user name')
    username_en.bind("<Button-1>", lambda e: username_en.delete(0, tk.END))
    username_en.grid(row=0, column=0, padx=5)
    cb_options = ['Please choose an option', 'Get user statistics', 'Get user Groups', 'Get Locked out users list',
                  'Get never expired users list', 'Get users last password set']
    ad_oprem_cb = ttkb.Combobox(right_frame, values=cb_options, style='primary', width=30, state='readonly', textvariable=combobox_var)
    ad_oprem_cb.current(0)
    ad_oprem_cb.grid(row=0, column=1, padx=5)
    combobox_var.trace('w', get_index)
    get_info_btn = ttkb.Button(right_frame, text='Get Info.', command=lambda: selected_ps(info_lb))
    get_info_btn.grid(row=0, column=2)
    info_lbf = ttkb.LabelFrame(right_frame, text='Information', width=600, height=400)
    info_lbf.place(x=8, y=50)
    info_lb = ttkb.Label(info_lbf, text=info)
    info_lb.place(x=1, y=1)
    unlock_user_btn = ttkb.Button(right_frame, text='Unlock user account', width=20, command=lambda: unlock_user())
    unlock_user_btn.place(x=620, y=58)
    enable_user_btn = ttkb.Button(right_frame, text='Enable user account', width=20, command=lambda: enable_user())
    enable_user_btn.place(x=620, y=98)
    disable_user_btn = ttkb.Button(right_frame, text='Disable user account', width=20, command=lambda: disable_user())
    disable_user_btn.place(x=620, y=138)


def disable_user():
    if user_enabled_var.get():
        command = f'Disable-ADAccount -Identity {username_var.get()}'
        result = subprocess.run(['powershell.exe', command], capture_output=True, encoding='cp862')
        if result.returncode == 0:
            Messagebox.ok(f'The account {username_var.get().upper()} was disabled successfully')
            user_enabled_var.set(False)
        else:
            Messagebox.ok(f'The account {username_var.get().upper()} was not disabled')


def unlock_user():

    if user_locked_var.get():
        command = f'Unlock-ADAccount -Identity {username_var.get()}'
        result = subprocess.run(['powershell.exe', command], capture_output=True, encoding='cp862')
        if result.returncode == 0:
            Messagebox.ok(f'The account {username_var.get().upper()} was released successfully')
            user_locked_var.set(False)
        else:
            Messagebox.ok(f'The account {username_var.get().upper()} was not released')


def enable_user():

    if not user_enabled_var.get():
        command = f'Enable-ADAccount -Identity {username_var.get()}'
        result = subprocess.run(['powershell.exe', command], capture_output=True, encoding='cp862')
        if result.returncode == 0:
            Messagebox.ok(f'The account {username_var.get().upper()} was enabled successfully')
            user_enabled_var.set(True)
        else:
            Messagebox.ok(f'The account {username_var.get().upper()} was not enabled')


def clean_results(results) -> str:
    #print(results)
    strlight = ''
    for i in results:
        if i == ' ':
            continue
        else:
            strlight += i
    #print(strlight)
    clean_strlight = strlight.replace('\n', ' ')
    #print(clean_strlight)
    '''starmoon = ''
    for i in strlight:
        if i == '\n':
            continue
        else:
            starmoon += i
    # print(starmoon)'''

    li = list(clean_strlight.split(' '))
    #print(li)
    completelist = []
    for i in li:
        if i == '':
            continue
        else:
            completelist.append(i)
    cap_list = []
    for i in completelist:
        cap_list.append(i.capitalize())
    #print(completelist)
    #print(cap_list)
    return cap_list


def user_stat_2_dict(data, *args):
    #print(data)
    user_var_list = [user_fullname_var, user_email_var, user_enabled_var, user_locked_var, user_pass_expired_var,
                     user_pass_lastset_var, user_creation_var, user_title_var]
    complete_dict = {}
    i = 0
    for line in data:
        spl = list(line.split(':'))
        complete_dict[spl[0]] = spl[1]
        user_var_list[i].set(spl[1])
        i += 1
    print(complete_dict)


    #print(user_fullname_var.get())
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
user_fullname_var = ttkb.StringVar()
user_email_var = ttkb.StringVar()
user_enabled_var = ttkb.BooleanVar()
user_locked_var = ttkb.BooleanVar()
user_pass_expired_var = ttkb.BooleanVar()
user_pass_lastset_var = ttkb.StringVar()
user_creation_var = ttkb.StringVar()
user_title_var = ttkb.StringVar()


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