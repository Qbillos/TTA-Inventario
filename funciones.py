def agregar_producto(ventana_producto, lista, categoria):
    def guardar_producto():
        nombre = entrada_nombre.get()
        precio = entrada_precio.get()
        # Agregar el producto a la lista del cuadro correspondiente
        lista.insert(tk.END, f"Nombre: {nombre}, Precio: {precio}, Categoría: {categoria}")
        ventana_producto.destroy()

    ventana_producto.title(f"Agregar producto - {categoria}")
    ventana_producto.geometry("250x150")

    label_nombre = tk.Label(ventana_producto, text="Nombre:", font=("Arial", 12))
    label_nombre.pack(pady=5)
    entrada_nombre = tk.Entry(ventana_producto, font=("Arial", 12))
    entrada_nombre.pack()

    label_precio = tk.Label(ventana_producto, text="Precio:", font=("Arial", 12))
    label_precio.pack(pady=5)
    entrada_precio = tk.Entry(ventana_producto, font=("Arial", 12))
    entrada_precio.pack()

    boton_guardar = tk.Button(ventana_producto, text="Guardar", command=guardar_producto, font=("Arial", 12))
    boton_guardar.pack(pady=5)


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


def cerrar_ventana():
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas salir?")
    if confirmacion:
        ventana.quit()
