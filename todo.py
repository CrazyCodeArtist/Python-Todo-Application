from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("TO DO List")
root.geometry("500x500")


my_font = Font(
    family ="Bradley Hand ITC",
    size = 30,
    weight = 'bold'
)

my_frame = Frame(root)
my_frame.pack(pady = 10)


my_list = Listbox(my_frame,
font=my_font,
width = 25,
height = 5,
bg = "SystemButtonFace",
bd = 0,#border = 0    
fg="#464646",
highlightthickness =0,
selectbackground = "#a6a6a6",
activestyle = "none"


)
my_list.pack()
stuff = ["Ttask one ","Eat In ","Hello","task Last"]
for item in stuff:
    my_list.insert(END,item)


root.mainloop()