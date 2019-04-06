#!/usr/bin/env python
#_*_coding:utf-8_*_
import tkinter
import sys
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter import ttk

#ウィンドウ作成
root = tkinter.Tk()
root.title("勇者求む！")
root.minsize(640, 480)
root.option_add("*font", ["メイリオ", 14])

#画像の読込み
img1 = ImageTk.PhotoImage(Image.open('img4/chap4-1-1.png').convert('RGB'))
img2 = ImageTk.PhotoImage(Image.open('img4/chap4-1-2.png').convert('RGB'))
img3 = ImageTk.PhotoImage(Image.open('img4/chap4-1-3.png').convert('RGB'))

#キャンパス作成
canvas = tkinter.Canvas(root, width=640, height=480)
canvas.place(x=0, y=0)
canvas.create_image(320, 220, image=img1, tag="illust")

#ラベル配置
serihu_text = tkinter.Label(text= \
    "王様「魔王を倒したら褒美をやるぞ！」")
serihu_text.place(x=160, y=10)
sys_text = tkinter.Label(text="褒美はいくらあげますか？", fg="red")
sys_text.place(x=180, y=380)

#入力ボックス配置
entry = tkinter.Entry(width=12)
entry.place(x=180, y=420)
gold_text = tkinter.Label(text="ゴールド")
gold_text.place(x=330, y=420)

#ボタン配置
button = tkinter.Button(text=u"決定")
button.place(x=420, y=420)

root.mainloop()
