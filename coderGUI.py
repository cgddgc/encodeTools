#!python3
#coding=utf-8
import tkinter
from tkinter import ttk
import myCoder

#win.geometry('600x500')

class Gui:
    def __init__(self):
        self.coder=myCoder.coder()
        self.li=self.coder.func_list
        self.win=tkinter.Tk()
        self.win.title('coderForCoders')
        #self.display()

    def transfer(self,s,f):
        return eval('self.coder.'+f)(s)

    def code(self,c):
        if c=='down':
            s=self.text1.get(0.0,'end')
            func=self.r.get()
            res=self.transfer(s,func)
            self.text2.delete(0.0,tkinter.END)
            self.text2.insert(tkinter.INSERT,res)
        else:
            s=self.text2.get(0.0,'end')
            func=self.r.get()
            res=self.transfer(s,func)
            self.text1.delete(0.0,tkinter.END)
            self.text1.insert(tkinter.INSERT,res)

    def display(self):
        frm1=tkinter.Frame(self.win,width=10)
        frm1.pack(side='left',anchor='nw',padx=5)

        frm2=tkinter.Frame(self.win)
        frm2.pack(side='left',anchor='w',pady=5)

        self.r=tkinter.StringVar()
        self.r.set('b64enc')
        for i in range(len(self.li)):
            tkinter.Radiobutton(self.win,text=self.li[i][0],value=self.li[i][1],variable=self.r).pack(anchor='nw',side='top',in_=frm1,pady=3)

        #print(li[1][0])

        frmt1=tkinter.Frame(self.win,width=30)
        frmt1.pack(side='top',anchor='center',in_=frm2,padx=5)

        self.text1=tkinter.Text(self.win,font=("Arial", 12),height=10,width=50)
        self.text1.pack(side='left',anchor='center',in_=frmt1)

        sc1=tkinter.Scrollbar()
        sc1.pack(side=tkinter.RIGHT, fill=tkinter.Y,in_=frmt1)
        sc1.config(command=self.text1.yview)

        frm3=tkinter.Frame(self.win)
        frm3.pack(side='top',anchor='n',pady=5,in_=frm2)

        tkinter.Button(self.win,text='转换↓',command=lambda:self.code('down')).pack(in_=frm3,side='left',padx=5)
        tkinter.Button(self.win,text='转换↑',command=lambda:self.code('up')).pack(in_=frm3,side='left',padx=5)

        frmt2=tkinter.Frame(self.win,width=30)
        frmt2.pack(side='top',in_=frm2,padx=5)

        self.text2=tkinter.Text(self.win,font=("Arial", 12),height=10,width=50)
        self.text2.pack(side='left',anchor='center',in_=frmt2)
        sc2=tkinter.Scrollbar()
        sc2.pack(side=tkinter.RIGHT, fill=tkinter.Y,in_=frmt2)
        sc2.config(command=self.text2.yview)

        self.win.mainloop()


app=Gui()
app.display()