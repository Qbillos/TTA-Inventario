import tkinter as tk
from tkinter import messagebox
from conexion import *
from time import strftime
import pandas as pd
    
    
    

# LIBRERIAS PANDAS Y OPENPYXL
def exportar_ecxel():
        
    sql = "select id, nombre, precio, categoria from productos"

    db.cursor.execute(sql)
    
    filas = db.cursor.fetchall()
    
    id, nombre, precio, categoria = [], [], [], []
    
    i = 0
    
    for dato in filas:
        id.append(filas[i][0])
        nombre.append(filas[i][1])
        precio.append(filas[i][2])
        categoria.append(filas[i][3])
        i = i + 1
        
    fecha = str(strftime('%d-%m-%y_%H-%M-%S'))
    datos = {'Producto': nombre, 'Precio': precio, 'Categoria': categoria}
    df = pd.DataFrame(datos, columns = ['Producto', 'Precio', 'Categoria'])
    
    #print(df)
    
    df.to_excel(f"DATOS {fecha}.xlsx", sheet_name='Sheet_name_1')
    
    
    messagebox.showinfo('Información', 'Datos guardados')
    
    
    
    
    
    
    
    
    
    
    
    

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

def eliminar_producto(categoria, lista):
    # Obtener el índice seleccionado en la lista
    indice = lista.curselection()
    categoria = str(categoria)
    if indice:
        # Obtener el nombre del producto seleccionado
        nombre = lista.get(indice)
        nombre = nombre.split()[0]

        # Mostrar una alarma de confirmación antes de eliminar el producto
        confirmacion = messagebox.askokcancel("Confirmar eliminación", f"¿Está seguro de que desea eliminar el producto '{nombre}'?")

        if confirmacion:
            # Eliminar el producto de la base de datos
            consulta = f"DELETE FROM productos WHERE nombre = '{nombre}' AND categoria = '{categoria}'"
            db.cursor.execute(consulta)
            db.connection.commit()

            # Eliminar de la interfaz gráfica
            lista.delete(indice)
            messagebox.showinfo("Éxito", "El producto ha sido eliminado correctamente.")
    else:
        messagebox.showinfo("Error", "No se ha seleccionado ningún producto.")

        
        
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
    respuesta = messagebox.askyesno("Confirmar cambios", "¿Desea guardar los cambios?")
    if respuesta:
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
    ventana_venta.title("Carrito de compras")

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