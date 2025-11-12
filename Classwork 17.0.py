import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        self.element.append(input("Enter what you would like to add: "))

    def dequeue(self):
        self.element.remove(0)

    def display_queue(self):
        print("Elements in Queue: ")
        for i in self.element:
            print(i)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Create Class Object with Button")
        self.geometry("300x200")

        # Label and Entry for name input
        tk.Label(self, text="Enter input: ").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        # Button to create object
        tk.Button(self, text="Create Queue", command=self.create_queue).pack(pady=10)

        # Label to display result
        self.result_label = tk.Label(self, text="", fg="blue")
        self.result_label.pack(pady=10)

    def create_queue(self):
        """Create a Person object when button is clicked."""
        input = self.name_entry.get().strip()

        # Input validation
        if not input:
            messagebox.showerror("Error", "Input cannot be empty!")
            return

        # Create the object
        queue = Queue[input]

        # Display greeting from the object
        self.result_label.config(text=queue.greet())

    # Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()


#Main Code
q1 = Queue()
q2 = Queue()

#top = Tk()
#top.geometry("500x500")

#answer = Text(width=35, height=2)
#answer.place(x=100, y=0)

#def show(n):
#    try:
#        answer.insert(tk.INSERT, n)
#    except:
#        answer.delete(1.0, "end-1c")

#B1 = Button(top, text="Create Queue", width=10, height=5, command=)
#B1.place(x=100, y=100)

#B3 = Button(top, text="Enqueue", width=10, height=5, command='equeue')
#B3.place(x=200, y=100)

#B4 = Button(top, text="Dequeue", width=10, height=5, command=lambda: show("Dequeue"))
#B4.place(x=100, y=200)

#B6 = Button(top, text="Display", width=10, height=5, command=lambda: show("Display"))
#B6.place(x=200, y=200)

#B7 = Button(top, text="12", width=10, height=5, command=lambda: show("12"))
#B7.place(x=100, y=300)

#top.mainloop()