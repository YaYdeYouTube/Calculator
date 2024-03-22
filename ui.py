from tkinter import *

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Erreur")
    elif text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, text)

root = Tk()
root.geometry("400x400+250+50")
root.title("Calculatrice")

numbers = [
    ("0", ".", "C", "+"),
    ("1", "2", "3", "-"),
    ("4", "5", "6", "*"),
    ("7", "8", "9", "/"),
    ("=")
]

entry = Entry(root, bd=10, font=("MV BOLI", 15), relief=SUNKEN, justify=RIGHT)
entry.pack(fill=X, padx=5, pady=10)
for row in numbers:
    width = 300
    height = 300
    frame = Frame(root, width=width, height=height, bg="Black")
    frame.pack()
    for button_text in row:
        button = Button(frame, text=button_text, bg="Gray", fg="White", font=("MV BOLI", 10), width=5, height=2)
        button.pack(side=LEFT, padx=5, pady=5)
        button.bind("<Button-1>", on_click)
try:
    pass
except ValueError:
    pass

root.mainloop()