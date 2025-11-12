import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append()

    def pop(self):
        self.element.pop()

    def get_stack(self):
        return self.element

class StackApp:
    def __init__(self, root):
        self.stack = Stack()
        self.root = root
        self.root.title("Stack GUI")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.label = tk.Label(root, text="Enter an item to stack:")
        self.label.pack(pady=5)
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        self.push_btn = tk.Button(root, text="Push", command=self.push_item)
        self.push_btn.pack(pady=5)

        self.pop_btn = tk.Button(root, text="Pop", command=self.pop_item)
        self.pop_btn.pack(pady=5)

        self.display_btn = tk.Button(root, text="Display Stack", command=self.displayStack)
        self.display_btn.pack(pady=5)

        self.output_label = tk.Label(root, text="Stack: []", font=("Arial", 12))
        self.output_label.pack(pady=10)

    def push_item(self):
        item = self.entry.get().strip()
        if not item:
            messagebox.showwarning("Input Error", "Please enter a value to push")
            return
        self.stack.push()
        self.entry.delete(0, tk.END)
        self.displayStack()

    def pop_item(self):
        removed = self.stack.pop()
        if removed is None:
            messagebox.showinfo("Stack Empty", "No element to pop")
        else:
            messagebox.showinfo("Pop", f"Removed: {removed}")
        self.displayStack()

    def displayStack(self):
        s = self.stack.get_stack()
        self.output_label.config(text=f"Stack: {s}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StackApp(root)
    root.mainloop()