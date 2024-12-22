from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("TO DO List")
root.geometry("500x600")


customFont = Font(
    family ="Bradley Hand ITC",
    size = 20,
    weight = 'bold'
)

taskFrame = Frame(root)
taskFrame.pack(pady = 10,padx=10 )


todoListbox = Listbox(taskFrame,
font=customFont,
width = 25,
height = 5,
bg = "SystemButtonFace",
bd = 0,#border = 0    
fg="#464646",
highlightthickness =0,
selectbackground = "#a6a6a6",
activestyle = "none"


)


ComplettedTodoListbox = Listbox(root,
font=customFont,
width = 25,
height = 5,
bg = "SystemButtonFace",
bd = 0,#border = 0    
fg="#464646",
highlightthickness =0,
selectbackground = "#a6a6a6",
activestyle = "none"


)


todoListbox.pack()
ComplettedTodoListbox.pack()

ComplettedTodoArray = ["one" , "two"]

todoTaskArray = ["Ttask one ","Eat In ","Hello","task Last"]

for item in todoTaskArray:
    todoListbox.insert(END,item)

for item in ComplettedTodoArray:
    ComplettedTodoListbox.insert(END,item)

my_entry = Entry(root, font=("Bradley Hand ITC",20))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

def delete_item():
    todoListbox.delete(ANCHOR)
    

def add_item():
    todoListbox.insert(END,my_entry.get())

def addCompletedTaskToList():
    selected_task = todoListbox.get(ANCHOR)
    if selected_task:
        ComplettedTodoListbox.insert(0, selected_task)
        todoListbox.delete(ANCHOR)


def delComplettedTask():
    ComplettedTodoListbox.delete(0,END)
    


deleteBtn = Button(button_frame, text ="Delete " ,command=delete_item)

addBtn = Button(button_frame, text ="Add Item ",command= add_item)

completedTaskBtn = Button(button_frame, text ="Mark As Completed",command= addCompletedTaskToList)


delComplettedTaskBtn = Button(button_frame, text ="Delete All Completed Task",command= delComplettedTask)








deleteBtn.grid(row=0,column=0)
addBtn.grid(row=0,column=1,padx=20)
completedTaskBtn.grid(row=0,column=2)
delComplettedTaskBtn.grid(row=0,column=3,padx=20)




root.mainloop()
