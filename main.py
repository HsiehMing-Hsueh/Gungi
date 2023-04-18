import tkinter as tk
from tkinter import ttk
from tkinter import Button,Frame
from tkinter.simpledialog import Dialog
from tkinter.simpledialog import askinteger,askstring
import Pmw

class Window(tk.Tk):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)

        #建立一個menu
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        #建立選項menu
        self.command_menu = tk.Menu(self.menubar)
        self.command_menu.add_command(label="開始",command=self.Game_Set)
        self.command_menu.add_command(label="離開", command=self.destroy)
        self.menubar.add_cascade(label="選項", menu=self.command_menu)
        
        one_frame = Frame(self,bg="#ffffff")
        Button(one_frame,text="9-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(one_frame,text="8-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(one_frame,text="7-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(one_frame,text="6-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(one_frame,text="5-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(one_frame,text="4-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(one_frame,text="3-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(one_frame,text="2-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(one_frame,text="1-1",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        one_frame.pack(expand=True,fill=tk.BOTH)

        two_frame = Frame(self,bg="#ffffff")
        Button(two_frame,text="9-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(two_frame,text="8-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(two_frame,text="7-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(two_frame,text="6-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(two_frame,text="5-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(two_frame,text="4-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(two_frame,text="3-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(two_frame,text="2-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(two_frame,text="1-2",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        two_frame.pack(expand=True,fill=tk.BOTH)

        three_frame = Frame(self,bg="#ffffff")
        Button(three_frame,text="9-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(three_frame,text="8-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(three_frame,text="7-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(three_frame,text="6-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(three_frame,text="5-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(three_frame,text="4-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(three_frame,text="3-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(three_frame,text="2-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(three_frame,text="1-3",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        three_frame.pack(expand=True,fill=tk.BOTH)

        four_frame = Frame(self,bg="#ffffff")
        Button(four_frame,text="9-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(four_frame,text="8-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(four_frame,text="7-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(four_frame,text="6-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(four_frame,text="5-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(four_frame,text="4-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(four_frame,text="3-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(four_frame,text="2-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(four_frame,text="1-4",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        four_frame.pack(expand=True,fill=tk.BOTH)

        five_frame = Frame(self,bg="#ffffff")
        Button(five_frame,text="9-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(five_frame,text="8-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(five_frame,text="7-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(five_frame,text="6-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(five_frame,text="5-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(five_frame,text="4-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(five_frame,text="3-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(five_frame,text="2-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(five_frame,text="1-5",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        five_frame.pack(expand=True,fill=tk.BOTH)

        six_frame = Frame(self,bg="#ffffff")
        Button(six_frame,text="9-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(six_frame,text="8-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(six_frame,text="7-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(six_frame,text="6-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(six_frame,text="5-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(six_frame,text="4-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(six_frame,text="3-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(six_frame,text="2-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(six_frame,text="1-6",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        six_frame.pack(expand=True,fill=tk.BOTH)

        seven_frame = Frame(self,bg="#ffffff")
        Button(seven_frame,text="9-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(seven_frame,text="8-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(seven_frame,text="7-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(seven_frame,text="6-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(seven_frame,text="5-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(seven_frame,text="4-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(seven_frame,text="3-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(seven_frame,text="2-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(seven_frame,text="1-7",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        seven_frame.pack(expand=True,fill=tk.BOTH)

        eight_frame = Frame(self,bg="#ffffff")
        Button(eight_frame,text="9-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(eight_frame,text="8-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(eight_frame,text="7-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(eight_frame,text="6-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(eight_frame,text="5-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(eight_frame,text="4-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(eight_frame,text="3-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(eight_frame,text="2-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(eight_frame,text="1-8",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        eight_frame.pack(expand=True,fill=tk.BOTH)

        nine_frame = Frame(self,bg="#ffffff")
        Button(nine_frame,text="9-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(nine_frame,text="8-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(nine_frame,text="7-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(nine_frame,text="6-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(nine_frame,text="5-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(nine_frame,text="4-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(nine_frame,text="3-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(nine_frame,text="2-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        Button(nine_frame,text="1-9",font=("Helvetica","24")).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        nine_frame.pack(expand=True,fill=tk.BOTH)

    def Game_Set(self):
        Pmw.initialise()
        dialog = Pmw.Dialog(self, buttons=('開始', 'Apply', '離開', '求助'),defaultbutton='開始', title='配置フェーズ(初始配置)')
        message_window = tk.Label(dialog.interior(), text='遊戲要開始了!',background='black', foreground='white', pady=20)
        message_window.pack(expand=1,fill=tk.X, padx=4, pady=4)
        dialog.activate()

def main():
    window = Window()
    window.title("這是軍儀")
    window.geometry("729x729")
    window.mainloop()

if __name__ =='__main__':
    main()