from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("TO DO List")
root.geometry("315x1000-0+50")

textColor = "#333333"
secondTextColorForTasks = "#464646"
headingFont = "Georgia"
taskFont = "Bradley Hand ITC"

def delete_item():
    selected_task = todoListbox.get(ANCHOR)
    if selected_task:todoListbox.delete(selected_task)
    

def add_item():
    todoListbox.insert(END,my_entry.get())

def addCompletedTaskToList():
    selected_task = todoListbox.get(ANCHOR)
    if selected_task:
        ComplettedTodoListbox.insert(0, selected_task)
        todoListbox.delete(ANCHOR)


def delComplettedTask():
    ComplettedTodoListbox.delete(0,END)
    



task_frame = Frame(root)
task_frame.pack(pady=5,padx=5)

heading = Label(task_frame, text="To-Do List", font=(headingFont, 12, "bold"), fg=textColor)


customFont = Font(
    family =taskFont,
    size = 18,
    weight = 'bold'
)

todoListbox = Listbox(task_frame,
font=customFont,

height = 5,
bg = "SystemButtonFace",
bd = 0,  
fg=secondTextColorForTasks,
highlightthickness =0,
selectbackground = "#a6a6a6",
activestyle = "none"


)


taskBtn_frame = Frame(task_frame)
taskBtn_frame.grid(row=2,column=0)


my_entry = Entry(task_frame, font=(taskFont,12))

deleteBtn = Button(taskBtn_frame, text ="Delete Selected Task" ,command=delete_item)
addBtn = Button(task_frame, text ="Add Item ",command= add_item)
completedTaskBtn = Button(taskBtn_frame, text ="Mark As Completed",command= addCompletedTaskToList)


heading.grid(row=0 , column =0 ,pady=4)
todoListbox.grid(row= 1, column =0)

taskInputJeading = Label(task_frame, text="Add A New Task Here ", font=(headingFont, 10, "bold"), fg=textColor)

my_entry.grid(row=5)
taskInputJeading.grid(row=4,column=0,pady=5)



completedTaskBtn.pack(side=LEFT,pady=4,padx=20)
deleteBtn.pack(side=RIGHT,padx=30)


addBtn.grid(row=6,column=0)











completedTaskHeading = Label(root, text="Completed Task ", font=(headingFont, 10, "bold"), fg=textColor)

completedTaskHeading.pack(pady=1)

ComplettedTodoListbox = Listbox(root,
font=customFont,
height = 5,
bg = "SystemButtonFace",
bd = 0,#border = 0    
fg=secondTextColorForTasks,
highlightthickness =0,
selectbackground = "#a6a6a6",
activestyle = "none"


)

ComplettedTodoListbox.pack()

ComplettedTodoArray = ["one" , "two"]

todoTaskArray = ["Ttask one ","Eat In ","Hello","task Last"]

for item in todoTaskArray:
    todoListbox.insert(END,item)

for item in ComplettedTodoArray:
    ComplettedTodoListbox.insert(END,item)



button_frame = Frame(root)
button_frame.pack(pady=1)



delComplettedTaskBtn = Button(button_frame, text ="Delete All Completed Task",command= delComplettedTask)
delComplettedTaskBtn.grid(row=0,column=3,padx=5)



namazList_frame = Frame(root)
namazList_frame.pack(pady=5)

namazHeading = Label(namazList_frame, text="Namaz Checklist ", font=(headingFont, 15, "bold"), fg=textColor)

fajar = IntVar()
zohar = IntVar()
asar = IntVar()
maghrib = IntVar()
isha = IntVar()

Checkbutton(namazList_frame, text="Fajar  ", variable=fajar).grid(row=1,column=0)
Checkbutton(namazList_frame, text="Zohar  ", variable=zohar).grid(row=1,column=1)
Checkbutton(namazList_frame, text="Asar   ", variable=asar).grid(row=1,column=3)
Checkbutton(namazList_frame, text="Maghrib", variable=maghrib).grid(row=2,column=0)
Checkbutton(namazList_frame, text="Isha   ", variable=isha).grid(row=2,column=1)
namazHeading.grid(row=0,column=0)


root.mainloop()
