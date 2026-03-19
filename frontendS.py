import tkinter as tk
from tkinter import messagebox
from listaS import TaskList

class App:
    def __init__(self, root):
        self.list = TaskList()

        root.title("🌸 Tasks by TuNombre")
        root.geometry("420x500")
        root.configure(bg="#ffc0cb")

        # ---------- TITLE ----------
        self.title_label = tk.Label(
            root,
            text="To-Do List",
            bg="#ffc0cb",
            fg="white",
            font=("Helvetica", 18, "bold")
        )
        self.title_label.pack(pady=10)

        # ---------- INPUT ----------
        self.entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.entry.pack(pady=10)

        # ---------- BUTTON FRAME ----------
        btn_frame = tk.Frame(root, bg="#ffc0cb")
        btn_frame.pack(pady=5)

        self.create_button(btn_frame, "Add", self.add_task).grid(row=0, column=0, padx=5, pady=5)
        self.create_button(btn_frame, "Delete", self.delete_task).grid(row=0, column=1, padx=5, pady=5)
        self.create_button(btn_frame, "Update", self.update_task).grid(row=1, column=0, padx=5, pady=5)
        self.create_button(btn_frame, "Move", self.move_task).grid(row=1, column=1, padx=5, pady=5)

        # ---------- LIST FRAME ----------
        list_frame = tk.Frame(root, bg="#ffc0cb")
        list_frame.pack(pady=10)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            list_frame,
            width=40,
            height=12,
            font=("Arial", 11),
            bg="#fff0f5",
            bd=0,
            highlightthickness=0,
            yscrollcommand=scrollbar.set
        )
        self.listbox.pack(side=tk.LEFT)

        scrollbar.config(command=self.listbox.yview)

        # ---------- FOOTER ----------
        self.footer = tk.Label(
            root,
            text="Linked List Implementation",
            bg="#ffc0cb",
            fg="white",
            font=("Arial", 9)
        )
        self.footer.pack(pady=10)

    # ---------- BUTTON STYLE ----------
    def create_button(self, parent, text, command):
        return tk.Button(
            parent,
            text=text,
            command=command,
            width=10,
            bg="#e75480",
            fg="black",
            relief="flat",
            font=("Arial", 10, "bold"),
            activebackground="#d9436e",
            activeforeground="black",
            cursor="hand2"
        )

    # ---------- FUNCTIONS ----------
    def add_task(self):
        task = self.entry.get()
        if task:
            self.list.add_contac(task)
            print(f"[INFO] Task added: {task}")
            self.refresh()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Notice", "Please enter a task 🌸")

    def delete_task(self):
        sel = self.listbox.curselection()
        if sel:
            task = self.listbox.get(sel)[2:]  # 🔥 FIX
            self.list.delete_task(task)
            print(f"[INFO] Task deleted: {task}")
            self.refresh()
        else:
            messagebox.showwarning("Notice", "Select a task")

    def update_task(self):
        sel = self.listbox.curselection()
        new_task = self.entry.get()
        if sel and new_task:
            old_task = self.listbox.get(sel)[2:]  # 🔥 FIX
            self.list.update_task(old_task, new_task)
            print(f"[INFO] Task updated: {old_task} -> {new_task}")
            self.refresh()
        else:
            messagebox.showwarning("Notice", "Select and write a new task")

    def move_task(self):
        sel = self.listbox.curselection()
        if sel:
            task = self.listbox.get(sel)[2:]  # 🔥 FIX
            self.list.move_task_to_end(task)
            print(f"[INFO] Task moved: {task}")
            self.refresh()
        else:
            messagebox.showwarning("Notice", "Select a task")

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for task in self.list.get_tasks():
            self.listbox.insert(tk.END, f"• {task}")

        print("[INFO] List updated")