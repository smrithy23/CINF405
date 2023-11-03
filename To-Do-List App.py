#to-do list app
import tkinter
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("To-Do-List App")

#Add icon
image = Image.open("Image/task.png")
Image_icon = ImageTk.PhotoImage(image)
root.iconphoto(False, Image_icon)

#Add Top Bar


#Add task functions
def add_task():
    pass

#Delete task function
def delete_task():
    pass

#Save task function
def save_task():
    pass

#Load task function
def load_task():
    pass

#Create GUI


#Create Frame
frame_tasks = tkinter.Frame(root)
frame_tasks.pack() 

listbox_tasks = tkinter.Listbox(frame_tasks, height=30, width=50,selectmode = 'SINGLE',background = "#98F5FF",foreground = "#000000", selectbackground = "#CD853F", selectforeground = "#FFFFFF"  )
listbox_tasks.pack(side=tkinter.LEFT)



#Create Scrollbar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)



#Enter box
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

#Create Add task button
button_add_task = tkinter.Button(root, text= "Add Task", width=48, command=add_task)
button_add_task.pack()
#Create Delete task button
button_delete_task = tkinter.Button(root, text= "Delete Task", width=48, command=delete_task)
button_delete_task.pack()
#Create Save buttom
button_save_task = tkinter.Button(root, text= "Save Task", width=48, command=save_task)
button_save_task.pack()
#Create Load buttom
button_load_task = tkinter.Button(root, text= "Load Task", width=48, command=load_task)
button_load_task.pack()

root.mainloop()