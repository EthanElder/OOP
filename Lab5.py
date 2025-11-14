import tkinter as tk
from tkinter import messagebox

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, item):
        self.elements.append(item)

    def dequeue(self):
        if not self.elements:
            return None
        return self.elements.pop(0)

    def get_queue(self):
        return self.elements

class Stack:
    def __init__(self):
        self.element = []

    def push(self, item):
        self.element.append(item)

    def pop(self):
        self.element.pop()

    def get_stack(self):
        return self.element

class App:
    def __init__(self, root):
        self.queue = Queue()
        self.stack = Stack()
        self.root = root
        self.root.title("GUI")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Input label and entry
        self.label = tk.Label(root, text="Enter an item to enqueue or stack:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Buttons
        self.enqueue_btn = tk.Button(root, text="Enqueue", command=self.enqueue_item)
        self.enqueue_btn.pack(pady=5)

        self.push_btn = tk.Button(root, text="Stack", command=self.push_item)
        self.push_btn.pack(pady=5)

        self.dequeue_btn = tk.Button(root, text="Dequeue", command=self.dequeue_item)
        self.dequeue_btn.pack(pady=5)

        self.pop_btn = tk.Button(root, text="Pop", command=self.pop_item)
        self.pop_btn.pack(pady=5)

        self.output_label2 = tk.Label(root, text="Queue: []", font=("Arial", 12))
        self.output_label2.pack(pady=10)

        self.output_label1 = tk.Label(root, text="Stack: []", font=("Arial", 12))
        self.output_label1.pack(pady=10)

    def enqueue_item(self):
        item = self.entry.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Please enter a value to enqueue.")
            return
        self.queue.enqueue(item)
        self.entry.delete(0, tk.END)
        self.display_queue()

    def dequeue_item(self):
        removed = self.queue.dequeue()
        if removed is None:
            messagebox.showinfo("Queue Empty", "No elements to dequeue.")
        else:
            messagebox.showinfo("Dequeue", f"Removed: {removed}")
        self.display_queue()

    def display_queue(self):
        q = self.queue.get_queue()
        self.output_label2.config(text=f"Queue: {q}")

    def push_item(self):
        item = self.entry.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Please enter a value to push")
            return
        self.stack.push(item)
        self.entry.delete(0, tk.END)
        self.displaystack()

    def pop_item(self):
        self.stack.pop()
        self.displaystack()

    def displaystack(self):
        s = self.stack.get_stack()
        self.output_label1.config(text=f"Stack: {s}")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()