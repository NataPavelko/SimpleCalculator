
import tkinter as tk
from tkinter import *
from tkinter import font

root=tk.Tk()

root.title("My Titel")
root.geometry("400x400")
root.resizable(width=False, height=False)
root.minsize(width=400, height=500)
fontgeneral=font.Font(size=30,family="Arial")

eingabe= tk.Entry(root, font=fontgeneral,borderwidth=20)
eingabe.grid(row=0,column=0, columnspan=5, sticky="nswe", padx=10)

def set_text(text):
    eingabe.insert(tk.END,text)

def clear_entry():
   eingabe.delete(eingabe.index("end")-1)

def clear_everything():
    eingabe.delete(0,tk.END)


def show_result():
       result = eval(eingabe.get())
       eingabe.delete(0,tk.END)
       eingabe.insert(0,str(result))


def result():
    string=eingabe.get()
    res=eval(string)
    return res

button1 = tk.Button(root, text ="1", command=lambda:set_text("1")).grid(column=0, row=3, sticky="nswe")
button2 = tk.Button(root, text ="2", command=lambda:set_text("2")).grid(column=1, row=3, sticky="nswe")
button3 = tk.Button(root, text ="3", command=lambda:set_text("3")).grid(column=2, row=3, sticky="nswe")
button4 = tk.Button(root, text ="4", command=lambda:set_text("4")).grid(column=0, row=2, sticky="nswe")
button5 = tk.Button(root, text ="5", command=lambda:set_text("5")).grid(column=1, row=2, sticky="nswe")
button6 = tk.Button(root, text ="6", command=lambda:set_text("6")).grid(column=2, row=2, sticky="nswe")
button7 = tk.Button(root, text ="7", command=lambda:set_text("7")).grid(column=0, row=1, sticky="nswe")
button8 = tk.Button(root, text ="8", command=lambda:set_text("8")).grid(column=1, row=1, sticky="nswe")
button9 = tk.Button(root, text ="9", command=lambda:set_text("9")).grid(column=2, row=1, sticky="nswe")

button0 = tk.Button(root, text ="0", command=lambda:set_text("0")).grid(column=0, row=4, sticky="nswe")
buttonpunkt = tk.Button(root, text =".", command=lambda:set_text(".")).grid(column=1, row=4, sticky="nswe")

buttonkl1 = tk.Button(root, text ="(", bg='#bfbfbf', command=lambda:set_text("(")).grid(column=3, row=1, sticky="nswe")
buttonkl2 = tk.Button(root, text =")", bg='#bfbfbf', command=lambda:set_text(")")).grid(column=4, row=1, sticky="nswe")
buttonplus = tk.Button(root, text ="+", bg='#bfbfbf', width="1", command=lambda:set_text("+")).grid(column=3, row=3, sticky="nswe")
buttonminus = tk.Button(root, text ="-", bg='#bfbfbf', width="1", command=lambda:set_text("-")).grid(column=4, row=3, sticky="nswe")
buttonmal = tk.Button(root, text ="*", bg='#bfbfbf', command=lambda:set_text("*")).grid(column=3, row=2, sticky="nswe")
buttonteil = tk.Button(root, text ="/", bg='#bfbfbf', command=lambda:set_text("/")).grid(column=4, row=2, sticky="nswe")
buttongleich = tk.Button(root, text ="=", bg='#70db70', command=show_result).grid(column=3, row=4, columnspan=2, sticky="nswe")
buttondelete = tk.Button(root, text ="DEL", command=clear_entry).grid(column=2, row=4, columnspan=1, sticky="nswe")
buttondelete = tk.Button(root, text ="DELETE EVERYTHING", command=clear_everything,  bg='#ffb3b3',).grid(column=0, row=5, columnspan=5, sticky="nswe")


for column in range(5):
    root.columnconfigure(column, weight=1)
for row in range(6):
   root.rowconfigure(row,weight=2)


root.mainloop()