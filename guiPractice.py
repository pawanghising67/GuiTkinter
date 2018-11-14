import tkinter  #importing tkinter
from tkinter import ttk
import webbrowser

def facebook(event):
    print("Redirecting to facebook...")
    webbrowser.open_new_tab("http://facebook.com")

def ebay(event):
    print("Redirecting to Ebay.....")
    webbrowser.open_new_tab("http://ebay.com")

root = tkinter.Tk() #objectifying tkinter into root var

alabel = ttk.Label(text= "Pawan's Blog")
alabel.grid(column =4 , row = 4)

button = ttk.Button(text= "Facebook")
button.grid(column =2, row = 4)
button.bind("<Button>",facebook)

button1 = ttk.Button(root,text = "Ebay!")
button1.grid(column =2, row =10)
button1.bind("<Button-1>", ebay)


root.mainloop() #calling mainloop method from tkinter class for GUI