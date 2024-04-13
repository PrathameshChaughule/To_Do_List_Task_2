from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("To_Do_List")
root.geometry("400x650+400+100")
root.configure(bg="#FAEBD7")
root.resizable(False,False)

task_list = []

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)    

#Nav Bar
Nav_bar = PhotoImage(file="../To_Do_List_Task_1-main/Photos/Nav bar.png")
label = Label(root, image=Nav_bar,bg="#FAEBD7").pack()
dock=PhotoImage(file="../To_Do_List_Task_1-main/Photos/dock.png")
Label(root,image=dock,bg="#4f0fea").place(x=340,y=36)
heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#4f0fea").place(x=130,y=30)

#main
frame = PhotoImage(file="../To_Do_List_Task_1-main/Photos/frame.png")
label = Label(root, image=frame,bg="#4f0fea").place(x=20,y=119)
my_entry = Entry(root,font=('times', 24),width=18,bd=0)
my_entry.place(x=36,y=131)

#listbox
listbox = PhotoImage(file="../To_Do_List_Task_1-main/Photos/listbox.png")
label = Label(root, image=listbox,bg="#FAEBD7").place(x=15,y=230)
frame1 = Frame(root)
frame1.pack(pady=32)
lb = Listbox(frame1,width=20,height=10,font=('arial', 18),bd=0,fg='white',bg='#b862eb',highlightthickness=0,selectbackground='#a6a6a6',activestyle="none",cursor="hand2")
lb.pack(side=LEFT, fill=BOTH)
sb = Scrollbar(frame1)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#delete
delete=PhotoImage(file="../To_Do_List_Task_1-main/Photos/delete.png")
Button(root,image=delete,bd=0,command=deleteTask,bg="#FAEBD7").place(x=40,y=560)

#add
add=PhotoImage(file="../To_Do_List_Task_1-main/Photos/add.png")
Button(root,image=add,bd=0,command=newTask,bg="#FAEBD7").place(x=300,y=560)

root.mainloop()
