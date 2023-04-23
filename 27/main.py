import tkinter

def button_click():
    print(input.get())


window = tkinter.Tk()

window.title("Neural Network")
window.geometry("500x500")
# frame = tkinter.Frame(window, width=500, height=500)
# frame.grid()
label1 = tkinter.Label(window, text="Welcome to my neural network app!", font="Century 20 bold")
label1.pack()
input = tkinter.Entry(window, width=200, font="Century 20 bold")
input.pack()
print(input.get())

button1 = tkinter.Button(window, text="Detect language", font="Century 20 bold", command=button_click)
button1.pack()

button3 = tkinter.Button(window, text="Quit", font="Century 20 bold", command=window.destroy)
button3.pack()

window.mainloop()
