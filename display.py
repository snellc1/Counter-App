import tkinter

maindisplay = tkinter.Tk()

maindisplay.title("Counter")
maindisplay.geometry("250x250")
count = 0

number_label = tkinter.Label(maindisplay, text=count, font=("Arial", 40, "bold"))
number_label.pack(pady=10)


counter_button = tkinter.Button(maindisplay, text="Count", font=("Arial", 20, "bold"))
counter_button.pack(pady=10)


maindisplay.mainloop()