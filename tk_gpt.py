import tkinter as tk

# Define la función que se ejecutará cuando se haga clic en el botón "Ingresar"


def ingresar():
    # Obtiene los valores ingresados por el usuario
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Cierra la ventana de inicio de sesión y muestra el resultado en la terminal
    print(usuario)
    print(contrasena)
    root.destroy()


# Crea la ventana de inicio de sesión
root = tk.Tk()
root.title("Inicio de sesión")

# Crea los widgets necesarios en la ventana de inicio de sesión
label_usuario = tk.Label(root, text="Usuario:")
label_contrasena = tk.Label(root, text="Contraseña:")
entry_usuario = tk.Entry(root)
entry_contrasena = tk.Entry(root, show="*")
button_ingresar = tk.Button(root, text="Ingresar", command=ingresar)
label_error = tk.Label(root, text="", fg="red")

# Coloca los widgets en la ventana
label_usuario.grid(row=0, column=0)
label_contrasena.grid(row=1, column=0)
entry_usuario.grid(row=0, column=1)
entry_contrasena.grid(row=1, column=1)
button_ingresar.grid(row=2, column=1)
label_error.grid(row=3, column=1)

# Ejecuta el bucle principal de la ventana
root.mainloop()
