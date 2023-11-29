import tkinter as tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename
root=tk.Tk()
root.title("Text Editor")
# root.geometry('120*360')

def o_open():
    filepath=askopenfilenames(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    write.delete(1.0,tk.END)
    with open(filepath,"r")as input_f:
        text=input_f.read()
        write.insert(tk.END,text)
    root.title(f"Text Editor - {filepath}")

def s_save():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt"),("All Files")])
    if not filepath:
        return
    with open(filepath, "w")as output_f:
        text=write.get(1.0,tk.END)
        output_f.write(text)
    root.title(f"Text Editor - {filepath}")






write=tk.Text(root)
write.grid(row=0,column=1,sticky='nsew')
row=tk.Frame(root,bd=2,relief=tk.RAISED)
row.grid(row=0,column=0,sticky='ns')
open_btn=tk.Button(row,text='OPEN',command=o_open)
open_btn.grid(row=0,column=0,padx=5,pady=5)
save=tk.Button(row,text='Save as',command=s_save)
save.grid(row=1,column=0,padx=5,pady=5)



root.mainloop()