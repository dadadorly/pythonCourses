import tkinter

window = tkinter.Tk()

window.title('GUI')

label = tkinter.Label(text="HelloWorld!",
                      foreground="white",
                      background="black",
                      width=50,
                      height=10)
label.pack()

entry = tkinter.Entry(fg="black", bg="white", width=60)
entry.insert(0, "Write here !")
entry.pack()


def press():
    label.config(text=entry.get())


def add():
    tab = entry.get().split('+')
    a = tab[0]
    b = tab[1]
    result = int(a) + int(b)
    label.config(text=result)


button = tkinter.Button(
    text="Change text",
    width=20,
    bg="blue",
    fg="yellow",
    command=press
)
button2 = tkinter.Button(
    text="addition (1+1)",
    width=20,
    bg="yellow",
    fg="blue",
    command=add
)
button.pack()
button2.pack()


window.mainloop()
