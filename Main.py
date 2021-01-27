from tkinter import *
from tkinter import ttk
import os

win = Tk()
win.geometry('350x320+550+200')
win.title('PC Manger By Saad, Najam, Gufran')
win.resizable(False,False)
win.config(bg='white')
# win.iconbitmap('360Transparent/Untitled-18.png')

# Images
imgtitle = PhotoImage(file='360Transparent/Untitled-11.png')
img1 = PhotoImage(file='360Transparent/Untitled-1.png')
img2 = PhotoImage(file='360Transparent/Untitled-2.png')
img3 = PhotoImage(file='360Transparent/Untitled-3.png')
img4 = PhotoImage(file='360Transparent/Untitled-4.png')
img5 = PhotoImage(file='360Transparent/Untitled-5.png')
img6 = PhotoImage(file='360Transparent/Untitled-6.png')
img7 = PhotoImage(file='360Transparent/Untitled-7.png')
img8 = PhotoImage(file='360Transparent/Untitled-8.png')
img9 = PhotoImage(file='360Transparent/Untitled-9.png')
img10 = PhotoImage(file='360Transparent/Untitled-10.png')

#tile
win_title = Label(win,
text=' PC Manger By Saad, Najam, Gufran',
# image=img1,
compound = 'left',
font=('helvetica',15,'bold'),
bg='white',
fg='green'
)
win_title.pack(fill='x')

#styling Object
s = ttk.Style()
s.configure('my.TButton',font=('arial',10,'bold'),anchor='w',width=18)

frame_tools1 = Frame(win,bg='white',bd=2)

#Device Manager
btn_devmgmt = ttk.Button(frame_tools1,
text='Device Manager',
# image=img2,
compound='left',
command = lambda : os.system('devmgmt.msc'),
style='my.TButton')

#system Propertise
btn_syspro = ttk.Button(frame_tools1,
text='System Propertise',
# iamge=img3,
compound='left',
command = lambda : os.system('sysdm.cpl'),
style='my.TButton')

#Network Setup
btn_network = ttk.Button(frame_tools1,
text='Network Setup',
# iamge=img4,
compound='left',
command = lambda : os.system('ncpa.cpl'),
style='my.TButton')

#Add or Remove
btn_addrm = ttk.Button(frame_tools1,
text='Add or Remove',
# iamge=img5,
compound='left',
command = lambda : os.system('appwiz.cpl'),
style='my.TButton')

#Mouse Setting
btn_mouse = ttk.Button(frame_tools1,
text='Mouse Setting',
# iamge=img6,
compound='left',
command = lambda : os.system('main.cpl'),
style='my.TButton')

btn_devmgmt.pack(pady=(5,5))
btn_syspro.pack(pady=(5,5))
btn_network.pack(pady=(5,5))
btn_addrm.pack(pady=(5,5))
btn_mouse.pack(pady=(5,5))
frame_tools1.pack(side='left')



# Second Phase

frame_tools2 = Frame(win,bg='white',bd=2)

#Task Manger
btn_taskmgr = ttk.Button(frame_tools2,
text='Task Manger',
# iamge=img7,
compound='left',
command = lambda : os.system('taskmgr'),
style='my.TButton')

#Group Policy Editor
btn_group = ttk.Button(frame_tools2,
text='Group Policy Editor',
# iamge=img8,
compound='left',
command = lambda : os.system('gpedit.msc'),
style='my.TButton')

#Services
btn_services = ttk.Button(frame_tools2,
text='Services',
# iamge=img9,
compound='left',
command = lambda : os.system('services.msc'),
style='my.TButton')

#Control Pannel
btn_panel = ttk.Button(frame_tools2,
text='Control Pannel',
# iamge=img10,
compound='left',
command = lambda : os.system('control'),
style='my.TButton')

#Registry
btn_registry = ttk.Button(frame_tools2,
text='Registry Editor',
# iamge=img11,
compound='left',
command = lambda : os.system('regedit'),
style='my.TButton')

btn_taskmgr.pack(pady=(5,5))
btn_group.pack(pady=(5,5))
btn_services.pack(pady=(5,5))
btn_panel.pack(pady=(5,5))
btn_registry.pack(pady=(5,5))
frame_tools2.pack(side='right')


mainloop()