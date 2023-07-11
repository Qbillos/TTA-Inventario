import tkinter as tk
from tkinter import messagebox


def confirmar_salida():
    confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas salir?")
    if confirmacion:
        ventana_principal.destroy()


def abrir_ventana_registro():
    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("400x300")
    ventana_registro.config(bg="white", bd=10, relief="solid")

    label_nombre = tk.Label(ventana_registro, text="Nombre:", font=("Arial", 12), bg="white")
    label_nombre.pack(pady=5)
    entrada_nombre = tk.Entry(ventana_registro, font=("Arial", 12))
    entrada_nombre.pack()

    label_apellido = tk.Label(ventana_registro, text="Apellido:", font=("Arial", 12), bg="white")
    label_apellido.pack(pady=5)
    entrada_apellido = tk.Entry(ventana_registro, font=("Arial", 12))
    entrada_apellido.pack()

    label_correo = tk.Label(ventana_registro, text="Correo electrónico:", font=("Arial", 12), bg="white")
    label_correo.pack(pady=5)
    entrada_correo = tk.Entry(ventana_registro, font=("Arial", 12))
    entrada_correo.pack()

    label_contrasena = tk.Label(ventana_registro, text="Contraseña:", font=("Arial", 12), bg="white")
    label_contrasena.pack(pady=5)
    entrada_contrasena = tk.Entry(ventana_registro, show="*", font=("Arial", 12))
    entrada_contrasena.pack()

    boton_registrar = tk.Button(ventana_registro, text="Registrar", font=("Arial", 12))
    boton_registrar.pack(pady=10)


ventana_principal = tk.Tk()
ventana_principal.title("Bienvenido")
ventana_principal.geometry("600x400")
ventana_principal.config(bg="white")

# Estilo de los elementos
estilo_label = {"font": ("Arial", 14), "bg": "white"}
estilo_entry = {"font": ("Arial", 12)}
estilo_boton = {"font": ("Arial", 12), "width": 20}

# Marco de color alrededor de la interfaz
marco_color = "#262D3F"
ventana_principal.configure(bg=marco_color)
marco = tk.Frame(ventana_principal, bg="white", bd=2, relief="solid")  # Cambio en el grosor del marco
marco.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

label_bienvenida = tk.Label(marco, text="¡Bienvenido!", **estilo_label)
label_bienvenida.pack(pady=20)

label_correo = tk.Label(marco, text="Correo electrónico:", **estilo_label)
label_correo.pack(pady=5)
entrada_correo = tk.Entry(marco, **estilo_entry)
entrada_correo.pack()

label_contrasena = tk.Label(marco, text="Contraseña:", **estilo_label)
label_contrasena.pack(pady=5)
entrada_contrasena = tk.Entry(marco, show="*", **estilo_entry)
entrada_contrasena.pack()

boton_iniciar_sesion = tk.Button(marco, text="Iniciar sesión", **estilo_boton)
boton_iniciar_sesion.pack(pady=10)

boton_registrarse = tk.Button(marco, text="Registrarse", command=abrir_ventana_registro, **estilo_boton)
boton_registrarse.pack(pady=10)

ventana_principal.protocol("WM_DELETE_WINDOW", confirmar_salida)
ventana_principal.mainloop()
