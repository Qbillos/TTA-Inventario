import tkinter as tk
from tkinter import messagebox
# from tkinter import ttk
from conexion import *

db = DataBase()

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




def eliminar_producto(lista):
    seleccion = lista.curselection()  # Obtener índice seleccionado
    if seleccion:
        nombre = lista.get(seleccion)  # Obtener nombre del producto
        consulta = "DELETE FROM productos WHERE nombre = %s"
        db.cursor.execute(consulta, (nombre,))
        db.connection.commit()
        lista.delete(seleccion)  # Eliminar elemento de la lista
        messagebox.showinfo("Éxito", "El producto ha sido eliminado correctamente.")


def editar_producto(lista):
    seleccion = lista.curselection()  # Obtener índice seleccionado
    if seleccion:
        nombre = lista.get(seleccion)  # Obtener nombre del producto
        consulta = "SELECT nombre, precio FROM productos WHERE nombre = %s"
        db.cursor.execute(consulta, (nombre,))
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

            boton_guardar = tk.Button(ventana_editar, text="Guardar", command=lambda: guardar_edicion(ventana_editar, nombre, campo_nombre.get(), campo_precio.get(), lista))
            boton_guardar.pack()

def guardar_edicion(ventana_editar, nombre_original, nombre_nuevo, precio_nuevo, lista):
    consulta = "UPDATE productos SET nombre = %s, precio = %s WHERE nombre = %s"
    db.cursor.execute(consulta, (nombre_nuevo, precio_nuevo, nombre_original))
    db.connection.commit()
    lista.delete(lista.curselection())
    lista.insert(lista.curselection(), nombre_nuevo)
    ventana_editar.destroy()
    messagebox.showinfo("Éxito", "Los cambios han sido guardados correctamente.")


 
 

# ventana que muestra el modal
def agregar_producto(categoria):
    
    
    
    #esta es la ventana 
    
    tabla = str(categoria)
    
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Producto")

    etiqueta_nombre = tk.Label(ventana_agregar, text="Nombre:")
    etiqueta_nombre.pack()
    campo_nombre = tk.Entry(ventana_agregar)
    campo_nombre.pack()




    etiqueta_precio = tk.Label(ventana_agregar, text="precio:")
    etiqueta_precio.pack()
    campo_precio = tk.Entry(ventana_agregar)
    campo_precio.pack()
    
    
    etiqueta_cantidad = tk.Label(ventana_agregar, text="Cantidad:")
    etiqueta_cantidad.pack()
    campo_cantidad = tk.Entry(ventana_agregar)
    campo_cantidad.pack()
    
    
    boton_guardar = tk.Button(ventana_agregar, text="Guardar", command=lambda: guardar_producto(ventana_agregar, campo_nombre, campo_precio, tabla, "Comida"))
    boton_guardar
    

    
    
    # etiqueta_categoria = tk.Label(ventana_agregar, text="Categoria:")
    # etiqueta_categoria.pack()
    # campo_categoria = tk.Entry(ventana_agregar)
    # campo_categoria.pack()

    
       


    

    
   
    
    
    
    
    
    
    
    
    # etiqueta_precio = tk.Label(ventana_agregar, text="Precio:")
    # etiqueta_precio.pack()
    
    
    # global campo_precio = tk.Entry(ventana_agregar)
    
    
    # campo_precio.pack()
    
    
    # etiqueta_descripcion = tk.Label(ventana_agregar, text="descripcion:")
    # etiqueta_descripcion.pack()
    
    
    
    # global campo_descripcion = tk.Entry(ventana_agregar)
    
    
    # campo_descripcion.pack()
    
    
    
    # etiqueta_cantidad = tk.Label(ventana_agregar, text="cantidad:")
    # etiqueta_cantidad.pack()
    
    
    # global campo_cantidad = tk.Entry(ventana_agregar)
    
    
    
    # campo_cantidad.pack()
    
    # etiqueta_provedorid = tk.Label(ventana_agregar, text="provedor:")
    # etiqueta_provedorid.pack()
    
    
    
    
    # global campo_proveedor_id = tk.Entry(ventana_agregar)
    
    
    
    
    # campo_proveedor_id.pack()
    
    
    
    
    

    
    
    
    
    
    

    # Resto de campos del formulario
    
def guardar_producto(ventana_agregar, campo_cantidad, campo_nombre, campo_precio, tabla):
    
        
        nombre = campo_nombre.get()
        precio = campo_precio.get()
        cantidad = campo_cantidad.get()
        # categoria = campo_categoria.get()
        
        
        # descripcion = campo_descripcion.get()
        # cantidad = campo_cantidad.get()
        # proveedor_id = campo_proveedor_id.get()
        # Resto de campos del formulario
        
        # consulta = "INSERT INTO productos (nombre, codigo, descripcion, cantidad, precio_compra, precio_venta, proveedor_id, fecha_compra, ubicacion_id, categoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # valores = (nombre, codigo, descripcion, cantidad, precio_compra, precio_venta, proveedor_id, fecha_compra, ubicacion_id, categoria)
        
        valores = (nombre, precio, cantidad, tabla)
        consulta = "INSERT INTO productos (nombre, precio, cantidad, categoria) VALUES (%s, %s, %s, %s)"
        
        db.cursor.execute(consulta, valores)
        db.connection.commit()
        
        # Mostrar el producto en la lista correspondiente
        if tabla == "Comida":   
            lista_comida.insert(tk.END, nombre)
            messagebox.showinfo("Éxito", "El producto ha sido agregado correctamente.")
            ventana_agregar.destroy()
            
            
        elif tabla == "Bebidas":
            lista_bebidas.insert(tk.END, nombre)
            messagebox.showinfo("Éxito", "El producto ha sido agregado correctamente.")
            ventana_agregar.destroy()
            
            
        elif tabla == "Higiene":
            lista_higiene.insert(tk.END, nombre)
            messagebox.showinfo("Éxito", "El producto ha sido agregado correctamente.")
            ventana_agregar.destroy()
                    
            
        
    
    
    
    
    


    
    
    
    
    
    
    
    

    
    
    
 

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

boton_comida = tk.Button(marco_comida, text="Agregar producto", command=lambda: agregar_producto("Comida"), font=("Arial", 12))
boton_comida.pack(pady=10)

boton_comida_eliminar = tk.Button(marco_comida, text="Eliminar producto", command=lambda: eliminar_producto(lista_comida), font=("Arial", 12))
boton_comida_eliminar.pack(pady=5)

boton_comida_editar = tk.Button(marco_comida, text="Editar producto", command=lambda: editar_producto(lista_comida), font=("Arial", 12))
boton_comida_editar.pack(pady=5)



marco_bebidas = tk.Frame(marco_productos, bg="lightgreen", padx=10, pady=10)
marco_bebidas.grid(row=0, column=1)

label_bebidas = tk.Label(marco_bebidas, text="Bebidas", font=("Arial", 20))
label_bebidas.pack()

lista_bebidas = tk.Listbox(marco_bebidas, font=("Helvetica", 12), width=50, height=20)
lista_bebidas.pack()

boton_bebidas = tk.Button(marco_bebidas, text="Agregar producto", command=lambda: agregar_producto("Bebidas"), font=("Arial", 12))
boton_bebidas.pack(pady=10)

boton_bebidas_eliminar = tk.Button(marco_bebidas, text="Eliminar producto", command=lambda: eliminar_producto(lista_bebidas), font=("Arial", 12))
boton_bebidas_eliminar.pack(pady=5)

boton_bebidas_editar = tk.Button(marco_bebidas, text="Editar producto", command=lambda: editar_producto(lista_bebidas), font=("Arial", 12))
boton_bebidas_editar.pack(pady=5)

marco_higiene = tk.Frame(marco_productos, bg="lightyellow", padx=10, pady=10)
marco_higiene.grid(row=0, column=2)

label_higiene = tk.Label(marco_higiene, text="Higiene producto", font=("Arial", 20))
label_higiene.pack()

lista_higiene = tk.Listbox(marco_higiene, font=("Helvetica", 12), width=50, height=20)
lista_higiene.pack()

boton_higiene = tk.Button(marco_higiene, text="Agregar producto", command=lambda: agregar_producto("Higiene"), font=("Arial", 12))
boton_higiene.pack(pady=10)

boton_higiene_eliminar = tk.Button(marco_higiene, text="Eliminar producto", command=lambda: eliminar_producto(lista_higiene), font=("Arial", 12))
boton_higiene_eliminar.pack(pady=5)

boton_higiene_editar = tk.Button(marco_higiene, text="Editar producto", command=lambda: editar_producto(lista_higiene), font=("Arial", 12))
boton_higiene_editar.pack(pady=5)

# Botón de salida
boton_salida = tk.Button(ventana, text="Salir", font=("Arial", 12))
boton_salida.pack(side=tk.RIGHT, padx=30, pady=10)
#ESTE BOTON DE SALIR NO CREO QUE SEA TAN NECESARIO BRO MIENTRASTANTO
    
# Botón de realizar venta
boton_venta = tk.Button(ventana, text="Realizar venta", font=("Arial", 12))
boton_venta.pack(side=tk.LEFT, padx=20, pady=10)

# Mostrar los productos en las listas correspondientes
mostrar_productos_categoria("Comida", lista_comida)
mostrar_productos_categoria("Bebidas", lista_bebidas)
mostrar_productos_categoria("Higiene", lista_higiene)       



ventana.mainloop()