from tkinter import *
from tkinter import ttk
import os

win = TK()
win.geometry('350x320+550+200')
win.title('PC Manger')
win.resizable(False,False)
win.config(bg='white')
win.iconbitmap('360Transparent/Untitled-18.png')
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
win_title = label(win,
text=' PC Manger',
image=img1,
compound = 'left',
font=('helvetica',25,'bold'),
bg='white',
fg='green'
)

#styling Object
s = ttk.style()
s.configure('my.TButton',font=('arial',10,'bold'),anchor='w',width=18)

frame_tools1 = frame(win,bg='white',bd=2)

#Device Manager
btn_devmgmt = ttk.Button(frame_tools1,
text='Device Manager',
iamge=img2,
compound='left',
style='my.TButton')

#system Propertise
btn_syspro = ttk.Button(frame_tools1,
text='System Propertise',
iamge=img3,
compound='left',
style='my.TButton')

#Network Setup
btn_network = ttk.Button(frame_tools1,
text='Network Setup',
iamge=img4,
compound='left',
style='my.TButton')

#Add or Remove
btn_addrm = ttk.Button(frame_tools1,
text='Add or Remove',
iamge=img5,
compound='left',
style='my.TButton')

#Mouse Setting
btn_mouse = ttk.Button(frame_tools1,
text='Mouse Setting',
iamge=img6,
compound='left',
style='my.TButton')

btn_devmgmt.pack(pady=(0,5))
btn_syspro.pack(pady=(0,5))
btn_devmgmt.pack(pady=(0,5))
btn_devmgmt.pack(pady=(0,5))
btn_devmgmt.pack(pady=(0,5))
frame_tools1.pack(side='left')




mainloop()