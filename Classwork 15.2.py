import tkinter

root = tkinter.Tk()
root.resizable(False, False)

#create canvas
myCanvas = tkinter.Canvas(root, bg="black", height=500, width=800)

shape1 = myCanvas.create_oval(10,10,200,200, outline="blue", fill="red")

shape2 = myCanvas.create_rectangle(750,450,100,300, outline="violet", fill="blue")

myCanvas.pack()
root.mainloop()