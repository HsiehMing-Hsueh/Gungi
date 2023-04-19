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
        button1 = tk.Button(one_frame,text="9-1",font=("Helvetica","24"),command=self.Click_Start)
        button1.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button2 = tk.Button(one_frame,text="8-1",font=("Helvetica","24"),command=self.Click_Start)
        button2.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button3 = tk.Button(one_frame,text="7-1",font=("Helvetica","24"),command=self.Click_Start)
        button3.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button4 = tk.Button(one_frame,text="6-1",font=("Helvetica","24"),command=self.Click_Start)
        button4.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button5 = tk.Button(one_frame,text="5-1",font=("Helvetica","24"),command=self.Click_Start)
        button5.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button6 = tk.Button(one_frame,text="4-1",font=("Helvetica","24"),command=self.Click_Start)
        button6.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button7 = tk.Button(one_frame,text="3-1",font=("Helvetica","24"),command=self.Click_Start)
        button7.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button8 = tk.Button(one_frame,text="2-1",font=("Helvetica","24"),command=self.Click_Start)
        button8.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button9 = tk.Button(one_frame,text="1-1",font=("Helvetica","24"),command=self.Click_Start)
        button9.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        one_frame.pack(expand=True,fill=tk.BOTH)

        two_frame = Frame(self,bg="#ffffff")
        button10 = tk.Button(two_frame,text="9-2",font=("Helvetica","24"),command=self.Click_Start)
        button10.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button11 = tk.Button(two_frame,text="8-2",font=("Helvetica","24"),command=self.Click_Start)
        button11.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button12 = tk.Button(two_frame,text="7-2",font=("Helvetica","24"),command=self.Click_Start)
        button12.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button13 = tk.Button(two_frame,text="6-2",font=("Helvetica","24"),command=self.Click_Start)
        button13.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button14 = tk.Button(two_frame,text="5-2",font=("Helvetica","24"),command=self.Click_Start)
        button14.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button15 = tk.Button(two_frame,text="4-2",font=("Helvetica","24"),command=self.Click_Start)
        button15.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button16 = tk.Button(two_frame,text="3-2",font=("Helvetica","24"),command=self.Click_Start)
        button16.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button17 = tk.Button(two_frame,text="2-2",font=("Helvetica","24"),command=self.Click_Start)
        button17.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button18 = tk.Button(two_frame,text="1-2",font=("Helvetica","24"),command=self.Click_Start)
        button18.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        two_frame.pack(expand=True,fill=tk.BOTH)

        three_frame = Frame(self,bg="#ffffff")
        button19 = tk.Button(three_frame,text="9-3",font=("Helvetica","24"),command=self.Click_Start)
        button19.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button20 = tk.Button(three_frame,text="8-3",font=("Helvetica","24"),command=self.Click_Start)
        button20.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button21 = tk.Button(three_frame,text="7-3",font=("Helvetica","24"),command=self.Click_Start)
        button21.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button22 = tk.Button(three_frame,text="6-3",font=("Helvetica","24"),command=self.Click_Start)
        button22.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button23 = tk.Button(three_frame,text="5-3",font=("Helvetica","24"),command=self.Click_Start)
        button23.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button24 = tk.Button(three_frame,text="4-3",font=("Helvetica","24"),command=self.Click_Start)
        button24.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button25 = tk.Button(three_frame,text="3-3",font=("Helvetica","24"),command=self.Click_Start)
        button25.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button26 = tk.Button(three_frame,text="2-3",font=("Helvetica","24"),command=self.Click_Start)
        button26.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button27 = tk.Button(three_frame,text="1-3",font=("Helvetica","24"),command=self.Click_Start)
        button27.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        three_frame.pack(expand=True,fill=tk.BOTH)

        four_frame = Frame(self,bg="#ffffff")
        button28 = tk.Button(four_frame,text="9-4",font=("Helvetica","24"),command=self.Click_Start)
        button28.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button29 = tk.Button(four_frame,text="8-4",font=("Helvetica","24"),command=self.Click_Start)
        button29.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button30 = tk.Button(four_frame,text="7-4",font=("Helvetica","24"),command=self.Click_Start)
        button30.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button31 = tk.Button(four_frame,text="6-4",font=("Helvetica","24"),command=self.Click_Start)
        button31.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button32 = tk.Button(four_frame,text="5-4",font=("Helvetica","24"),command=self.Click_Start)
        button32.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button33 = tk.Button(four_frame,text="4-4",font=("Helvetica","24"),command=self.Click_Start)
        button33.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button34 = tk.Button(four_frame,text="3-4",font=("Helvetica","24"),command=self.Click_Start)
        button34.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button35 = tk.Button(four_frame,text="2-4",font=("Helvetica","24"),command=self.Click_Start)
        button35.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button36 = tk.Button(four_frame,text="1-4",font=("Helvetica","24"),command=self.Click_Start)
        button36.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        four_frame.pack(expand=True,fill=tk.BOTH)

        five_frame = Frame(self,bg="#ffffff")
        button37 = tk.Button(five_frame,text="9-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button38 = tk.Button(five_frame,text="8-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button39 = tk.Button(five_frame,text="7-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button40 = tk.Button(five_frame,text="6-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button41 = tk.Button(five_frame,text="5-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button42 = tk.Button(five_frame,text="4-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button43 = tk.Button(five_frame,text="3-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button44 = tk.Button(five_frame,text="2-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button45 = tk.Button(five_frame,text="1-5",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        five_frame.pack(expand=True,fill=tk.BOTH)

        six_frame = Frame(self,bg="#ffffff")
        button46 = tk.Button(six_frame,text="9-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button47 = tk.Button(six_frame,text="8-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button48 = tk.Button(six_frame,text="7-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button49 = tk.Button(six_frame,text="6-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button50 = tk.Button(six_frame,text="5-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button51 = tk.Button(six_frame,text="4-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button52 = tk.Button(six_frame,text="3-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button53 = tk.Button(six_frame,text="2-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button54 = tk.Button(six_frame,text="1-6",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        six_frame.pack(expand=True,fill=tk.BOTH)

        seven_frame = Frame(self,bg="#ffffff")
        button55 = tk.Button(seven_frame,text="9-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button56 = tk.Button(seven_frame,text="8-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button57 = tk.Button(seven_frame,text="7-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button58 = tk.Button(seven_frame,text="6-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button59 = tk.Button(seven_frame,text="5-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button60 = tk.Button(seven_frame,text="4-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button61 = tk.Button(seven_frame,text="3-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button62 = tk.Button(seven_frame,text="2-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button63 = tk.Button(seven_frame,text="1-7",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        seven_frame.pack(expand=True,fill=tk.BOTH)

        eight_frame = Frame(self,bg="#ffffff")
        button64 = tk.Button(eight_frame,text="9-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button65 = tk.Button(eight_frame,text="8-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button66 = tk.Button(eight_frame,text="7-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button67 = tk.Button(eight_frame,text="6-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button68 = tk.Button(eight_frame,text="5-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button69 = tk.Button(eight_frame,text="4-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button70 = tk.Button(eight_frame,text="3-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button71 = tk.Button(eight_frame,text="2-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button72 = tk.Button(eight_frame,text="1-8",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        eight_frame.pack(expand=True,fill=tk.BOTH)

        nine_frame = Frame(self,bg="#ffffff")
        button73 = tk.Button(nine_frame,text="9-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button74 = tk.Button(nine_frame,text="8-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button75 = tk.Button(nine_frame,text="7-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button76 = tk.Button(nine_frame,text="6-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button77 = tk.Button(nine_frame,text="5-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button78 = tk.Button(nine_frame,text="4-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button79 = tk.Button(nine_frame,text="3-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button80 = tk.Button(nine_frame,text="2-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        button81 = tk.Button(nine_frame,text="1-9",font=("Helvetica","24"),command=self.Click_Start).pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        nine_frame.pack(expand=True,fill=tk.BOTH)

    def Game_Set(self):
        Pmw.initialise()
        dialog = Pmw.Dialog(self, buttons=('開始', 'Apply', '離開', '求助'),defaultbutton='開始', title='配置フェーズ(初始配置)')
        message_window = tk.Label(dialog.interior(), text='遊戲要開始了!',background='black', foreground='white', pady=20)
        message_window.pack(expand=1,fill=tk.X, padx=4, pady=4)
        dialog.activate()

    def Click_Start(self):
        pass
def main():
    window = Window()
    window.title("這是軍儀")
    window.geometry("729x729")
    window.mainloop()

if __name__ =='__main__':
    main()