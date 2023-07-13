import tkinter as tk
from funciones import *



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inventario de Productos")



mensaje_bienvenida = tk.Label(ventana, text="Hola Bienvenido al Hospedaje!", font=("Arial", 20))
mensaje_bienvenida.pack(pady=10)

# Marco de búsqueda
marco_busqueda = tk.Frame(ventana)
marco_busqueda.pack(pady=10)

search_label = tk.Label(marco_busqueda, text="Buscar Productos", font=("Arial", 12))
search_label.pack(side=tk.LEFT, padx=10, pady=10)

search_bar = tk.Entry(marco_busqueda, width=30, font=("Arial", 12))
search_bar.pack(side=tk.LEFT, padx=10, pady=10)
search_button = tk.Button(marco_busqueda, text="Buscar", font=("Arial", 12))
search_button.pack(side=tk.LEFT, padx=10, pady=10)

marco_productos = tk.Frame(ventana)
marco_productos.pack(pady=10)

# lightblue
marco_comida = tk.Frame(marco_productos, bg="green3", padx=10, pady=10)
marco_comida.grid(row=0, column=0)

label_comida = tk.Label(marco_comida, text="Comida", font=("Arial", 20))
label_comida.pack()

lista_comida = tk.Listbox(marco_comida, font=("Helvetica", 12), width=50, height=20)
lista_comida.pack()

boton_comida = tk.Button(marco_comida, text="Agregar producto", command=lambda: agregar_producto("Comida", lista_comida, ventana), font=("Arial", 12)) 
boton_comida.pack(pady=10)

boton_comida_eliminar = tk.Button(marco_comida, text="Eliminar producto", command=lambda: eliminar_producto("Comida", lista_comida), font=("Arial", 12)) 
boton_comida_eliminar.pack(pady=5)

boton_comida_editar = tk.Button(marco_comida, text="Editar producto", command=lambda: editar_producto("Comida", lista_comida, ventana), font=("Arial", 12))
boton_comida_editar.pack(pady=5)

marco_bebidas = tk.Frame(marco_productos, bg="lightgreen", padx=10, pady=10)
marco_bebidas.grid(row=0, column=1)

label_bebidas = tk.Label(marco_bebidas, text="Bebidas", font=("Arial", 20))
label_bebidas.pack()

lista_bebidas = tk.Listbox(marco_bebidas, font=("Helvetica", 12), width=50, height=20)
lista_bebidas.pack()

boton_bebidas = tk.Button(marco_bebidas, text="Agregar producto", command=lambda: agregar_producto("Bebidas", lista_bebidas, ventana), font=("Arial", 12))
boton_bebidas.pack(pady=10)

boton_bebidas_eliminar = tk.Button(marco_bebidas, text="Eliminar producto", command=lambda: eliminar_producto("Bebidas", lista_bebidas), font=("Arial", 12))
boton_bebidas_eliminar.pack(pady=5)

boton_bebidas_editar = tk.Button(marco_bebidas, text="Editar producto", command=lambda: editar_producto("Bebidas", lista_bebidas, ventana), font=("Arial", 12))
boton_bebidas_editar.pack(pady=5)

marco_higiene = tk.Frame(marco_productos, bg="lightyellow", padx=10, pady=10)
marco_higiene.grid(row=0, column=2)

label_higiene = tk.Label(marco_higiene, text="Higiene producto", font=("Arial", 20))
label_higiene.pack()

lista_higiene = tk.Listbox(marco_higiene, font=("Helvetica", 12), width=50, height=20)
lista_higiene.pack()

boton_higiene = tk.Button(marco_higiene, text="Agregar producto", command=lambda: agregar_producto("Higiene", lista_higiene, ventana), font=("Arial", 12))
boton_higiene.pack(pady=10)

boton_higiene_eliminar = tk.Button(marco_higiene, text="Eliminar producto", command=lambda: eliminar_producto("Higiene", lista_higiene), font=("Arial", 12))
boton_higiene_eliminar.pack(pady=5)

boton_higiene_editar = tk.Button(marco_higiene, text="Editar producto", command=lambda: editar_producto("Higiene", lista_higiene, ventana), font=("Arial", 12))
boton_higiene_editar.pack(pady=5)


# Botón de salida
boton_salida = tk.Button(ventana, text="Salir", font=("Arial", 12), command=cerrar_programa)
boton_salida.pack(side=tk.LEFT, padx=20, pady=10)


# Botón de realizar venta
boton_venta = tk.Button(ventana, text="Realizar venta", font=("Arial", 12), command= lambda: ventana_venta(ventana))


boton_venta.pack(side=tk.RIGHT, padx=20, pady=10)

# Mostrar los productos en las listas correspondientes
mostrar_productos_categoria("Comida", lista_comida)
mostrar_productos_categoria("Bebidas", lista_bebidas)
mostrar_productos_categoria("Higiene", lista_higiene)


import tkinter as tk
from tkinter import messagebox
from conexion import *




def mostrar_productos_categoria(categoria, lista):
    consulta = f"SELECT nombre, precio, cantidad FROM productos WHERE categoria = '{categoria}'"
    db.cursor.execute(consulta)
    productos = db.cursor.fetchall()

    lista.delete(0, tk.END)

    for producto in productos:
        nombre = producto[0]
        precio = producto[1]
        cantidad = producto[2]
        lista.insert(tk.END, f"{nombre} - Precio: {precio} - Cantidad: {cantidad}")

def eliminar_producto (categoria, lista):
    #Obtener el indice seleccionado en la lista
    indice = lista.curselection()
    categoria = str (categoria)
    if indice:
        #Obtener el nombre del producto seleccionado
        nombre = lista.get(indice)
        nombre = nombre.split()[0]
        
        #Eliminar el producto de la base de datos
        consulta = f"DELETE FROM productos WHERE nombre = '{nombre}' AND categoria = '{categoria}'"
        db.cursor.execute(consulta)
        db.connection.commit()
        
        #eliminar de la interfaz grafica 
        lista.delete(indice)
        messagebox.showinfo("Exito", "El producto ha sifo eliminado correctamente.")
    
    else:
        messagebox.showinfo("Error" , "No se ha seleccionado ningun producto.")
        
        
def editar_producto(categoria, lista, ventana):
    seleccion = lista.curselection()  # Obtener índice seleccionado
    if seleccion:
        datos = lista.get(seleccion)  # Obtener nombre del producto
        
        nombre = datos.split()[0]
        
        consulta = f"SELECT nombre, precio, cantidad FROM productos WHERE nombre = '{nombre}'"
        db.cursor.execute(consulta)
        producto = db.cursor.fetchone()  # Obtener datos del producto
        
        
        if producto:
            ventana_editar = tk.Toplevel(ventana)
            ventana_editar.title("Editar Producto")

            etiqueta_nombre = tk.Label(ventana_editar, text="Nombre:")
            etiqueta_nombre.pack()
            campo_nombre = tk.Entry(ventana_editar)
            campo_nombre.pack()
            campo_nombre.insert(tk.END, producto[0])  # Mostrar nombre del producto

            etiqueta_precio = tk.Label(ventana_editar, text="Precio:")
            etiqueta_precio.pack()
            campo_precio = tk.Entry(ventana_editar)
            campo_precio.pack()
            campo_precio.insert(tk.END, producto[1])  # Mostrar precio del producto

            etiqueta_cantidad = tk.Label(ventana_editar, text="Cantidad:")
            etiqueta_cantidad.pack()
            campo_cantidad = tk.Entry(ventana_editar)
            campo_cantidad.pack()
            campo_cantidad.insert(tk.END, producto[2])  # Mostrar cantidad del producto

            boton_guardar = tk.Button(ventana_editar, text="Guardar", command=lambda: guardar_edicion(ventana_editar, nombre, campo_nombre.get(), campo_precio.get(), campo_cantidad.get(), lista, categoria))
            boton_guardar.pack()
    else:
        messagebox.showinfo("Error" , "No se ha seleccionado ningun producto.")
        
        
        
        
        

def guardar_edicion(ventana_editar, nombre_original, nombre_nuevo, precio_nuevo, cantidad_nueva, lista, categoria):
    consulta = "UPDATE productos SET nombre = %s, precio = %s, cantidad = %s WHERE nombre = %s"
    db.cursor.execute(consulta, (nombre_nuevo, precio_nuevo, cantidad_nueva, nombre_original))
    db.connection.commit()
    mostrar_productos_categoria(categoria, lista)
    messagebox.showinfo("Éxito", "Los cambios han sido guardados correctamente.")
    ventana_editar.destroy()




def agregar_producto(categoria, lista, ventana):
    tabla = str(categoria)

    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Producto")

    etiqueta_nombre = tk.Label(ventana_agregar, text="Nombre:")
    etiqueta_nombre.pack()
    campo_nombre = tk.Entry(ventana_agregar)
    campo_nombre.pack()

    etiqueta_precio = tk.Label(ventana_agregar, text="Precio:")
    etiqueta_precio.pack()
    campo_precio = tk.Entry(ventana_agregar)
    campo_precio.pack()

    etiqueta_cantidad = tk.Label(ventana_agregar, text="Cantidad:")
    etiqueta_cantidad.pack()
    campo_cantidad = tk.Entry(ventana_agregar)
    campo_cantidad.pack()

    boton_guardar = tk.Button(ventana_agregar, text="Guardar", command=lambda: guardar_producto(ventana_agregar, campo_nombre, campo_precio, campo_cantidad, tabla, lista))
    boton_guardar.pack()

def guardar_producto(ventana_agregar, campo_nombre, campo_precio, campo_cantidad, tabla, lista):
    nombre = campo_nombre.get()
    precio = campo_precio.get()
    cantidad = campo_cantidad.get()

    valores = (nombre, precio, cantidad, tabla)
    consulta = "INSERT INTO productos (nombre, precio, cantidad, categoria) VALUES (%s, %s, %s, %s)"

    db.cursor.execute(consulta, valores)
    db.connection.commit()

    mostrar_productos_categoria(tabla,lista)
    
    
    
    
    messagebox.showinfo("Éxito", "El producto ha sido agregado correctamente.")
    ventana_agregar.destroy()


















# def editar_producto_seleccionado(lista):
#     seleccion = lista.curselection()  # Obtener índice seleccionado
#     if seleccion:
#         nombre = lista.get(seleccion)  # Obtener nombre del producto
#         ventana_editar = tk.Toplevel(ventana)
#         ventana_editar.title("Editar Producto")

#         etiqueta_nombre = tk.Label(ventana_editar, text="Nombre:")
#         etiqueta_nombre.pack()
#         campo_nombre = tk.Entry(ventana_editar)
#         campo_nombre.pack()

#         etiqueta_precio = tk.Label(ventana_editar, text="Precio:")
#         etiqueta_precio.pack()
#         campo_precio = tk.Entry(ventana_editar)
#         campo_precio.pack()

#         etiqueta_cantidad = tk.Label(ventana_editar, text="Cantidad:")
#         etiqueta_cantidad.pack()
#         campo_cantidad = tk.Entry(ventana_editar)
#         campo_cantidad.pack()

#         boton_cargar = tk.Button(ventana_editar, text="Cargar", command=lambda: cargar_datos_editar(nombre, campo_nombre, campo_precio, campo_cantidad))
#         boton_cargar.pack()

#         boton_guardar = tk.Button(ventana_editar, text="Guardar", command=lambda: guardar_edicion(ventana_editar, nombre, campo_nombre.get(), campo_precio.get(), campo_cantidad.get(), lista))
#         boton_guardar.pack()

# def cargar_datos_editar(nombre, campo_nombre, campo_precio, campo_cantidad):
    consulta = "SELECT nombre, precio, cantidad FROM productos WHERE nombre = %s"
    db.cursor.execute(consulta, (nombre,))
    producto = db.cursor.fetchone()

    if producto:
        campo_nombre.insert(tk.END, producto[0])
        campo_precio.insert(tk.END, producto[1])
        campo_cantidad.insert(tk.END, producto[2])
        
      
      

def ventana_venta(ventana):
    ventana_venta = tk.Toplevel(ventana)
    ventana_venta.title("Realizar Venta")

    marco_venta = tk.Frame(ventana_venta)
    marco_venta.pack(padx=10, pady=10)

    marco_venta = tk.Frame(ventana_venta)
    marco_venta.pack(padx=10, pady=10)

    boton_descartar = tk.Button(marco_venta, text="Descartar venta", font=("Arial", 12))
    boton_descartar.pack(side=tk.LEFT, anchor=tk.NW, padx=10, pady=10)
    
    lista_productos = tk.Listbox(marco_venta, font=("Helvetica", 12), width=50, height=20)
    lista_productos.pack()
    
    marco_botones = tk.Frame(ventana_venta)
    marco_botones.pack(pady=10)

    boton_cancelar = tk.Button(marco_botones, text="Cancelar venta", font=("Arial", 12))
    boton_cancelar.pack(side=tk.LEFT, padx=10)


    boton_confirmar = tk.Button(marco_botones, text="Confirmar venta", font=("Arial", 12))
    boton_confirmar.pack(side=tk.RIGHT, padx=10)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
db = DataBase()


ventana.mainloop()




