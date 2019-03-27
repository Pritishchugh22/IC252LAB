#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 22:22:02 2019

@author: tushar
"""

import tkinter as tk

#from pytube import YouTube
#def downloadVid():
#    global E1
#    string =E1.get()
#    yt = YouTube(str(string))
#    videos = yt.get_videos()
#    s=1
#    for v in videos:
#        print(str(s) + '.' + str(v))
#        s +=1
#    n=int(input("Enter your choice"))
#    vid=videos[n-1]
#    destination=str(input("Enter your destination"))
#    vid.download(destination)
#    print(yt.filename+"\n Ha been downloaded")
#root=tk.Tk()
#
#w=tk.Label(root,text="Youtube Downloader")
#w.pack()
#
#
#E1=tk.Entry(root,bd=5)
#E1.pack(side=tk.TOP)
#
#
#button=tk.Button(root,text="Download",fg="red",command=downloadVid   )
#button.pack(side=tk.BOTTOM)
#
#root.mainloop()

from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=bmyv0nRkDmc")
print(yt.title)
stream = yt.streams.first()
stream.download()
