# -*- coding: utf-8 -*-
__author__ = '刘志奇'
"""
 Tkinter + PIL 图像转换器（PNG转换为JPG）
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="图像转换器", bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def getPNG():
    global image
    import_file_path = filedialog.askopenfilename()
    image = Image.open(import_file_path)


browse_png = tk.Button(text="选择PNG文件", command=getPNG, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browse_png)


def convert():
    global image
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    image.save(export_file_path)


saveasbutton = tk.Button(text="转换PNG成JPG", command=convert, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveasbutton)
root.mainloop()