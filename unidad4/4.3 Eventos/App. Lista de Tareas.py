import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x450")

        # Frame para la entrada y botón de añadir tarea
        add_frame = tk.Frame(root)
        add_frame.pack(pady=10)

        self.new_task_entry = tk.Entry(add_frame, width=40)
        self.new_task_entry.grid(row=0, column=0)

        self.add_task_button = tk.Button(add_frame, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10)

        # Frame para los botones de manejo de tareas
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.mark_task_button = tk.Button(button_frame, text="Marcar como Completada", command=self.mark_task)
        self.mark_task_button.grid(row=0, column=0, padx=10)

        self.unmark_task_button = tk.Button(button_frame, text="Desmarcar Tarea", command=self.unmark_task)
        self.unmark_task_button.grid(row=0, column=1, padx=10)

        self.delete_task_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=2, padx=10)

        # Lista de tareas
        self.tasks_frame = ttk.Frame(root)
        self.tasks_frame.pack(fill=tk.BOTH, expand=True)

        self.tasks_list = ttk.Treeview(self.tasks_frame, columns=("Tarea", "Fecha de Creación"), show="headings")
        self.tasks_list.heading("Tarea", text="Descripción")
        self.tasks_list.heading("Fecha de Creación", text="Fecha de Creación")
        self.tasks_list.pack(fill=tk.BOTH, expand=True)

        # Cargar tareas desde un archivo al iniciar (ahora después de crear tasks_list)
        self.load_tasks()

        # Atajos de teclado
        root.bind('<Escape>', lambda e: root.quit())
        root.bind('<Return>', lambda e: self.mark_task() if self.tasks_list.selection() else self.add_task())
        root.bind('<Delete>', self.delete_task)  # Tecla 'Delete' para eliminar

        # Acciones solo cuando la entrada no tiene foco
        self.root.bind('<KeyPress-c>', self.check_focus)  # Tecla 'C' para marcar como completada
        self.root.bind('<KeyPress-u>', self.check_focus)  # Tecla 'U' para desmarcar tarea

    def check_focus(self, event):
        if self.new_task_entry.focus_get() is None:  # Verifica si la entrada no tiene foco
            if event.char == 'c':
                self.mark_task()
            elif event.char == 'u':
                self.unmark_task()

    def add_task(self, event=None):
        task = self.new_task_entry.get()
        if task:
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha actual
            self.tasks_list.insert('', tk.END, values=(task, created_at))
            self.new_task_entry.delete(0, tk.END)
            self.save_tasks()  # Guardar tareas después de añadir
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def mark_task(self):
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.item(selected_item, tags=('completed',))
            self.tasks_list.tag_configure('completed', background='light green')

    def unmark_task(self):
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.item(selected_item, tags=('uncompleted',))
            self.tasks_list.tag_configure('uncompleted', background='white')

    def delete_task(self, event=None):
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.delete(selected_item)
            self.save_tasks()  # Guardar tareas después de eliminar
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una tarea para eliminar.")

    def save_tasks(self):
        tasks = []
        for item in self.tasks_list.get_children():
            tasks.append(self.tasks_list.item(item)['values'])
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    self.tasks_list.insert('', tk.END, values=task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
