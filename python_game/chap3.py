#!/usr/bin/env python
#_*_coding:utf-8_*_
import tkinter
import sys
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import ttk

#ウィンドウの表示
root = tkinter.Tk()
root.title("リリーにしつもん")
root.minsize(640, 480)
root.option_add("*font", ["MS Pゴシック", 22])

#画像表示
canvas = tkinter.Canvas(bg="black", width=640, height=480)
canvas.place(x=0, y=0)
img = ImageTk.PhotoImage(file="img3/chap3-back.png")
canvas.create_image(320, 240, image=img)

#テキスト表示
question = tkinter.Label(text="知りたいのは何分かな？", bg="white")
question.place(x=100, y=40)

#テキストボックス表示
entry = tkinter.Entry(width=12, bd=4)
entry.place(x=50, y=133)

#質問ボタン表示
askbutton = tkinter.Button(text=u"聞く")
askbutton.pack()
askbutton.place(x=260, y=125)

#答えを表示
answer = tkinter.Label(text=".........", bg="white")
answer.place(x=115, y=235)

#イベント設定
def ask_click():
    val = entry.get()
    minutes = float(val)
    hours = round(minutes/60, 2)
    answer["text"] = str(hours) + "時間だね！"
askbutton["command"] = ask_click

#メインループ
root.mainloop()
