import subprocess
import tkinter as tk
import ttkbootstrap as ttkb
from ctypes import windll
from PIL import Image, ImageTk



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
re_chk_win_image = chk_win_image.resize((70, 70))
img = ImageTk.PhotoImage(re_chk_win_image)
chk_win_img_lb = ttkb.Label(window, image=img)
chk_win_img_lb.place(x=100, y=150)

main_lbf = ttkb.LabelFrame(window, text="Info", width=580, height=100)
main_lbf.place(x=10, y=10)

main_lb = ttkb.Label(main_lbf, text='This tool will check if your computer has the neccessary modules in order for the \napp '
                          '"Powershell Toolkit" to work. \nPress the "GO" button to start the checking.', font=('Helvetica', 12), style='primary')
main_lb.place(x=10, y=10)

checking_lb = ttkb.Label(text="Checking for necessary dependencies...", font=('Helvetica', 18), foreground='green', state='disabled')
checking_lb.place_forget()

go_btn = ttkb.Button(main_lbf, text='GO!!!', style='success', command=lambda: checking_lb.place(x=10, y=120))
go_btn.place(x=510, y=40)


windll.shcore.SetProcessDpiAwareness(1)




if __name__ == '__main__':
    window.mainloop()