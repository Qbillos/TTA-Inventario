import mysql.connector
from tkinter import *

def iniciar_sesion():
    username = entry_username.get()
    password = entry_password.get()

    # Conectarse a la base de datos
    cnx = mysql.connector.connect(user='tu_usuario', password='tu_contraseña', host='localhost', database='nombre_de_tu_base_de_datos')
    cursor = cnx.cursor()

    # Verificar las credenciales en la base de datos
    query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        lbl_status.config(text="Inicio de sesión exitoso")
    else:
        lbl_status.config(text="Inicio de sesión fallido")

    cnx.close()

def registrar():
    username = entry_username.get()
    password = entry_password.get()

    # Conectarse a la base de datos
    cnx = mysql.connector.connect(user='tu_usuario', password='tu_contraseña', host='localhost', database='nombre_de_tu_base_de_datos')
    cursor = cnx.cursor()

    # Insertar el nuevo usuario en la base de datos
    query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    cnx.commit()

    lbl_status.config(text="Registro exitoso")

    cnx.close()

# Crear la ventana principal
ventana = Tk()
ventana.title("Login y Registro")

# Crear los widgets
lbl_username = Label(ventana, text="Usuario:")
lbl_username.pack()
entry_username = Entry(ventana)
entry_username.pack()

lbl_password = Label(ventana, text="Contraseña:")
lbl_password.pack()
entry_password = Entry(ventana, show="*")
entry_password.pack()

btn_login = Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
btn_login.pack()

btn_register = Button(ventana, text="Registrarse", command=registrar)
btn_register.pack()

lbl_status = Label(ventana, text="")
lbl_status.pack()

# Ejecutar la ventana
ventana.mainloop()