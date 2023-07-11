import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()
    role = var_role.get()

    if role == 1:  # Administrador
        # Aquí puedes realizar la lógica de autenticación para el administrador
        if username == "admin" and password == "admin":
            print("Inicio de sesión exitoso como administrador")
        else:
            print("Credenciales incorrectas para el administrador")
    elif role == 2:  # Usuario
        # Aquí puedes realizar la lógica de autenticación para el usuario
        if username == "user" and password == "user":
            print("Inicio de sesión exitoso como usuario")
        else:
            print("Credenciales incorrectas 2para el usuario")

def register():
    register_window = tk.Toplevel(ventana)
    register_window.title("Registro")
    register_window.geometry("300x200")

    label_register = tk.Label(register_window, text="Registro de usuario", font=("Arial", 16))
    label_register.pack(pady=10)

    # Campos de registro con datos predeterminados
    label_nombre = tk.Label(register_window, text="Nombre:", font=("Arial", 12))
    label_nombre.pack()
    entry_nombre = tk.Entry(register_window, font=("Arial", 12))
    entry_nombre.insert(tk.END, "John Doe")  # Nombre predeterminado
    entry_nombre.pack()

    label_email = tk.Label(register_window, text="Email:", font=("Arial", 12))
    label_email.pack()
    entry_email = tk.Entry(register_window, font=("Arial", 12))
    entry_email.insert(tk.END, "johndoe@example.com")  # Email predeterminado
    entry_email.pack()
                        
    label_password = tk.Label(register_window, text="Contraseña:", font=("Arial", 12))
    label_password.pack()
    entry_password = tk.Entry(register_window, show="*", font=("Arial", 12))
    entry_password.pack()

    btn_register = tk.Button(register_window, text="Registrar", font=("Arial", 12))
    btn_register.pack(pady=10)

# Aquí definimos la pantalla de inicio de sesión

ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("300x300")

label_bienvenido = tk.Label(ventana, text="Bienvenido a Staycom", font=("Arial", 32))
label_bienvenido.pack(pady=10)

label_username = tk.Label(ventana, text="Nombre de usuario:", font=("Arial", 16))
label_username.pack(pady=10)
entry_username = tk.Entry(ventana, font=("Arial", 16))
entry_username.pack()

label_password = tk.Label(ventana, text="Contraseña:", font=("Arial", 16))
label_password.pack(pady=10)
entry_password = tk.Entry(ventana, show="*", font=("Arial", 16))
entry_password.pack()




label_role = tk.Label(ventana, text="Seleccione el rol:", font=("Arial", 16))
label_role.pack(pady=10)    

var_role = tk.IntVar(value=0)  # Valor por defecto para el rol de usuario

radio_admin = tk.Radiobutton(ventana, text="Administrador", variable=var_role, value=1, font=("Arial", 12))
radio_admin.pack()

radio_user = tk.Radiobutton(ventana, text="Usuario", variable=var_role, value=2, font=("Arial", 12))
radio_user.pack()

btn_login = tk.Button(ventana, text="Iniciar sesión", command=login, font=("Arial", 16))
btn_login.pack(pady=10)

btn_register = tk.Button(ventana, text="Registrarse", command=register, font=("Arial", 16))
btn_register.pack(pady=5)


ventana.mainloop()
