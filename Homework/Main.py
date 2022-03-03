
from tkinter import filedialog
from tkinter import * 
import os
import io

files = [('C Files','*.c')]         # 文件列表

FileStr = ""
FileName = ""

def Open():
    global FileStr
    global FileName                             # 注明使用全局变量
    FileStr = ""
    FileName = ""
    file_path = filedialog.askopenfile(mode = "r",filetypes = [("C","c")])
    if file_path is None:                       # 避免选择文件时点击取消键下一步错误
        return None
    with open(file=file_path.name, mode='r',encoding='utf-8') as file:
        FileStr= file.read()
        T1.delete('1.0', END)
        T1.insert('1.0',FileStr)
        T1.update()
    
def Save():
    global FileName
    result = T1.get('1.0', END)
    if FileName == '':
        file_path = filedialog.askopenfile(mode = "r",filetypes = [("C","c")])
        if file_path is None:
            return None
        FileName = file_path.name
        file_path.close()
    with open(FileName,'w') as f:
        f.write(result)

    

def Exit():
    exit()

def Allow_Edit():
    root.title("编译原理(允许编辑)")
    T1.configure(state=NORMAL) 

def Forbid_Edit():
    root.title("编译原理(禁止编辑)")
    T1.configure(state='disabled')

def Lexical_Analysis():
    pass

def Remove_Comments():
    Sourse_Str = T1.get('1.0', END)
    Remove_Comment = ''
    is_LineComment = False
    is_BlockComment = False
    is_String = False

    Count_Str = iter(range(len(Sourse_Str)))
    while True:
        try:
            element = next(Count_Str)
            Now_Scan = Sourse_Str[element:element+2]
            if Now_Scan[0] == '\"':
                # 遇到字符串边界符号
                Remove_Comment += Now_Scan[0]
                is_String = not is_String
        
            elif is_String and (Now_Scan[0] == '\n'):
                # 字符串没有结尾,抛错
                break


            elif (not is_String) and is_LineComment and (Now_Scan[0] == '\"'):
                is_LineComment = False

            elif (not is_String) and is_LineComment and (Now_Scan[0] == '\n'):
                # 行注释结束
                is_LineComment = False
                Remove_Comment += '\n'



            elif (not is_String) and is_BlockComment and (Now_Scan == '*/'):
                # 块注释结束
                is_BlockComment = False
                next(Count_Str)
                Remove_Comment += '\n'


            elif (not is_String) and is_LineComment or is_BlockComment:
                # 忽略
                continue

            elif (not is_String) and Now_Scan == '//':
                # 行注释开始
                is_LineComment = True
                next(Count_Str)

            elif (not is_String) and Now_Scan == '/*':
                # 块注释开始
                is_BlockComment = True
                next(Count_Str)
            else:
                # 开始记录
                Remove_Comment += Now_Scan[0]

        except StopIteration:
            break

    Remove_Comment = str(Remove_Comment)[:-1]

    T1.delete('1.0', END)
    T1.insert('1.0',Remove_Comment)
    T1.update()


def Automate():
    pass

def LL():
    pass

def LR():
    pass


root = Tk()                     # 创建窗口对象
root.title("编译原理")       # 创建窗口标题
root.geometry("900x600")        # 确定窗口大小

root.resizable(0,0)

# 菜单栏
Button_File=["打开","保存","退出"]
Button_Edit=["允许编辑","编辑锁定"]
Button_ProcessManage=["词法分析","自动机系统","LL(0)分析","LR(0)分析"]
Menubar = Menu(root)             # 创建根菜单
root["menu"] = Menubar           # 第一层根菜单关联根窗体
File = Menu(Menubar,tearoff=False)             # 创建根菜单下的子菜单
Edit = Menu(Menubar,tearoff=False)
ProcessManage = Menu(Menubar,tearoff=False)
Memory = Menu(Menubar,tearoff=False)
EquipmentManage = Menu(Menubar,tearoff=False)
File.add_command(label = Button_File[0],accelerator='Crtl+O',command = Open)
File.add_command(label = Button_File[1],accelerator='Crtl+S',command = Save)
File.add_separator()#分割线
File.add_command(label = Button_File[2],accelerator='Crtl+X',command = Exit)
Edit.add_command(label = Button_Edit[0],command = Allow_Edit)
Edit.add_command(label = Button_Edit[1],command = Forbid_Edit)
ProcessManage.add_command(label = Button_ProcessManage[0],command = Lexical_Analysis)
ProcessManage.add_command(label = Button_ProcessManage[1],command = Automate)
ProcessManage.add_command(label = Button_ProcessManage[2],command = LL)
ProcessManage.add_command(label = Button_ProcessManage[3],command = LR)
Menubar.add_cascade(label = "文件(F)",menu=File)
Menubar.add_cascade(label = "编辑",menu=Edit)
Menubar.add_cascade(label = "编译",menu=ProcessManage)


# 菜单栏下的按钮
img1 = PhotoImage(file="open.png").subsample(9, 9) 
img2 = PhotoImage(file="save.png").subsample(9, 9)          # 按比例压缩
img3 = PhotoImage(file="exit.png").subsample(9, 9) 
frame = Frame(root,width=900)
FrameButton1=Button(frame,image = img1,text='打开',bd = 0,command = Open,compound="left")
FrameButton2=Button(frame,image = img2,text='保存',bd = 0,command = Save,compound="left")
FrameButton3=Button(frame,image = img3,text='退出',bd = 0,command = Exit,compound="left")
FrameButton4=Button(frame,text='| 允许编辑',bd = 0,command = Allow_Edit,compound="left")
FrameButton5=Button(frame,text=' 禁止编辑',bd = 0,command = Forbid_Edit,compound="left")
FrameButton6=Button(frame,text='| 词法分析',bd = 0,command = Lexical_Analysis,compound="left")
FrameButton7=Button(frame,text=' 自动机系统',bd = 0,command = Automate,compound="left")
FrameButton8=Button(frame,text=' LL(1)分析',bd = 0,command = LL,compound="left")
FrameButton9=Button(frame,text=' LR(0)分析',bd = 0,command = LR,compound="left")
FrameButton10=Button(frame,text='| 移除注释*',bd = 0,command = Remove_Comments,compound="left")

FrameButton1.grid(row=0, column=0,sticky = 'w')
FrameButton2.grid(row=0, column=1,sticky = 'w')
FrameButton3.grid(row=0, column=2,sticky = 'w')
FrameButton4.grid(row=0, column=3,sticky = 'w')
FrameButton5.grid(row=0, column=4,sticky = 'w')
FrameButton6.grid(row=0, column=5,sticky = 'w')
FrameButton7.grid(row=0, column=6,sticky = 'w')
FrameButton8.grid(row=0, column=7,sticky = 'w')
FrameButton9.grid(row=0, column=8,sticky = 'w')
FrameButton10.grid(row=0, column=9,sticky = 'w')
frame.pack(anchor=W)


# 显示区域
L1 = Label(root , text = "源程序" )
L2 = Label(root , text = "Token序列" )
L3 = Label(root , text = "词法错误" )

L1.place(x = 10,y = 25)
L2.place(x = 450,y = 25)
L3.place(x = 450,y = 305)

T1 = Text(root)
T2 = Text(root)
T3 = Text(root)
root.title("编译原理(允许编辑)")
T1.configure(state=NORMAL) 

T1.place(x = 10,y = 50,width=430,height=540)
T2.place(x = 450,y = 50,width=430,height=250)
T3.place(x = 450,y = 330,width=430,height=260)
root.mainloop()

