from funcionalidad import AgendaApp
import tkinter as tk
from tkcalendar import DateEntry

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
