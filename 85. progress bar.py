from tkinter import *
from tkinter.ttk import *
import time


# def start():
#     tasks = 10
#     x = 0
#     while x < tasks:
#         time.sleep(0.2)
#         bar['value'] += 10
#         x += 1
#         percent.set(str(int(x/tasks * 100)) + "%")
#         text.set(str(x) + "/" + str(tasks) + " tasks completed")
#         root.update_idletasks()


def start():
    gb = 100
    download = 0
    speed = 1
    while download < gb:
        time.sleep(0.05)
        bar['value'] += speed/gb * 100
        download += speed
        percent.set(str(int(download/gb * 100)) + "%")
        text.set(str(download) + "/" + str(gb) + " GB downloaded")
        root.update_idletasks()


root = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(root, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(root, textvariable=percent).pack()
taskLabel = Label(root, textvariable=text).pack()

button = Button(root, text="download", command=start).pack()

root.mainloop()
