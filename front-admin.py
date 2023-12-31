import tkinter as tk
from tkinter import ttk, messagebox
from funciones import *



# Crear la ventana principal
ventana = tk.Tk()
ventana.config(width=300, height=200)
ventana.title("Inventario de Productos")

style = ttk.Style() 
style.configure('C.TButton', font=("Roboto Cn", 12))
style.configure('C.TButton', relief="ridge")
style.configure('C.TButton', width=3)
style.configure('C.TButton', bd=1)
style.configure('C.TButton', bg="green")



mensaje_bienvenida = tk.Label(ventana, text="Hola Bienvenido al Hospedaje!", font=("Arial", 20))
mensaje_bienvenida.pack(pady=10)





#Confirmar salida del programa
def confirmar_salida():
    if messagebox.askokcancel("Confirmar salida", "¿Está seguro de que desea salir?"):
        ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", confirmar_salida)
# Asociar la función confirmar_salida con el evento WM_DELETE_WINDOW de la ventana











def enviar_carrito():
    if not lista_comida.curselection() and not lista_bebidas.curselection() and not lista_higiene.curselection():
        messagebox.showwarning("Error", "Por favor, seleccione al menos un producto antes de enviar al carrito.")
    else:
        # Aquí puedes agregar la lógica para enviar los productos seleccionados al carrito
        messagebox.showinfo("Éxito", "Productos enviados al carrito correctamente.")

boton_enviar_carrito = ttk.Button(ventana, text="Enviar a carrito", width=13, style='C.TButton', command=enviar_carrito)
boton_enviar_carrito.pack(padx=60, anchor="nw") 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# Marco de búsqueda
marco_busqueda = tk.Frame(ventana)
marco_busqueda.pack(pady=10)

search_label = tk.Label(marco_busqueda, text="Buscar Productos", font=("Arial", 12))
search_label.pack(side=tk.LEFT, padx=10, pady=10)

search_bar = ttk.Entry(marco_busqueda, width=30, font=("Arial", 12))
search_bar.pack(side=tk.LEFT, padx=10, pady=10)

marco_productos = tk.Frame(ventana)
marco_productos.pack(pady=5)

# lightblue
marco_comida = tk.Frame(marco_productos, bg="#4A6275", padx=10, pady=10)
marco_comida.grid(row=0, column=0)

label_comida = tk.Label(marco_comida, text="Comida", font=("Arial", 15))
label_comida.pack()

lista_comida = tk.Listbox(marco_comida, font=("Helvetica", 12), width=50, height=20)
lista_comida.pack()

boton_comida = ttk.Button(marco_comida, text="Agregar producto", style='C.TButton', width=14, command=lambda: agregar_producto("Comida", lista_comida, ventana)) 
boton_comida.pack(pady=10)

boton_comida_eliminar = ttk.Button(marco_comida, text="Eliminar producto", style='C.TButton', width=14, command=lambda: eliminar_producto("Comida", lista_comida)) 
boton_comida_eliminar.pack(pady=5)

boton_comida_editar = ttk.Button(marco_comida, text="Editar producto", style='C.TButton', width=14, command=lambda: editar_producto("Comida", lista_comida, ventana))
boton_comida_editar.pack(pady=5)

marco_bebidas = tk.Frame(marco_productos, bg="#D5D6D9", padx=10, pady=10)
marco_bebidas.grid(row=0, column=1)

label_bebidas = tk.Label(marco_bebidas, text="Bebidas", font=("Arial", 15))
label_bebidas.pack()

lista_bebidas = tk.Listbox(marco_bebidas, font=("Helvetica", 12), width=50, height=20)
lista_bebidas.pack()

boton_bebidas = ttk.Button(marco_bebidas, text="Agregar producto", style='C.TButton', width=14, command=lambda: agregar_producto("Bebidas", lista_bebidas, ventana))
boton_bebidas.pack(pady=10)

boton_bebidas_eliminar = ttk.Button(marco_bebidas, text="Eliminar producto", style='C.TButton', width=14, command=lambda: eliminar_producto("Bebidas", lista_bebidas))
boton_bebidas_eliminar.pack(pady=5)

boton_bebidas_editar = ttk.Button(marco_bebidas, text="Editar producto", style='C.TButton', width=14, command=lambda: editar_producto("Bebidas", lista_bebidas, ventana))
boton_bebidas_editar.pack(pady=5)

marco_higiene = tk.Frame(marco_productos, bg="#A1FB8E", padx=10, pady=10)
marco_higiene.grid(row=0, column=2)

label_higiene = tk.Label(marco_higiene, text="Higiene", font=("Arial", 15))
label_higiene.pack()

lista_higiene = tk.Listbox(marco_higiene, font=("Helvetica", 12), width=50, height=20)
lista_higiene.pack()

boton_higiene = ttk.Button(marco_higiene, text="Agregar producto", style='C.TButton', width=14, command=lambda: agregar_producto("Higiene", lista_higiene, ventana))
boton_higiene.pack(pady=10)

boton_higiene_eliminar = ttk.Button(marco_higiene, text="Eliminar producto", style='C.TButton', width=14, command=lambda: eliminar_producto("Higiene", lista_higiene))
boton_higiene_eliminar.pack(pady=5)

boton_higiene_editar = ttk.Button(marco_higiene, text="Editar producto", style='C.TButton', width=14, command=lambda: editar_producto("Higiene", lista_higiene, ventana))
boton_higiene_editar.pack(pady=5)


marco_acciones = tk.Frame(marco_productos)
marco_acciones.grid(row=1, column=0, columnspan=3)







# Función para resaltar el texto coincidente en la lista, BARRA DE BUSQUEDA
def resaltar_texto(event):
    texto_busqueda = search_bar.get().lower()
    
    # Restablecer el estilo de todos los elementos en la lista
    lista_comida.selection_clear(0, tk.END)
    lista_bebidas.selection_clear(0, tk.END)
    lista_higiene.selection_clear(0, tk.END)
    
    # Resaltar el texto coincidente en la lista de comida
    for i in range(lista_comida.size()):
        if texto_busqueda in lista_comida.get(i).lower():
            lista_comida.selection_set(i)
    
    # Resaltar el texto coincidente en la lista de bebidas
    for i in range(lista_bebidas.size()):
        if texto_busqueda in lista_bebidas.get(i).lower():
            lista_bebidas.selection_set(i)
    
    # Resaltar el texto coincidente en la lista de higiene
    for i in range(lista_higiene.size()):
        if texto_busqueda in lista_higiene.get(i).lower():
            lista_higiene.selection_set(i)

# Asociar la función resaltar_texto con el evento KeyRelease del Search Bar
search_bar.bind("<KeyRelease>", resaltar_texto)









# Función de confirmación de salida para el boton de salir
def confirmar_salida():
    if messagebox.askokcancel("Confirmar salida", "¿Está seguro de que desea salir?"):
        ventana.destroy()

# Botón de salida
boton_salida = ttk.Button(marco_acciones, text="Salir", style='C.TButton', width=14, command=confirmar_salida)
boton_salida.pack(side=tk.LEFT, padx=1, pady=1)















# Botón de realizar venta
boton_venta = ttk.Button(marco_acciones, text="Exportar a Excel", style='C.TButton', width=10, command=  lambda: exportar_ecxel())
boton_venta.pack(side=tk.LEFT, padx=10, pady=1)







# Mostrar los productos en las listas correspondientes
mostrar_productos_categoria("Comida", lista_comida)
mostrar_productos_categoria("Bebidas", lista_bebidas)
mostrar_productos_categoria("Higiene", lista_higiene)




def vender_producto(lista1, lista2, lista3, ventana):
    # Obtener el índice seleccionado de la tabla
    indice_comida = lista1.curselection()
    indice_bebidas = lista2.curselection()
    indice_higiene = lista3.curselection()
    
    
    
    
    if indice_comida:
        #print(type(indice_comida))  #retrorna una tupla
        # print(indice_comida)
        producto = lista1.get(indice_comida[0])
        nombre = producto.split()[0]
        
        
        
        
        
        
        # Crear una nueva ventana para mostrar los detalles del producto
        ventana_producto = tk.Toplevel(ventana)
        ventana_producto.title("Detalles del Producto")
        
        # Etiqueta para mostrar el nombre del producto
        etiqueta_producto = tk.Label(ventana_producto, text=f"Producto: {producto}", font=("Arial", 12))
        etiqueta_producto.pack(pady=10)
        
        # Etiqueta para solicitar la cantidad al usuario
        etiqueta_cantidad = tk.Label(ventana_producto, text="Selecciona una cantidad:", font=("Arial", 12))
        etiqueta_cantidad.pack(pady=10)
        
        # Campo de entrada para que el usuario ingrese la cantidad
        cantidad_entry = tk.Entry(ventana_producto, font=("Arial", 12))
        cantidad_entry.insert(tk.END, "1")
        cantidad_entry.pack()
        
        
        
        
        
        
        
        
        def realizar_venta(categoria, producto, lista_comida):
            
            
            cantidad = int(cantidad_entry.get())
            
            # Obtener el nombre de la categoría seleccionada
            nombre_categoria = str(categoria)
            
             # Mostrar un cuadro de diálogo para confirmar la venta
            respuesta = messagebox.askquestion("Confirmar venta", f"¿Deseas vender {cantidad} unidades del producto {producto}?")
            
            if respuesta == "yes":
                 if cantidad > 0:
            # Actualizar la cantidad en la base de datos
                    consulta_cantidad_actual = "SELECT cantidad FROM productos WHERE nombre = %s AND categoria = %s"
                    db.cursor.execute(consulta_cantidad_actual, (producto, nombre_categoria))
                    resultado = db.cursor.fetchone()
                    cantidad_actual = int(resultado[0] if resultado else 0)
                    
                    print(type(cantidad_actual))
                 else:
                    messagebox.showinfo("Invalido", "La cantidad no puede ser menor a cero")
                     
                     
                    
         
                    
        
             # Verificar que la cantidad ingresada no supere la cantidad actual del producto en la base de datos
            if cantidad <= cantidad_actual:
                # Actualizar la cantidad en la base de datos
                consulta_actualizar_cantidad = "UPDATE productos SET cantidad = cantidad - %s WHERE nombre = %s AND categoria = %s"
                db.cursor.execute(consulta_actualizar_cantidad, (cantidad, producto, nombre_categoria))
                db.connection.commit()
           
           
           
                mostrar_productos_categoria(categoria, lista_comida)
                # Mostrar un mensaje de éxito
                messagebox.showinfo("Venta realizada", "La venta se ha realizado correctamente.")

                ventana_producto.destroy()
                
            else:
                ventana_producto.destroy()
                messagebox.showinfo("Cantidad Superada", "No Cuentas con esta cantidad del producto.")
                
                
                
        
        
        
        
        
        
        
        
        # Botón para realizar la venta
        boton_vender = tk.Button(ventana_producto, text="Vender", command= lambda: realizar_venta("Comida", nombre, lista1), font=("Arial", 12))
        boton_vender.pack(pady=10)
    
        # Mostrar la ventana del producto
        ventana_producto.mainloop()

        
        
        
        
        
        
        
        
        
        
        
        
        
    elif indice_bebidas:
        # print(indice_bebidas)
        producto = lista2.get(indice_bebidas[0])
        nombre = producto.split()[0]
        
        
        
        
        # Crear una nueva ventana para mostrar los detalles del producto
        ventana_producto = tk.Toplevel(ventana)
        ventana_producto.title("Detalles del Producto")
        
        # Etiqueta para mostrar el nombre del producto
        etiqueta_producto = tk.Label(ventana_producto, text=f"Producto: {producto}", font=("Arial", 12))
        etiqueta_producto.pack(pady=10)
        
        # Etiqueta para solicitar la cantidad al usuario
        etiqueta_cantidad = tk.Label(ventana_producto, text="Selecciona una cantidad:", font=("Arial", 12))
        etiqueta_cantidad.pack(pady=10)
        
        # Campo de entrada para que el usuario ingrese la cantidad
        cantidad_entry = tk.Entry(ventana_producto, font=("Arial", 12))
        cantidad_entry.insert(tk.END, "1")
        cantidad_entry.pack()
        
        
        def realizar_venta(categoria, producto, lista_bebidas):
            cantidad = int(cantidad_entry.get())
            
            # Obtener el nombre de la categoría seleccionada
            nombre_categoria = str(categoria)
            
             # Mostrar un cuadro de diálogo para confirmar la venta
            respuesta = messagebox.askquestion("Confirmar venta", f"¿Deseas vender {cantidad} unidades del producto {producto}?")
            
            if respuesta == "yes":
                 if cantidad > 0:
            # Actualizar la cantidad en la base de datos
                    consulta_cantidad_actual = "SELECT cantidad FROM productos WHERE nombre = %s AND categoria = %s"
                    db.cursor.execute(consulta_cantidad_actual, (producto, nombre_categoria))
                    resultado = db.cursor.fetchone()
                    cantidad_actual = int(resultado[0] if resultado else 0)
                    
                 else:
                    ventana_producto.destroy()
                    messagebox.showinfo("Invalido", "La cantidad no puede ser menor a cero")
                     
                     
                    
         
                    
        
             # Verificar que la cantidad ingresada no supere la cantidad actual del producto en la base de datos
            if cantidad <= cantidad_actual:
                # Actualizar la cantidad en la base de datos
                consulta_actualizar_cantidad = "UPDATE productos SET cantidad = cantidad - %s WHERE nombre = %s AND categoria = %s"
                db.cursor.execute(consulta_actualizar_cantidad, (cantidad, producto, nombre_categoria))
                db.connection.commit()
           
           
           
                mostrar_productos_categoria(categoria, lista_bebidas)
                # Mostrar un mensaje de éxito
                messagebox.showinfo("Venta realizada", "La venta se ha realizado correctamente.")

                ventana_producto.destroy()
                
            else:
                ventana_producto.destroy()
                messagebox.showinfo("Cantidad Superada", "No Cuentas con esta cantidad del producto.")
                
                
        
        
        
        # Botón para realizar la venta
        boton_vender = tk.Button(ventana_producto, text="Vender", command= lambda: realizar_venta("Bebidas", nombre, lista2), font=("Arial", 12))
        boton_vender.pack(pady=10)
    
        # Mostrar la ventana del producto
        ventana_producto.mainloop()
        
        
        
        
        
        
        
        
        
        
    elif indice_higiene:
        # print(indice_higiene)
    
        
        producto = lista3.get(indice_higiene[0])
        nombre = producto.split()[0]
        
        
        
        # Crear una nueva ventana para mostrar los detalles del producto
        ventana_producto = tk.Toplevel(ventana)
        ventana_producto.title("Detalles del Producto")
        
        # Etiqueta para mostrar el nombre del producto
        etiqueta_producto = tk.Label(ventana_producto, text=f"Producto: {producto}", font=("Arial", 12))
        etiqueta_producto.pack(pady=10)
        
        # Etiqueta para solicitar la cantidad al usuario
        etiqueta_cantidad = tk.Label(ventana_producto, text="Selecciona una cantidad:", font=("Arial", 12))
        etiqueta_cantidad.pack(pady=10)
        
        # Campo de entrada para que el usuario ingrese la cantidad
        cantidad_entry = tk.Entry(ventana_producto, font=("Arial", 12))
        cantidad_entry.insert(tk.END, "1")
        cantidad_entry.pack()
        
        
        
        
        def realizar_venta(categoria, producto, lista_higiene):
            
           cantidad = int(cantidad_entry.get())
            
            # Obtener el nombre de la categoría seleccionada
           nombre_categoria = str(categoria)
            
             # Mostrar un cuadro de diálogo para confirmar la venta
           respuesta = messagebox.askquestion("Confirmar venta", f"¿Deseas vender {cantidad} unidades del producto {producto}?")
            
           if respuesta == "yes":
                 if cantidad > 0:
            # Actualizar la cantidad en la base de datos
                    consulta_cantidad_actual = "SELECT cantidad FROM productos WHERE nombre = %s AND categoria = %s"
                    db.cursor.execute(consulta_cantidad_actual, (producto, nombre_categoria))
                    resultado = db.cursor.fetchone()
                    cantidad_actual = int(resultado[0] if resultado else 0)
                    
                 else:
                    ventana_producto.destroy()
                     
                    messagebox.showinfo("Invalido", "La cantidad no puede ser menor a cero")
                     
                     
                    
         
                    
        
             # Verificar que la cantidad ingresada no supere la cantidad actual del producto en la base de datos
           if cantidad <= cantidad_actual:
                # Actualizar la cantidad en la base de datos
                consulta_actualizar_cantidad = "UPDATE productos SET cantidad = cantidad - %s WHERE nombre = %s AND categoria = %s"
                db.cursor.execute(consulta_actualizar_cantidad, (cantidad, producto, nombre_categoria))
                db.connection.commit()
           
           
           
                mostrar_productos_categoria(categoria, lista_higiene)
                # Mostrar un mensaje de éxito
                messagebox.showinfo("Venta realizada", "La venta se ha realizado correctamente.")

                ventana_producto.destroy()
                
           else:
                ventana_producto.destroy()
               
                messagebox.showinfo("Cantidad Superada", "No Cuentas con esta cantidad del producto.")
                
                
        
            
            
        
        
        # Botón para realizar la venta
        boton_vender = tk.Button(ventana_producto, text="Vender", command= lambda: realizar_venta("Higiene", nombre, lista3), font=("Arial", 12))
        boton_vender.pack(pady=10)
    
        # Mostrar la ventana del producto
        ventana_producto.mainloop()
       
       
       
       
       
       
       
       
       
        
    else:
                
        # Mostrar un mensaje de error si no se selecciona ningún producto
        messagebox.showerror("Error de selección", "Por favor, seleccione un producto antes de realizar la venta.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Asociar la función vender_producto con el botón de vender, estos son los parametros que debemos hacer dinamicos
boton_vender = ttk.Button(marco_acciones, text="Vender", width=13, style='C.TButton', command=lambda: vender_producto(lista_comida, lista_bebidas, lista_higiene, ventana))
boton_vender.pack(side=tk.LEFT, padx=20, pady=10)

# Mostrar los botones "Realizar venta" y "Salir" separados
boton_venta.pack(side=tk.LEFT, padx=520)
boton_salida.pack(side=tk.LEFT, padx=20)















# Esta Funcion solo muestra la ventana Modal para vender producto
def mostrar_ventana_producto(producto):
    ventana_producto = tk.Toplevel(ventana)
    ventana_producto.title("Detalles del Producto")
    
    # Etiqueta para solicitar la cantidad al usuario
    etiqueta_cantidad = tk.Label(ventana_producto, text="Selecciona una cantidad:", font=("Arial", 12))
    etiqueta_cantidad.pack(pady=10)
    
    # Campo de entrada para que el usuario ingrese la cantidad
    cantidad_entry = tk.Entry(ventana_producto, font=("Arial", 12))
    cantidad_entry.pack()
    
    
    
    
    
    
    
    
    
    
    # Función para agregar la cantidad del producto, POSTERIOR
# def mostrar_ventana_producto(categoria, producto):
    # Crear una nueva ventana para mostrar los detalles del producto
    ventana_producto = tk.Toplevel(ventana)
    ventana_producto.title("Detalles del Producto")
    
    # Etiqueta para mostrar el nombre del producto
    etiqueta_producto = tk.Label(ventana_producto, text=f"Producto: {producto}", font=("Arial", 12))
    etiqueta_producto.pack(pady=10)
    
    # Etiqueta para solicitar la cantidad al usuario
    etiqueta_cantidad = tk.Label(ventana_producto, text="Selecciona una cantidad:", font=("Arial", 12))
    etiqueta_cantidad.pack(pady=10)
    
    # Campo de entrada para que el usuario ingrese la cantidad
    cantidad_entry = tk.Entry(ventana_producto, font=("Arial", 12))
    cantidad_entry.insert(tk.END, "1")
    cantidad_entry.pack()
    
    # Botón para realizar la venta
    boton_vender = tk.Button(ventana_producto, text="Vender", command=lambda: realizar_venta(categoria, producto, cantidad_entry, ventana_producto), font=("Arial", 12))
    boton_vender.pack(pady=10)
    
    # Mostrar la ventana del producto
    ventana_producto.mainloop()











# Función para manejar el doble clic en un producto
def triple_clic_producto(event):
    # Obtener el nombre del producto seleccionado
    indice_seleccionado = lista_comida.curselection() or lista_bebidas.curselection() or lista_higiene.curselection()
    if indice_seleccionado and event.num == 3:  # Verificar que se haya hecho triple clic
        producto = None
        if lista_comida.curselection():
            producto = lista_comida.get(indice_seleccionado[0])
        elif lista_bebidas.curselection():
            producto = lista_bebidas.get(indice_seleccionado[0])
        elif lista_higiene.curselection():
            producto = lista_higiene.get(indice_seleccionado[0])
        
        # Mostrar la ventana del producto seleccionado
        mostrar_ventana_producto(producto)

# Asociar la función triple_clic_producto con el evento <<ListboxTriple>> de las listas
lista_comida.bind("<<ListboxTriple>>", triple_clic_producto)
lista_bebidas.bind("<<ListboxTriple>>", triple_clic_producto)
lista_higiene.bind("<<ListboxTriple>>", triple_clic_producto)



ventana.mainloop()