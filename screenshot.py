import tkinter as tk

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


if __name__ == '__main__':
    root = tk.Tk()

    root.geometry('100x100')
    root.config(bg='white')
    root.attributes('-transparentcolor', 'white')

    root.bind('<Motion>', motion)
    root.mainloop()
