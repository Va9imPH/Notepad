from tkinter.filedialog import *
from tkinter import *
import sys

root = Tk()
root.geometry("400x600")
root.title("Notepad")
root.config(bg = "white")
top = Frame(root)
top.pack(padx = 10, pady = 5, anchor = "nw")

def openFile():
    file = askopenfile(mode = "r", filetype = [("text files", "*.txt")])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

def saveFile():
    new_file = asksaveasfile(mode = "w", filetype=[("text files", ".txt")])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def clearFile():
    entry.delete(1.0, END)

def exit():
    sys.exit()

# fonts
f = "poppins"

# buttons
but1 = Button(root, font = f, text = "Open", bg="white", command = openFile)
but1.pack(in_ = top, side = LEFT)

but2 = Button(root, font = f, text = "Save", bg="white", command = saveFile)
but2.pack(in_ = top, side = LEFT)

but3 = Button(root, font = f, text = "Clear", bg="white", command = clearFile)
but3.pack(in_ = top, side = LEFT)

but4 = Button(root, font = f, text = "Exit", bg="white", command = exit)
but4.pack(in_ = top, side = LEFT)

# text area
entry = Text(root, bg = "#ffbf67", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand=True, fill = BOTH)

mainloop()