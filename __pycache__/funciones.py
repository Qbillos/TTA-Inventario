import tkinter as tk
from tkinter import messagebox
from conexion import *




def mostrar_productos_categoria(categoria, lista):
    consulta = f"SELECT nombre, precio FROM productos WHERE categoria = '{categoria}'"
    db.cursor.execute(consulta)
    productos = db.cursor.fetchall()

    lista.delete(0, tk.END)

    for producto in productos:
        nombre = producto[0]
        precio = producto[1]
        lista.insert(tk.END, f"{nombre} - {precio}")









# ventana que muestra el modal
def agregar_producto(categoria, lista):
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
    
    
    boton_guardar = tk.Button(ventana_agregar, text="Guardar", command= lambda: guardar_producto(ventana_agregar, campo_nombre, campo_precio, tabla, lista))
    boton_guardar.pack() 
    
    
    # etiqueta_categoria = tk.Label(ventana_agregar, text="Categoria:")
    # etiqueta_categoria.pack()
    # campo_categoria = tk.Entry(ventana_agregar)
    # campo_categoria.pack()
    
    
       
    
    
    
    
    
    
def eliminar_producto(categoria, lista):
    # Obtener el índice seleccionado en la lista
    indice = lista.curselection()
    #print(indice)
    
    if indice:
        # Obtener el nombre del producto seleccionado
        nombre = lista.get(indice)
        nombre = nombre.split()[0]
        

        # Eliminar el producto de la base de datos
        consulta = f"DELETE FROM productos WHERE nombre = '{nombre}' AND categoria = '{categoria}'"
        db.cursor.execute(consulta)
        db.connection.commit()

        # Eliminar el producto de la interfaz gráfica
        lista.delete(indice)

        messagebox.showinfo("Éxito", "El producto ha sido eliminado correctamente.")
    else:
        messagebox.showinfo("Error", "No se ha seleccionado ningún producto.")


    
    
    
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
    
def guardar_producto(ventana_agregar, campo_nombre, campo_precio, tabla, lista):
    
        
        nombre = campo_nombre.get()
        precio = campo_precio.get()
        # categoria = campo_categoria.get()
        
        
        # descripcion = campo_descripcion.get()
        # cantidad = campo_cantidad.get()
        # proveedor_id = campo_proveedor_id.get()
        # Resto de campos del formulario
        
        # consulta = "INSERT INTO productos (nombre, codigo, descripcion, cantidad, precio_compra, precio_venta, proveedor_id, fecha_compra, ubicacion_id, categoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # valores = (nombre, codigo, descripcion, cantidad, precio_compra, precio_venta, proveedor_id, fecha_compra, ubicacion_id, categoria)
        
        
        valores = (nombre, precio, tabla)
        consulta = "INSERT INTO productos (nombre, precio, categoria) VALUES (%s, %s, %s)"
        
        
        db.cursor.execute(consulta, valores)
        db.connection.commit()
        
        # Mostrar el producto en la lista correspondiente
        if tabla == "Comida":
            #lista_comida.insert(tk.END, nombre)
            
            mostrar_productos_categoria(tabla, lista)
            messagebox.showinfo("Éxito", "El producto ha sido agregado correctamente.")
            ventana_agregar.destroy()
            
            
        elif tabla == "Bebidas":
            #lista_bebidas.insert(tk.END, nombre)
            
            mostrar_productos_categoria(tabla, lista)
            messagebox.showinfo("Éxito", "El producto ha sido agregado correctamente.")
            ventana_agregar.destroy()
            
            
        elif tabla == "Higiene":
            #lista_higiene.insert(tk.END, nombre)
            
            mostrar_productos_categoria(tabla, lista)
            messagebox.showinfo("Éxito", "El producto ha sido agregado correctamente.")
            ventana_agregar.destroy()
            
    
            
    


#funcion editar producto 
def editar_producto(categoria, lista):
    categoria = str(categoria)
    
    
    seleccion = lista.curselection()  # Obtener índice seleccionado
    if seleccion:
        indice = lista.get(seleccion)
        nombre = indice.split()[0]# Obtener nombre del producto
        nombre = str(nombre)
        
        
        consulta = f"SELECT nombre, precio FROM productos WHERE nombre = '{nombre}'"
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

            boton_guardar = tk.Button(ventana_editar, text="Guardar", command=lambda: guardar_edicion(ventana_editar, nombre, campo_nombre.get(), campo_precio.get(), lista, categoria))
            boton_guardar.pack()
    else:
        messagebox.showinfo("Error", "No se ha seleccionado ningún producto.")



def guardar_edicion(ventana_editar, nombre_original, nombre_nuevo, precio_nuevo, lista, categoria):
    consulta = "UPDATE productos SET nombre = %s, precio = %s WHERE nombre = %s"
    db.cursor.execute(consulta, (nombre_nuevo, precio_nuevo, nombre_original))
    db.connection.commit()
    #lista.delete(lista.curselection())
    #lista.insert(lista.curselection(), nombre_nuevo)
    mostrar_productos_categoria(categoria, lista)
    ventana_editar.destroy()
    messagebox.showinfo("Éxito", "Los cambios han sido guardados correctamente.")


    
    
    
db = DataBase()  
    
    
    
    

    
    
    
    
    
    
