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


class QueueApp:
    def __init__(self, root):
        self.queue = Queue()
        self.root = root
        self.root.title("Queue GUI")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Input label and entry
        self.label = tk.Label(root, text="Enter an item to enqueue:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Buttons
        self.enqueue_btn = tk.Button(root, text="Enqueue", command=self.enqueue_item)
        self.enqueue_btn.pack(pady=5)

        self.dequeue_btn = tk.Button(root, text="Dequeue", command=self.dequeue_item)
        self.dequeue_btn.pack(pady=5)

        self.display_btn = tk.Button(root, text="Display Queue", command=self.display_queue)
        self.display_btn.pack(pady=5)

        # Output label
        self.output_label = tk.Label(root, text="Queue: []", font=("Arial", 12))
        self.output_label.pack(pady=10)

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
        self.output_label.config(text=f"Queue: {q}")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = QueueApp(root)
    root.mainloop()