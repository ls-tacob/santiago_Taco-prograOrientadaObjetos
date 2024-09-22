import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry
from eventos import Evento

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.configure(bg="#001F3F")  # Color de fondo azul eléctrico

        # Lista de eventos
        self.eventos = []

        # Crear contenedores
        self.create_widgets()

    def create_widgets(self):
        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(padx=10, pady=10)

        # Estilo de la tabla
        style = ttk.Style()
        style.configure("Treeview",
                        background="#e6f2ff",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#e6f2ff")
        style.map("Treeview", background=[("selected", "#007BFF")])

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("fecha", "hora", "descripcion", "estado"), show="headings")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.heading("estado", text="Estado")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(padx=10, pady=10)

        # Campos de entrada
        ttk.Label(self.frame_entrada, text="Fecha:", background="#001F3F", foreground="white").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada, date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora (HH:MM):", background="#001F3F", foreground="white").grid(row=1, column=0)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.frame_entrada, text="Descripción:", background="#001F3F", foreground="white").grid(row=2, column=0)
        self.descripcion_entry = ttk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1)

        ttk.Label(self.frame_entrada, text="Estado:", background="#001F3F", foreground="white").grid(row=3, column=0)
        self.estado_combo = ttk.Combobox(self.frame_entrada, values=["Iniciado", "Pendiente", "Finalizado"])
        self.estado_combo.grid(row=3, column=1)

        # Botones
        self.btn_agregar = ttk.Button(self.frame_entrada, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=4, column=0, columnspan=2)

        self.btn_editar = ttk.Button(self.frame_entrada, text="Editar Evento Seleccionado", command=self.editar_evento)
        self.btn_editar.grid(row=5, column=0, columnspan=2)

        self.btn_eliminar = ttk.Button(self.frame_entrada, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=6, column=0, columnspan=2)

        self.btn_salir = ttk.Button(self.frame_entrada, text="Salir", command=self.root.quit)
        self.btn_salir.grid(row=7, column=0, columnspan=2)

        # Vincular la selección de la tabla a la función de edición
        self.tree.bind("<<TreeviewSelect>>", self.cargar_evento_seleccionado)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()
        estado = self.estado_combo.get() or "Pendiente"  # Valor por defecto

        # Validar el formato de hora
        if not self.validar_hora(hora):
            messagebox.showwarning("Advertencia", "Formato de hora incorrecto. Use HH:MM.")
            return

        if fecha and hora and descripcion:
            nuevo_evento = Evento(fecha, hora, descripcion, estado)
            self.eventos.append(nuevo_evento)
            self.tree.insert("", "end", values=(fecha, hora, descripcion, estado))
            self.limpiar_campos()
            self.guardar_evento_en_historial(nuevo_evento)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def validar_hora(self, hora):
        try:
            datetime.strptime(hora, "%H:%M")
            return True
        except ValueError:
            return False

    def editar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            index = self.tree.index(seleccionado)
            evento = self.eventos[index]

            # Actualizar campos de entrada
            self.fecha_entry.set_date(evento.fecha)
            self.hora_entry.delete(0, tk.END)
            self.hora_entry.insert(0, evento.hora)
            self.descripcion_entry.delete(0, tk.END)
            self.descripcion_entry.insert(0, evento.descripcion)
            self.estado_combo.set(evento.estado)

            # Eliminar el evento antiguo para agregar el editado
            self.eliminar_evento()
            self.agregar_evento()
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para editar.")

    def cargar_evento_seleccionado(self, event):
        seleccionado = self.tree.selection()
        if seleccionado:
            index = self.tree.index(seleccionado)
            evento = self.eventos[index]
            self.fecha_entry.set_date(evento.fecha)
            self.hora_entry.delete(0, tk.END)
            self.hora_entry.insert(0, evento.hora)
            self.descripcion_entry.delete(0, tk.END)
            self.descripcion_entry.insert(0, evento.descripcion)
            self.estado_combo.set(evento.estado)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            index = self.tree.index(seleccionado)
            self.eventos.pop(index)  # Eliminar de la lista de eventos
            self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

    def limpiar_campos(self):
        self.fecha_entry.set_date(datetime.now())
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.estado_combo.set("")

    def guardar_evento_en_historial(self, evento):
        with open("agenda_historial.txt", "a") as archivo:
            archivo.write(str(evento) + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
