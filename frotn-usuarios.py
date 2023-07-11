import tkinter as tk
from tkinter import messagebox
import mysql.connector
# Establece la conexión con la base de datos
class DataBase:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tta" 
        )
        self.cursor = self.connection.cursor()

def editar_producto(ventana_producto, lista, index):
    def guardar_cambios():
        nombre = entrada_nombre.get()
        precio = entrada_precio.get()
        # Actualizar el producto en la lista del cuadro correspondiente
        lista.delete(index)
        lista.insert(index, f"Nombre: {nombre}, Precio: {precio}")
        ventana_producto.destroy()

    ventana_producto.title("Editar producto")
    ventana_producto.geometry("250x150")

    producto_actual = lista.get(index)
    nombre_actual = producto_actual.split(",")[0].split(":")[1].strip()
    precio_actual = producto_actual.split(",")[1].split(":")[1].strip()

    label_nombre = tk.Label(ventana_producto, text="Nombre:", font=("Arial", 12))
    label_nombre.pack(pady=5)
    entrada_nombre = tk.Entry(ventana_producto, font=("Arial", 12))
    entrada_nombre.insert(tk.END, nombre_actual)
    entrada_nombre.pack()

    label_precio = tk.Label(ventana_producto, text="Precio:", font=("Arial", 12))
    label_precio.pack(pady=5)
    entrada_precio = tk.Entry(ventana_producto, font=("Arial", 12))
    entrada_precio.insert(tk.END, precio_actual)
    entrada_precio.pack()

    boton_guardar = tk.Button(ventana_producto, text="Guardar cambios", command=guardar_cambios, font=("Arial", 12))
    boton_guardar.pack(pady=5)


def eliminar_producto(lista):
    seleccionado = lista.curselection()
    if len(seleccionado) > 0:
        indice = seleccionado[0]
        lista.delete(indice)


def confirmar_salida():
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas salir?")
    if confirmacion:
        ventana.destroy()


ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("800x600")
ventana.protocol("WM_DELETE_WINDOW", confirmar_salida)

welcome_label = tk.Label(ventana, text="Hola, bienvenido a Hospedaje TTA Armenia", font=("Arial", 20))
welcome_label.pack()

frame = tk.Frame(ventana)
frame.pack(pady=10)

search_label = tk.Label(frame, text="Buscar Productos", font=("Arial", 12))
search_label.pack(side=tk.TOP, padx=10, pady=10)

search_bar_frame = tk.Frame(frame)
search_bar_frame.pack(side=tk.TOP, padx=10)

search_bar = tk.Entry(search_bar_frame, width=30, font=("Arial", 12))
search_bar.pack(side=tk.LEFT)
search_button = tk.Button(search_bar_frame, text="Buscar", font=("Arial", 12))
search_button.pack(side=tk.LEFT)

frame_productos = tk.Frame(ventana)
frame_productos.pack(pady=10)

frame_comida = tk.Frame(frame_productos)
frame_comida.pack(side="left", padx=10)

frame_bebidas = tk.Frame(frame_productos)
frame_bebidas.pack(side="left", padx=10)

frame_higiene = tk.Frame(frame_productos)
frame_higiene.pack(side="left", padx=10)

label_comida = tk.Label(frame_comida, text="Comida", font=("Arial", 20))
label_comida.pack()

lista_comida = tk.Listbox(frame_comida, font=("Helvetica", 20))
lista_comida.pack()

label_bebidas = tk.Label(frame_bebidas, text="Bebidas", font=("Arial", 20))
label_bebidas.pack()

lista_bebidas = tk.Listbox(frame_bebidas, font=("Helvetica", 20))
lista_bebidas.pack()

label_higiene = tk.Label(frame_higiene, text="Higiene", font=(" Arial", 20))
label_higiene.pack()

lista_higiene = tk.Listbox(frame_higiene, font=("Helvetica", 20))
lista_higiene.pack()


cerrar_sesion_button = tk.Button(ventana, text="Cerrar sesión", command=confirmar_salida, font=("Arial", 12))
cerrar_sesion_button.pack(side=tk.LEFT, padx=30, pady=30, anchor=tk.SE)

realizar_venta_button = tk.Button(ventana, text="Realizar venta", font=("Arial", 12))
realizar_venta_button.pack(side=tk.BOTTOM, padx=30, pady=30, anchor=tk.SE)


ventana.mainloop()
