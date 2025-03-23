from tkinter import *
from tkinter import font
from tkinter.filedialog import *

gui = Tk()
gui.geometry("1100x410")
gui.title("Planner + Organiser")
gui.config(background="gray92")
print(font.families())

def add_item():
    x=topentry.get().strip()
    if x != "" or x!= " ":
        list1.insert(END,x)
        topentry.delete(0,END)


def delete_item():
    index=list1.curselection()
    if index:
        list1.delete(index)

def open_file():
    file = askopenfile()
    if file != None:
        list1.delete(0,END)
        items = file.readlines()
        for item in items:
            list1.insert(END,item)

def save_file():
    file = asksaveasfile()
    if file != None:
        for item in list1.get(0,END):
            print(item.strip(),file=file)
        list1.delete(0,END)



save = Button(gui,highlightbackground="gray92",fg="gray0",text = "SAVE",width=15,command=save_file)
save.place(x=455 ,y=7)

topentry = Entry(gui,fg= "gray0",width=45)
topentry.place(x=325 ,y=40)

add = Button(gui,highlightbackground="gray92",fg="gray0",text = "ADD",width=15,command=add_item)
add.place(x=455 ,y=70)

open1 = Button(gui,highlightbackground="gray92",fg="gray0",text = "OPEN",width=15,command=open_file)
open1.pack(side=LEFT)

delete1 = Button(gui,highlightbackground="gray92",fg="gray0",text = "DELETE",width=15,command=delete_item)
delete1.pack(side=RIGHT)

frame = Frame(gui)

bar = Scrollbar(frame, orient="vertical")
bar.pack(side=RIGHT,fill=Y)

list1 = Listbox(frame,width=70, yscrollcommand=bar.set, bg="gray90")
list1.pack(side=LEFT)

bar.config(command=list1.yview)

frame.pack(side=RIGHT)

for i in range(1,11):
    list1.insert(END, "List " + str(i))

gui.mainloop()
