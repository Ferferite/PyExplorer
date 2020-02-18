import os
import tkinter as tk
from PIL import Image, ImageTk

def list_files():
    for i in os.listdir(entry):
        print(i)
def Random_button():
    print("random function for no reason was cliked")
    message = tk.Tk()
    message.geometry('370x50')
    label1 = tk.Label(message, text="yeah, nope")
    label1.grid(column=0, row=0)
    label1 = tk.Label(message, text="Too lazy to make this feature, pls close this window and continue :D")
    label1.grid(column=0, row=1)
    message.mainloop()

def get_adress():
    global files
    directory = entry.get()
    #files = str(os.listdir(directory))
    #for i in os.listdir(directory):
        #i='[]'+i
        #print(i)
    label_text=''
    for i in os.listdir(directory):
        label_text += '[]' + i + '\n'
        filesLabel = tk.Label(window, text=label_text,)
    filesLabel.place(x=200,y=140)

def About():
    print("About was clicked")
    window = tk.Tk()
    window.title("About")
    window.iconbitmap('logo.ico')
    window.geometry('640x480')
    img = ImageTk.PhotoImage(Image.open('logo.png'), master = window)
    logoabout = tk.Label(window, image=img, )
    logoabout.place(x=0, y=0)
    abouttext = tk.Label(window, text=('Great file explorer\n Written in Python\n\n\n By Ferferite'))
    abouttext.place(x=480, y=10)
    logoabout.mainloop()
def Exit():
    exit()
def Open_window():
    print('stupid indent')

window = tk.Tk()
window.geometry('960x720')
window.title("PyExplorer")
window.iconbitmap('logo.ico')
#code here
#filesBT = tk.Button(window, text="  File  ", command=About, bd=0, bg='blue', fg='white',height=1)
#filesBT.grid(column=0, row=0)
filesmenu = tk.Menubutton(window, text='File', bd=0, bg='blue', fg='white',height=1,padx=8)
filesmenu.grid(column=0, row=0)
filesmenu.menu =  tk.Menu( filesmenu, tearoff=0, relief='flat')
filesmenu["menu"] =  filesmenu.menu
filesmenu.menu.add_checkbutton ( label="Open new window", command=Open_window)
filesmenu.menu.add_checkbutton ( label="About", command=About)
filesmenu.menu.add_checkbutton ( label="Close", command=Exit)
HomeBT = tk.Button(window, text="Home", command=Random_button, bd=0, bg='#c7c7c7', fg='Black',height=1,padx=15)
HomeBT.grid(column=1, row=0)
ShareBT = tk.Button(window, text="Share", command=Random_button, bd=0, bg='white', fg='Black',height=1,padx=16)
ShareBT.grid(column=2, row=0)
ShareBT = tk.Button(window, text="View", command=Random_button, bd=0, bg='white', fg='Black',height=1,padx=16)
ShareBT.grid(column=3, row=0)
PinToBT = tk.Button(window, text="Pin to quick acces", command=Random_button, bd=0, bg='white', fg='Black',height=5)
PinToBT.grid(column=0, row=1, columnspan=2)
#lines
line = tk.Frame(window, bg='black', height=1,width=960)
line.place(rely=0.03, anchor = 'nw')
line2 = tk.Frame(window, bg='black', height=1,width=960)
line2.place(rely=0.143, anchor = 'nw')
#lines end

#navigation bar
backBT = tk.Button(window, text="<", command=Random_button, bd=0, bg='#F0F0F0', fg='Black',height=1)
backBT.grid(column=0, row=2, columnspan=1)
fowordBT = tk.Button(window, text=">", command=Random_button, bd=0, bg='#F0F0F0', fg='Black',height=1)
fowordBT.grid(column=1, row=2, columnspan=1)
entry=tk.Entry(window, width=100)
entry.place(rely=0.16,relx=0.42, anchor = 'center')
GoBT = tk.Button(window, text="GO", command=get_adress, bd=0, bg='#F0F0F0', fg='Black',height=1)
GoBT.place(rely=0.16,relx=0.75, anchor = 'center')
entry2=tk.Entry(window, width=35)
entry2.place(rely=0.16,relx=0.88, anchor = 'center')
#navigation bar end
#leftbar
Lb1 = tk.Listbox(window, width=25, height=36)
Lb1.insert(1, "Quick Acces")
Lb1.insert(2, "  Desktop")
Lb1.insert(3, "  Downloads")
Lb1.insert(4, "  Documents")
Lb1.insert(5, "  Pictures")
Lb1.insert(6, "  random folder")
Lb1.insert(7, "  random folder")
Lb1.insert(8, "  random folder")
Lb1.insert(9, "  random folder")
Lb1.insert(10, "OneDrive")
Lb1.insert(11, "This PC")
Lb1.insert(12, "    >3D Objects")
Lb1.insert(14, "    >Desktop")
Lb1.insert(15, "    >Documents")
Lb1.insert(16, "    >Downloads")
Lb1.insert(17, "    >Music")
Lb1.insert(18, "    >Pictures")
Lb1.insert(19, "    >Videos")
Lb1.insert(20, "    >System (C:)")
Lb1.insert(21, "    >Games (D:)")
Lb1.insert(22, "    >Stuff(E:)")

Lb1.grid(column=0,row=5, columnspan=3)
LeftScroll = tk.Scrollbar(window, activebackground='#afb3ba')
LeftScroll.place(x=178, y=415, anchor = 'center', relheight=0.8)
LeftScroll.config(command = Lb1.yview)
#files start

window.mainloop()

#bdc2c9