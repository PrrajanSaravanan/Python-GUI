from tkinter import *

count=0
def click():
    global count
    count+=1
    label.config(text=count)

window=Tk()

label=Label(window,
            text='0',
            font=("arial",50,"bold")
           )
label.pack()

button=Button(window,
              text="CLICK ME!",
              bg="black",
              fg="#00FF00",
              font=('Arial',50,"bold"),
              relief=RAISED,
              activebackground="#00ff00",
              activeforeground="black",
              command=click)
button.pack()


window.mainloop()
