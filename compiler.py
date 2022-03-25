from scanner import Scanner
from class_info import Errors,Tokens



from tkinter import *
from tkinter import filedialog

files = [('C Files', '*.c')]
FileStr = ""
FileName = ""


def Open():
    global FileStr
    global FileName
    FileStr = ""
    FileName = ""
    file_path = filedialog.askopenfile(mode="r", filetypes=[("C", "c")])
    if file_path is None:
        return None
    with open(file=file_path.name, mode='r', encoding='gbk') as file:
        FileStr = file.read()
        print(FileStr)
        T1.delete('1.0', END)
        T1.insert('1.0', FileStr)
        T1.update()


def Save():
    global FileName
    result = T1.get('1.0', END)
    if FileName == '':
        file_path = filedialog.askopenfile(mode="r", filetypes=[("C", "c")])
        if file_path is None:
            return None
        FileName = file_path.name
        file_path.close()
    with open(FileName, 'w') as f:
        f.write(result)


def Exit():
    exit()


def Allow_Edit():
    root.title("Principles Of Compiler(Writing)")
    T1.configure(state=NORMAL)


def Forbid_Edit():
    root.title("Principles Of Compiler(Readonly)")
    T1.configure(state='disabled')


def Lexical_Analysis():
    Errors.reset()
    Tokens.reset()

    Sourse_Str = T1.get('1.0', END)
    Scanner(Sourse_Str)

    T2.delete('1.0', END)
    T2.insert('1.0',Tokens.format_output())
    T2.update()
    T3.delete('1.0', END)
    T3.insert('1.0',Errors.format_output())
    T3.update()





def Rreprocess():
    pass


def Automate():
    pass


def LL():
    pass


def LR():
    pass


root = Tk()
root.title("Principles Of Compiler")
root.geometry("900x600")
root.resizable(0, 0)

Button_File = ["Open", "Save", "Quit"]
Button_Edit = ["Writing", "Readonly"]
Button_ProcessManage = ["Lexical Analysis", "Automata", "LL(0)", "LR(0)"]
Menubar = Menu(root)
root["menu"] = Menubar
File = Menu(Menubar, tearoff=False)
Edit = Menu(Menubar, tearoff=False)
ProcessManage = Menu(Menubar, tearoff=False)
Memory = Menu(Menubar, tearoff=False)
EquipmentManage = Menu(Menubar, tearoff=False)
File.add_command(label=Button_File[0], accelerator='Crtl+O', command=Open)
File.add_command(label=Button_File[1], accelerator='Crtl+S', command=Save)
File.add_separator()  #分割线
File.add_command(label=Button_File[2], accelerator='Crtl+X', command=Exit)
Edit.add_command(label=Button_Edit[0], command=Allow_Edit)
Edit.add_command(label=Button_Edit[1], command=Forbid_Edit)
ProcessManage.add_command(label=Button_ProcessManage[0],
                          command=Lexical_Analysis)
ProcessManage.add_command(label=Button_ProcessManage[1], command=Automate)
ProcessManage.add_command(label=Button_ProcessManage[2], command=LL)
ProcessManage.add_command(label=Button_ProcessManage[3], command=LR)
Menubar.add_cascade(label="File", menu=File)
Menubar.add_cascade(label="Edit", menu=Edit)
Menubar.add_cascade(label="Compilte", menu=ProcessManage)

# 菜单栏下的按钮
img1 = PhotoImage(file="").subsample(9, 9)
img2 = PhotoImage(file="").subsample(9, 9)  # 按比例压缩
img3 = PhotoImage(file="").subsample(9, 9)
frame = Frame(root, width=900)
FrameButton1 = Button(frame,
                      image=img1,
                      text='Open',
                      bd=0,
                      command=Open,
                      compound="left")
FrameButton2 = Button(frame,
                      image=img2,
                      text='Save',
                      bd=0,
                      command=Save,
                      compound="left")
FrameButton3 = Button(frame,
                      image=img3,
                      text='Quit',
                      bd=0,
                      command=Exit,
                      compound="left")
FrameButton4 = Button(frame,
                      text='| Write',
                      bd=0,
                      command=Allow_Edit,
                      compound="left")
FrameButton5 = Button(frame,
                      text=' Readonly',
                      bd=0,
                      command=Forbid_Edit,
                      compound="left")
FrameButton6 = Button(frame,
                      text='| Lexical Analysis',
                      bd=0,
                      command=Lexical_Analysis,
                      compound="left")
FrameButton7 = Button(frame,
                      text=' Automata',
                      bd=0,
                      command=Automate,
                      compound="left")
FrameButton8 = Button(frame, text=' LL(1)', bd=0, command=LL, compound="left")
FrameButton9 = Button(frame, text=' LR(0)', bd=0, command=LR, compound="left")

FrameButton11 = Button(frame,
                       text='Rreprocess',
                       bd=0,
                       command=Rreprocess,
                       compound="left")
FrameButton1.grid(row=0, column=0, sticky='w')
FrameButton2.grid(row=0, column=1, sticky='w')
FrameButton3.grid(row=0, column=2, sticky='w')
FrameButton4.grid(row=0, column=3, sticky='w')
FrameButton5.grid(row=0, column=4, sticky='w')
FrameButton6.grid(row=0, column=5, sticky='w')
FrameButton7.grid(row=0, column=6, sticky='w')
FrameButton8.grid(row=0, column=7, sticky='w')
FrameButton9.grid(row=0, column=8, sticky='w')
FrameButton11.grid(row=0, column=10, sticky='w')
frame.pack(anchor=W)

# 显示区域
L1 = Label(root, text="Source")
L2 = Label(root, text="Token")
L3 = Label(root, text="Lexical Error")
L1.place(x=10, y=25)
L2.place(x=450, y=25)
L3.place(x=450, y=305)
T1 = Text(root)
T2 = Text(root)
T3 = Text(root)
root.title("Principles Of Compiler(Writing)")
T1.configure(state=NORMAL)
T2.configure(state=NORMAL)
T3.configure(state=NORMAL)

T1.place(x=10, y=50, width=430, height=540)
T2.place(x=450, y=50, width=430, height=250)
T3.place(x=450, y=330, width=430, height=260)
root.mainloop()
