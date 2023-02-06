import tkinter as tk
from tkinter import *


'''
MESSAGE_BOXES V.1.0.0
CURRENTLY IN DEVELOPMENT
CURRENTLY IN BETA TESTING
'''


class MessageBox(object):
    #use tkinter to create a window with a label and a button, that returns the text of the button pressed

    def __init__(self, text, title, button_options, Wbg="white", Lbg="white", Lfg="black", justify=LEFT, font="consolas", btnfont="consolas"):
        self.value = None
        self.root = None
        self.text = text
        self.title = title
        self.button_options = button_options
        self.Wbg = Wbg
        self.Lbg = Lbg
        self.Lfg = Lfg
        self.justify = justify
        self.font = font
        self.btnfont = btnfont

    def center(self):
        self.root.update_idletasks()
        width, height = (self.root.winfo_width(), self.root.winfo_height())
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def message(self):
        self.root = tk.Tk()
        self.root['background'] = self.Wbg
        self.root.attributes("-topmost", True)
        self.root.after(1, lambda: self.root.focus_force())
        self.root.title(self.title)
        Label(self.root, text=self.text, justify=self.justify, bg=self.Lbg, fg=self.Lfg, font=self.font).pack(padx=25, pady=10)
        tk.Button(self.root, text = self.button_options, font=self.btnfont, command = self.finish).pack(side=LEFT, padx=25, pady=10)
        self.root.bind("<Return>", lambda event: self.finish())
        tk.Button(self.root, text = "Cancel", font=self.btnfont, command = self.root.destroy).pack(side=RIGHT, padx=25, pady=10)
        self.center()
        self.root.mainloop()
        return self.value

    def finish(self):
        self.value = self.button_options
        self.root.destroy()

class ButtonBox(object):
    '''
    A message box that returns the text of the button pressed. Can have as many buttons as you want, as long as there is at least one. 
    
    '''
    def __init__(self, text, title, button_options, Wbg="white", Lbg="white", Lfg="black", font="consolas", btnfont="consolas"):
        self.value = None
        self.root = None
        self.button_options = button_options
        self.text = text
        self.title = title
        self.Wbg = Wbg
        self.Lbg = Lbg
        self.Lfg = Lfg
        self.font = font
        self.btnfont = btnfont
    def center(self):
        self.root.update_idletasks()
        width, height = (self.root.winfo_width(), self.root.winfo_height())
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    def options(self):
        self.root = tk.Tk()
        self.root['background'] = self.Wbg
        self.root.attributes("-topmost", True)
        self.root.focus_force() # just in case
        self.root.title(self.title)
        Label(self.root, text=self.text, justify=CENTER, bg=self.Lbg, fg=self.Lfg, font=self.font).grid(columnspan=len(self.button_options), padx=25, pady=10)
        if type(self.button_options) == str:
            self.button_options = [self.button_options]
        if type(self.button_options) == list or tuple:
                for index, text in enumerate(self.button_options):
                    if index < 10:
                        tk.Button(self.root, text = f"{index + 1}: {text}", font=self.btnfont, command = lambda index = index: self.finish(self.button_options[index])).grid(row=3, column=index, padx=25, pady=10)
                        self.root.bind(str(index + 1), lambda event, index = index: self.finish(self.button_options[index]))
                        tk.Button(self.root, text = "Cancel", font=self.btnfont, command = self.root.destroy).grid(row=4, columnspan=len(self.button_options), padx=25, pady=10)
                        self.root.bind("<Escape>", lambda event: self.root.destroy())
                        

                    
        self.center()
        self.root.mainloop()
        return self.value

    def finish(self, value):
        self.value = value
        self.root.destroy()

class InputBox(object):
    '''
    A message box that returns the text of the entry.
    
    '''
    def __init__(self, text, title = '', show = None, Wbg="white", Lbg="white", Ebg="white", Lfg="black", font="consolas", entfont="consolas", btnfont="consolas"):
        self.value = None
        self.root = None
        self.text = text
        self.title = title
        self.show = show
        self.result = None
        self.Lbg = Lbg
        self.Wbg = Wbg
        self.Ebg = Ebg
        self.Lfg = Lfg
        self.font = font
        self.entfont = entfont
        self.btnfont = btnfont

    def center(self):
        self.root.update_idletasks()
        width, height = (self.root.winfo_width(), self.root.winfo_height())
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def return_entry(self):
        self.result = self.entry.get()
        self.root.destroy()

    def input(self):
        self.root = tk.Tk()
        self.root['background'] = self.Wbg
        self.root.attributes("-topmost", True)
        self.root.focus_force() # just in case
        self.root.title(self.title)
        Label(self.root, text=self.text, bg=self.Lbg, fg=self.Lfg, font=self.font).grid(columnspan = 2)
        self.entry = Entry(self.root, show=self.show, bg=self.Ebg, font=self.entfont)
        self.entry.focus_set()
        self.entry.grid(columnspan = 2)
        self.ok_button = Button(self.root, text = "OK", font=self.btnfont, command = self.return_entry)
        self.ok_button.grid(row=3, column=0, padx=25, pady=10)
        Button(self.root, text = "Cancel", font=self.btnfont, command = lambda: self.root.destroy()).grid(row=3, column=1, padx=25, pady=10)
        self.center()
        self.root.bind("<Return>", lambda e = None: self.return_entry())
        self.root.bind("<Escape>", lambda e = None: self.root.destroy())
        self.root.mainloop()

class DoubleInputBox(object):
    '''
    A message box that allows for two seperate text entries, with two different labels. Wil return ("text_input1", "text_input2").
    
    '''
    def __init__(self, text1, text2, title = None, show1 = None, show2 = None, Wbg="white", Lbg1="white", Lfg1="black", Lbg2="white", Lfg2="black", Ebg1="white", Ebg2="white", font1="consolas", font2="consolas", entfont1="consolas", entfont2="consolas", btnfont="consolas"):
        self.value = None
        self.root = None
        self.text1 = text1
        self.text2 = text2
        self.title = title
        self.show1 = show1
        self.show2 = show2
        self.result = None
        self.Lbg1 = Lbg1
        self.Lbg2 = Lbg2
        self.Wbg = Wbg
        self.Ebg1 = Ebg1
        self.Ebg2 = Ebg2
        self.Lfg1 = Lfg1
        self.Lfg2 = Lfg2
        self.font1 = font1
        self.font2 = font2
        self.btnfont = btnfont
        self.entfont1 = entfont1
        self.entfont2 = entfont2

    def center(self):
        self.root.update_idletasks()
        width, height = (self.root.winfo_width(), self.root.winfo_height())
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2) - 50 # 50 is for the awkwardness of the taskbar
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def return_entry(self):
        self.result = self.entry1.get()
        self.result2 = self.entry2.get()
        self.root.destroy()

    def input(self):
        self.root = tk.Tk()
        self.root['background'] = self.Wbg
        self.root.attributes("-topmost", True)
        self.root.focus_force() # just in case
        self.root.title(self.title)
        Label(self.root, text=self.text1, bg=self.Lbg1, fg=self.Lfg1, font=self.font1).grid(columnspan = 2)
        self.entry1 = Entry(self.root, show=self.show1, bg=self.Ebg1, font=self.entfont1)
        self.entry1.focus_set()
        self.entry1.grid(columnspan = 2)
        Label(self.root, text=self.text2, bg=self.Lbg2, fg=self.Lfg2, font=self.font2).grid(columnspan = 2)
        self.entry2 = Entry(self.root, show=self.show2, bg=self.Ebg2, font=self.entfont2)
        self.entry2.grid(columnspan = 2)
        self.ok_button = Button(self.root, text = "OK", font=self.btnfont, command = self.return_entry)
        self.ok_button.grid(row=4, column=0, padx=25, pady=10)
        Button(self.root, text = "Cancel", font=self.btnfont, command = lambda: self.root.destroy()).grid(row=4, column=1, padx=25, pady=10)
        self.center()
        self.root.bind("<Return>", lambda e = None: self.return_entry())
        self.root.bind("<Escape>", lambda e = None: self.root.destroy())
        self.root.mainloop()


def message(text=None, title=None, button_options="Ok", Wbg="white", Lbg="white", Lfg="black"):
    # text: the text to be displayed, title: the title of the window, button_options: the text displayed on the buttons, 
    # Wbg: the background color of the window (name of color or HEX), Lbg: the background color of the text (name of color or HEX),
    # Lfg: the foreground color of the text (name of color or HEX)
    msg = MessageBox(text=text, title=title, button_options=button_options, Wbg=Wbg, Lbg=Lbg, Lfg=Lfg).message()
    return msg

def buttons(text=None, title=None, button_options=["Ok"], Wbg="white", Lbg="white", Lfg="black"):
    # text: the text to be displayed, title: the title of the window, button_options: the text displayed on the buttons, 
    # Wbg: the background color of the window (name of color or HEX), Lbg: the background color of the text (name of color or HEX),
    # Lfg: the foreground color of the text (name of color or HEX)
    bttn = ButtonBox(text=text, title=title, button_options=button_options, Wbg=Wbg, Lbg=Lbg, Lfg=Lfg).options()
    return bttn

def input(text=None, title=None, show=None, Wbg="white", Lbg="white", Ebg="white", Lfg="black"):
    # text: the text to be displayed, title: the title of the window, show: what other character the text should be displayed 
    # as(*, #, etc), Wbg: the background color of the window (name of color or HEX), Lbg: the background color of the text 
    # (name of color or HEX),Lfg: the foreground color of the text (name of color or HEX)
    box = InputBox(text=text, title=title, show=show, Wbg=Wbg, Lbg=Lbg, Lfg=Lfg)
    box.input()
    return box.result

def double_input(text1=None, text2=None, title=None, show1=None, show2="*", Wbg="white", Lbg1="white", Lfg1="black", Lbg2="white", Lfg2="black", Ebg1="white", Ebg2="white"):
    # text: the text to be displayed, title: the title of the window, show: what other character the text should be displayed 
    # as(*, #, etc), Wbg: the background color of the window (name of color or HEX), Lbg: the background color of the text 
    # (name of color or HEX),Lfg: the foreground color of the text (name of color or HEX)
    box = DoubleInputBox(text1=text1, text2=text2, title=title, show1=show1, show2=show2, Wbg=Wbg, Lbg1=Lbg1, Lfg1=Lfg1, Lbg2=Lbg2, Lfg2=Lfg2, Ebg1=Ebg1, Ebg2=Ebg2)
    box.input()
    try:
        final_result = box.result + " " + box.result2
    except TypeError as e:
        print(e)
        final_result = None
    return final_result