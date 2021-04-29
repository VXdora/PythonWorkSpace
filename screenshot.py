import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Screen Shot')
        self.geometry('500x300')
        self.config(bg='white')
        self.attributes('-transparentcolor', 'white')

if __name__ == '__main__':
    app = Application()
    app.mainloop()
