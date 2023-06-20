import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, height=50, bg="red")
frame1.pack(fill=tk.BOTH, expand=True)

frame2 = tk.Frame(master=window, height=50, bg="orange")
frame2.pack(fill=tk.BOTH, expand=True)

frame3 = tk.Frame(master=window, height=50, bg="yellow")
frame3.pack(fill=tk.BOTH, expand=True)

frame4 = tk.Frame(master=window, height=50, bg="green")
frame4.pack(fill=tk.BOTH, expand=True)

frame5 = tk.Frame(master=window, height=50, bg="blue")
frame5.pack(fill=tk.BOTH, expand=True)

frame6 = tk.Frame(master=window, height=50, bg="indigo")
frame6.pack(fill=tk.BOTH, expand=True)

frame7 = tk.Frame(master=window, height=50, bg="violet")
frame7.pack(fill=tk.BOTH, expand=True)

window.mainloop()