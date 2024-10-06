import tkinter as tk
from tkinter import messagebox, ttk
import json
import os


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Mejorado")
        self.root.geometry("500x500")

        # Variables
        self.tasks = []
        self.load_tasks()

        # Frame para la entrada y botón de añadir tarea
        add_frame = tk.Frame(root)
        add_frame.pack(pady=10)

        self.new_task_entry = tk.Entry(add_frame, width=30)
        self.new_task_entry.grid(row=0, column=0)

        self.priority_var = tk.StringVar(value='Baja')
        priority_options = ttk.Combobox(add_frame, textvariable=self.priority_var, values=['Baja', 'Media', 'Alta'])
        priority_options.grid(row=0, column=1)

        self.add_task_button = tk.Button(add_frame, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.grid(row=0, column=2, padx=10)

        # Frame para los botones de manejo de tareas
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.mark_task_button = tk.Button(button_frame, text="Marcar como Completada", command=self.mark_task)
        self.mark_task_button.grid(row=0, column=0, padx=10)

        self.edit_task_button = tk.Button(button_frame, text="Editar Tarea", command=self.edit_task)
        self.edit_task_button.grid(row=0, column=1, padx=10)

        self.delete_task_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=2, padx=10)

        # Lista de tareas
        self.tasks_frame = ttk.Frame(root)
        self.tasks_frame.pack(fill=tk.BOTH, expand=True)

        self.tasks_list = ttk.Treeview(self.tasks_frame, columns=("Tarea", "Prioridad"), show="headings")
        self.tasks_list.heading("Tarea", text="Descripción")
        self.tasks_list.heading("Prioridad", text="Prioridad")
        self.tasks_list.pack(fill=tk.BOTH, expand=True)

        self.load_tasks_to_list()

        # Atajos de teclado
        root.bind('<Escape>', lambda e: root.quit())
        root.bind('<Return>', lambda e: self.add_task())  # Tecla 'Enter' para añadir tarea
        root.bind('c', lambda e: self.mark_task() if self.tasks_list.selection() else None)  # Tecla 'C' para marcar como completada
        root.bind('e', lambda e: self.edit_task() if self.tasks_list.selection() else None)  # Tecla 'E' para editar
        root.bind('d', lambda e: self.delete_task() if self.tasks_list.selection() else None)  # Tecla 'D' para eliminar
        root.bind('<Delete>', lambda e: self.delete_task() if self.tasks_list.selection() else None)  # Tecla 'Delete' para eliminar

    def add_task(self):
        task = self.new_task_entry.get()
        priority = self.priority_var.get()
        if task:
            self.tasks.append({"task": task, "priority": priority, "completed": False})
            self.new_task_entry.delete(0, tk.END)
            self.priority_var.set('Baja')
            self.save_tasks()
            self.load_tasks_to_list()
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def mark_task(self):
        selected_item = self.tasks_list.selection()
        if selected_item:
            task = self.tasks_list.item(selected_item, 'values')[0]
            for t in self.tasks:
                if t['task'] == task:
                    t['completed'] = True
                    self.load_tasks_to_list()
                    break

    def edit_task(self):
        selected_item = self.tasks_list.selection()
        if selected_item:
            task = self.tasks_list.item(selected_item, 'values')[0]
            for t in self.tasks:
                if t['task'] == task:
                    new_task = self.new_task_entry.get()
                    if new_task:
                        t['task'] = new_task
                        t['priority'] = self.priority_var.get()
                        self.new_task_entry.delete(0, tk.END)
                        self.priority_var.set('Baja')
                        self.save_tasks()
                        self.load_tasks_to_list()
                    else:
                        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")
                    break

    def delete_task(self):
        selected_item = self.tasks_list.selection()
        if selected_item:
            task = self.tasks_list.item(selected_item, 'values')[0]
            self.tasks = [t for t in self.tasks if t['task'] != task]
            self.save_tasks()
            self.load_tasks_to_list()
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una tarea para eliminar.")

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks_to_list(self):
        self.tasks_list.delete(*self.tasks_list.get_children())
        for task in self.tasks:
            color = 'light green' if task['completed'] else 'white'
            self.tasks_list.insert('', tk.END, values=(task['task'], task['priority']), tags=('completed' if task['completed'] else ''))
            self.tasks_list.tag_configure('completed', background=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
