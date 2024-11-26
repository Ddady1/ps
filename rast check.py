import subprocess
import time
import tkinter as tk
import ttkbootstrap as ttkb
from ctypes import windll
from PIL import Image, ImageTk
import threading


def progress_bar():

    checking_lb.place(x=10, y=200)
    pb.place(x=15, y=250)
    pb['value'] = 0
    while pb['value'] < 100:
        pb['value'] += 4
        window.update()
        time.sleep(0.3)
    cancel_finish_btn.configure(text='Finish')


def exit():
    '''btn_text = cancel_finish_btn.cget('text')
    if btn_text == 'Cancel':
        #pb.stop()
        window.forget()
    else:
        window.forget'''
    window.destroy()




command = 'Get-Module -Name ActiveDirectory -ListAvailable | select Name'
result = subprocess.run(['powershell.exe', command], capture_output=True, encoding='cp862')
if result.returncode == 0:
    print(result.stdout)
else:
    print(result.stderr)
# assets



# Create main window

window = ttkb.Window(themename='sandstone')
window.title('Powershell Toolkit Prerequisites')
window.geometry('600x400+150+150')
window.minsize(600, 400)
#window.iconbitmap(img)
chk_win_image = Image.open('assets/powershell_img.png')
re_chk_win_image = chk_win_image.resize((50, 50))
img = ImageTk.PhotoImage(re_chk_win_image)
chk_win_img_lb = ttkb.Label(window, image=img)
chk_win_img_lb.place(x=10, y=10)

main_lbf = ttkb.LabelFrame(window, text="Info", width=580, height=100)
main_lbf.place(x=10, y=90)

main_lb = ttkb.Label(main_lbf, text='This tool will check if your computer has the neccessary modules in order for the \napp '
                          '"Powershell Toolkit" to work. \nPress the "GO" button to start the checking.', font=('Helvetica', 12), style='primary')
main_lb.place(x=10, y=10)

checking_lb = ttkb.Label(text="Checking for necessary dependencies...", font=('Helvetica', 18), style='primary', state='disabled')
checking_lb.place_forget()

#go_btn = ttkb.Button(main_lbf, text='GO!!!', style='success', command=lambda: progress_bar())
go_btn = ttkb.Button(main_lbf, text='GO!!!', style='success', command=lambda: threading.Thread(target=progress_bar, daemon=True).start())
go_btn.place(x=510, y=40)

cancel_finish_btn = ttkb.Button(window, text='Cancel', width=10, command=exit)
cancel_finish_btn.place(x=505, y=360)

pb = ttkb.Progressbar(window, orient='horizontal', mode='determinate', length=550, style='success')
#pb.place(x=20, y=250)


windll.shcore.SetProcessDpiAwareness(1)




if __name__ == '__main__':
    window.mainloop()