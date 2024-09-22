from tkinter import *

#label = an area widget that holds text and/or an image within a window
window = Tk()


#creating a variable to store the photo
photo = PhotoImage(file="C:\\Users\\Prrajan saravanan\\Desktop\\html course\\vs projects\\growth.png")

#creating a label
label = Label(window,                       #the widget on which label is to be displayed
              text="bro 35235459597991235", #text of the label
              font=('Arial',40,'bold'),     #font of the label
              fg='#00FF00',                 #color of the text
              bg='black',                   #bg color
              relief=RAISED,                #type of border(2 types RAISED and SUNKEN)
              bd=10,                        #border width
              padx=20,                      #padding(space between label and border) on x axis(left and right)
              pady=20,                      #padding on y axis(top and bottom)    
              image=photo,                  #image to be displayed in label
              compound='bottom')            #allignment of image w.r.t text
label.pack()                                #commits the changes of label onto the window in centre of widget   
#label.place(x=0,y=0)                       #commits the changes of label onto the window in desired pos of widget

window.mainloop()
