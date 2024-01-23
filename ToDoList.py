import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(user, master):
        user.master = master
        user.master.title("To-Do List Manager")

        user.tasks = []

        # Create GUI components
        user.task_entry = tk.Entry(master, width=50)
        user.task_entry.grid(row=0, column=0, padx=20, pady=20)

        user.add_button = tk.Button(master, text="Add Task", command=user.add_task)
        user.add_button.grid(row=0, column=1, padx=20, pady=20)

        user.task_listbox = tk.Listbox(master, width=50, height=15)
        user.task_listbox.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        user.remove_button = tk.Button(master, text="Remove Task", command=user.remove_task)
        user.remove_button.grid(row=2, column=0, padx=20, pady=20)

        user.clear_button = tk.Button(master, text="Clear All", command=user.clear_tasks)
        user.clear_button.grid(row=2, column=1, padx=20, pady=20)

        # creating functions that will be linked to users actions

    def add_task(user):
        task = user.task_entry.get()
        if task:
            user.tasks.append(task)
            user.update_task_list()
            user.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Please enter a task.")

    def remove_task(user):
        selected_task_index = user.task_listbox.curselection()
        if selected_task_index:
            user.tasks.pop(selected_task_index[0])
            user.update_task_list()

    def clear_tasks(user):
        user.tasks = []
        user.update_task_list()

    def update_task_list(user):
        user.task_listbox.delete(0, tk.END)
        for task in user.tasks:
            user.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
