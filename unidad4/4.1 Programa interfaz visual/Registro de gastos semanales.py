import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime

class GastoSemanalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Gasto Semanal")

        # Variables
        self.descripcion_var = tk.StringVar()
        self.monto_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.fecha_var = tk.StringVar()
        self.hora_var = tk.StringVar()

        # Layout
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y campo de descripción
        tk.Label(self.root, text="Descripción:").grid(row=0, column=0, padx=10, pady=5)
        self.descripcion_entry = tk.Entry(self.root, textvariable=self.descripcion_var)
        self.descripcion_entry.grid(row=0, column=1, padx=10, pady=5)

        # Campo de selección de categorías
        tk.Label(self.root, text="Categoría:").grid(row=1, column=0, padx=10, pady=5)
        categorias = ['Alimentación', 'Transporte', 'Salud', 'Implementos de Aseo', 'Deudas', 'Pagos Trabajo', 'Estudios']
        self.categoria_menu = ttk.Combobox(self.root, textvariable=self.categoria_var, values=categorias)
        self.categoria_menu.grid(row=1, column=1, padx=10, pady=5)

        # Selector de fecha
        tk.Label(self.root, text="Fecha:").grid(row=2, column=0, padx=10, pady=5)
        self.fecha_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.grid(row=2, column=1, padx=10, pady=5)

        # Selector de hora
        tk.Label(self.root, text="Hora:").grid(row=3, column=0, padx=10, pady=5)
        self.hora_entry = tk.Entry(self.root, textvariable=self.hora_var)
        self.hora_entry.grid(row=3, column=1, padx=10, pady=5)
        self.hora_entry.insert(0, datetime.datetime.now().strftime('%H:%M'))

        # Campo de monto (acepta float)
        tk.Label(self.root, text="Monto (float):").grid(row=4, column=0, padx=10, pady=5)
        self.monto_entry = tk.Entry(self.root, textvariable=self.monto_var)
        self.monto_entry.grid(row=4, column=1, padx=10, pady=5)

        # Botones
        tk.Button(self.root, text="Agregar", command=self.agregar_gasto).grid(row=5, column=0, padx=10, pady=5)
        tk.Button(self.root, text="Limpiar", command=self.limpiar_formulario).grid(row=5, column=1, padx=10, pady=5)

        # Tabla de gastos
        self.tabla = ttk.Treeview(self.root, columns=("descripcion", "categoria", "fecha", "hora", "monto"), show='headings')
        self.tabla.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        self.tabla.heading("descripcion", text="Descripción")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("fecha", text="Fecha")
        self.tabla.heading("hora", text="Hora")
        self.tabla.heading("monto", text="Monto")

    def agregar_gasto(self):
        descripcion = self.descripcion_var.get()
        categoria = self.categoria_var.get()
        fecha = self.fecha_entry.get()
        hora = self.hora_var.get()
        monto = self.monto_var.get()

        try:
            monto = float(monto)
            self.tabla.insert("", "end", values=(descripcion, categoria, fecha, hora, monto))
            self.limpiar_formulario()
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número decimal válido.")

    def limpiar_formulario(self):
        self.descripcion_var.set("")
        self.categoria_var.set("")
        self.monto_var.set("")
        self.hora_entry.delete(0, tk.END)
        self.hora_entry.insert(0, datetime.datetime.now().strftime('%H:%M'))

if __name__ == "__main__":
    root = tk.Tk()
    app = GastoSemanalApp(root)
    root.mainloop()
