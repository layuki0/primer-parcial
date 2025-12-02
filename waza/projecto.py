import tkinter as tk
from tkinter import messagebox

def registrar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    genero = genero_var.get()
    deporte = entry_deporte.get()
    nivel = nivel_var.get()
    peso = float(entry_peso.get())
    estatura = float(entry_estatura.get())
    capacidad = float(entry_capacidad.get())

    # Cálculos
    IMC = peso / (estatura ** 2)
    fuerza_relativa = peso / IMC
    capacidad_aerobica = (220 - int(edad)) + peso

    # Mostrar resultados
    resultados = (
        f"Nombre: {nombre}\n"
        f"Edad: {edad}\n"
        f"Género: {genero}\n"
        f"Deporte: {deporte}\n"
        f"Nivel: {nivel}\n\n"
        f"IMC: {IMC:.2f}\n"
        f"Fuerza relativa: {fuerza_relativa:.2f}\n"
        f"Capacidad aeróbica estimada: {capacidad_aerobica:.2f}"
    )
    messagebox.showinfo("Resultados del registro", resultados)

# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Deportistas")

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0, sticky="w")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text="Género:").grid(row=2, column=0, sticky="w")
genero_var = tk.StringVar(value="masculino")
tk.OptionMenu(ventana, genero_var, "masculino", "femenino", "no binario").grid(row=2, column=1)

tk.Label(ventana, text="Deporte:").grid(row=3, column=0, sticky="w")
entry_deporte = tk.Entry(ventana)
entry_deporte.grid(row=3, column=1)

tk.Label(ventana, text="Nivel:").grid(row=4, column=0, sticky="w")
nivel_var = tk.StringVar(value="principiante")
tk.OptionMenu(ventana, nivel_var, "principiante", "intermedio", "avanzado").grid(row=4, column=1)

tk.Label(ventana, text="Peso (kg):").grid(row=5, column=0, sticky="w")
entry_peso = tk.Entry(ventana)
entry_peso.grid(row=5, column=1)

tk.Label(ventana, text="Estatura (m):").grid(row=6, column=0, sticky="w")
entry_estatura = tk.Entry(ventana)
entry_estatura.grid(row=6, column=1)

tk.Label(ventana, text="Peso levantado (kg):").grid(row=7, column=0, sticky="w")
entry_capacidad = tk.Entry(ventana)
entry_capacidad.grid(row=7, column=1)

# Botón de registro
tk.Button(ventana, text="Registrar", command=registrar).grid(row=8, column=0, columnspan=2, pady=10)

ventana.mainloop()

import tkinter as tk
from tkinter import messagebox

def registrar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    genero = genero_var.get()
    deporte = entry_deporte.get()
    nivel = nivel_var.get()
    peso = float(entry_peso.get())
    estatura = float(entry_estatura.get())
    capacidad = float(entry_capacidad.get())

    # Cálculos
    IMC = peso / (estatura ** 2)
    fuerza_relativa = peso / IMC
    capacidad_aerobica = (220 - int(edad)) + peso

    # Mostrar resultados
    resultados = (
        f"Nombre: {nombre}\n"
        f"Edad: {edad}\n"
        f"Género: {genero}\n"
        f"Deporte: {deporte}\n"
        f"Nivel: {nivel}\n\n"
        f"IMC: {IMC:.2f}\n"
        f"Fuerza relativa: {fuerza_relativa:.2f}\n"
        f"Capacidad aeróbica estimada: {capacidad_aerobica:.2f}"
    )
    messagebox.showinfo("Resultados del registro", resultados)

# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Deportistas")

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0, sticky="w")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text="Género:").grid(row=2, column=0, sticky="w")
genero_var = tk.StringVar(value="masculino")
tk.OptionMenu(ventana, genero_var, "masculino", "femenino", "no binario").grid(row=2, column=1)

tk.Label(ventana, text="Deporte:").grid(row=3, column=0, sticky="w")
entry_deporte = tk.Entry(ventana)
entry_deporte.grid(row=3, column=1)

tk.Label(ventana, text="Nivel:").grid(row=4, column=0, sticky="w")
nivel_var = tk.StringVar(value="principiante")
tk.OptionMenu(ventana, nivel_var, "principiante", "intermedio", "avanzado").grid(row=4, column=1)

tk.Label(ventana, text="Peso (kg):").grid(row=5, column=0, sticky="w")
entry_peso = tk.Entry(ventana)
entry_peso.grid(row=5, column=1)

tk.Label(ventana, text="Estatura (m):").grid(row=6, column=0, sticky="w")
entry_estatura = tk.Entry(ventana)
entry_estatura.grid(row=6, column=1)

tk.Label(ventana, text="Peso levantado (kg):").grid(row=7, column=0, sticky="w")
entry_capacidad = tk.Entry(ventana)
entry_capacidad.grid(row=7, column=1)

# Botón de registro
tk.Button(ventana, text="Registrar", command=registrar).grid(row=8, column=0, columnspan=2, pady=10)

ventana.mainloop()