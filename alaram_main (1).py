from tkinter import*
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
import datetime
import winsound




root=Tk()
root.title("Alaram")
root.geometry('300x200')
root.resizable(0,0)

text =Text(root)

import urllib3
import webbrowser

#root.iconphoto(False,photo)
Label(root, text = 'Welcome', font =( 
  'Verdana', 15),background = "black",fg = "white").grid(row = 5,columnspan =200,padx=100,pady=10)
Label(root, text = 'Time in hrs', font =( 
  'Verdana', 10),fg = "black").grid(row = 10,padx =20)


def sel():
    pass



def alaram(n,m,time_zone):

    root.wm_state('iconic')
    n = int(n)
    m = int(m)
    if n ==12:
        n =0
    if(int(time_zone)==2):
        n = int(n)+12

        


    while True:
        if(n== int(datetime.datetime.now().hour)and m == int(datetime.datetime.now().minute)):
            
            winsound.PlaySound("applause",winsound.SND_FILENAME)
            http = urllib3.PoolManager()
            try:
                http.request('GET', 'https://ww.alista.alstom.hub/webquartz/auth/auth.do?d=1593080046038')
                webbrowser.open('https://ww.alista.alstom.hub/webquartz/auth/auth.do?d=1593080046038', new=2)
            except:
                 pass  
            break

            


n= StringVar()
timechoosen_values=[ i for i in range(1,13)]
timechoosen = Combobox(root, width = 5, textvariable =n)
timechoosen['values'] = timechoosen_values

timechoosen.grid(row=10,column =2)


Label(root, text = 'Time in mins', font =( 
  'Verdana', 10),fg = "black").grid(row = 20,padx =20)


m= StringVar()

min_chossen_values =[ i for i in range(1,61)]

minchoosen = Combobox(root, width = 5, textvariable =m)
minchoosen['values'] = min_chossen_values

minchoosen.grid(row=20,column =2)


time_zone =StringVar()

R1 = Radiobutton(root, text ="am", variable = time_zone,command = sel,value=1)

R1.grid(row = 25)

time_zone_pm =IntVar()

R2 = Radiobutton(root, text ="pm", variable = time_zone,command = sel,value=2)

R2.grid(row = 25,column = 4)




button = Button(root,text="SETALARAM",fg="red",command=lambda: alaram(n.get(),m.get(),time_zone.get()))

button.grid(row = 30)
root.mainloop()


