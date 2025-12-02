import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Datos base
DEPORTES = ["gimnasia", "tenis", "box"]

CONTENIDO = {
    "gimnasia": {
        "historia": (
            "La gimnasia tiene sus orígenes en la antigua Grecia, practicada para fuerza, "
            "agilidad y belleza corporal. En el siglo XIX, Alemania y Suecia estructuraron "
            "sistemas con aparatos. La gimnasia moderna se consolidó en el siglo XX con la FIG "
            "y su inclusión en los Juegos Olímpicos."
        ),
        "deportistas": {
            "Simone Biles": "Gimnasta más condecorada; revolucionó la dificultad y el control.",
            "Nadia Comaneci": "Primera en lograr un 10 perfecto en Juegos Olímpicos (1976).",
            "Larisa Latynina": "Dominó los 50s-60s; récord de medallas durante décadas.",
        },
        "juegos recientes": (
            "París 2024: Simone Biles oro, Rebeca Andrade plata y Sunisa Lee bronce."
        ),
        "apuestas": {
            "minimo": 1000,
            "opciones": ["Simon", "Kohei"],
            "etiqueta": "Equipos en competencia",
        },
    },
    "tenis": {
        "historia": (
            "El tenis moderno nació en Inglaterra en el siglo XIX, con raíces en el 'jeu de paume'. "
            "Primer Wimbledon en 1877. Grand Slams: Wimbledon, Roland Garros, US Open y Australia."
        ),
        "deportistas": {
            "Roger Federer": "Elegancia y técnica; 20 Grand Slams.",
            "Rafael Nadal": "Rey de la Tierra Batida; 22 Grand Slams.",
            "Novak Djokovic": "Fortaleza mental y física; más títulos de Grand Slam.",
        },
        "juegos recientes": (
            "US Open 2024: Djokovic campeón tras final intensa contra Carlos Alcaraz."
        ),
        "apuestas": {
            "minimo": 1000,
            "opciones": ["Djokovic", "Alcaraz"],
            "etiqueta": "Jugadores en competencia",
        },
    },
    "box": {
        "historia": (
            "Raíces en Grecia y Roma; forma moderna en Inglaterra s. XVIII. Reglas de Queensberry (1867) "
            "introdujeron guantes y asaltos. Hoy es global: fuerza, estrategia y superación."
        ),
        "deportistas": {
            "Muhammad Ali": "El más grande: técnica, velocidad y activismo.",
            "Mike Tyson": "Campeón más joven de pesos pesados; era marcada por su fuerza.",
            "Canelo Álvarez": "Mexicano más exitoso actual; campeón en múltiples categorías.",
        },
        "peleas recientes": (
            "2024: Canelo Álvarez vs David Benavídez; Canelo retuvo título unificado por decisión unánime."
        ),
        "apuestas": {
            "minimo": 1000,
            "opciones": ["Canelo", "Benavidez"],
            "etiqueta": "Boxeadores en competencia",
        },
    },
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Deportes y Apuestas")
        self.geometry("720x520")
        self.resizable(False, False)

        # Estado
        self.deporte_actual = tk.StringVar(value=DEPORTES[0])
        self.seccion_actual = tk.StringVar(value="historia")
        self.dinero = 0
        self.apuestas_activas = []

        # Layout principal
        self._build_header()
        self._build_controls()
        self._build_display()
        self._update_display()

    def _build_header(self):
        header = tk.Frame(self, padx=10, pady=10)
        header.pack(fill="x")
        tk.Label(header, text="Elige un deporte:", font=("Segoe UI", 12, "bold")).pack(side="left")

        deporte_menu = ttk.OptionMenu(header, self.deporte_actual, self.deporte_actual.get(), *DEPORTES, command=lambda _: self._update_sections())
        deporte_menu.pack(side="left", padx=8)

        tk.Button(header, text="Reiniciar apuestas", command=self._reset_apuestas).pack(side="right", padx=8)

    def _build_controls(self):
        controls = tk.Frame(self, padx=10, pady=10)
        controls.pack(fill="x")

        tk.Label(controls, text="¿Qué quieres conocer?", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w")

        self.sections_menu = ttk.OptionMenu(controls, self.seccion_actual, self.seccion_actual.get(), "historia")
        self.sections_menu.grid(row=0, column=1, padx=8, sticky="w")

        tk.Button(controls, text="Mostrar", command=self._update_display).grid(row=0, column=2, padx=8)

        # Botones de acción
        self.btn_deportistas = tk.Button(controls, text="Ver deportistas", command=self._mostrar_deportistas)
        self.btn_deportistas.grid(row=1, column=0, pady=10, sticky="w")

        self.btn_eventos = tk.Button(controls, text="Ver eventos recientes", command=self._mostrar_eventos)
        self.btn_eventos.grid(row=1, column=1, pady=10, sticky="w")

        self.btn_apuestas = tk.Button(controls, text="Abrir apuestas", command=self._abrir_apuestas)
        self.btn_apuestas.grid(row=1, column=2, pady=10, sticky="w")

    def _build_display(self):
        display = tk.Frame(self, padx=10, pady=10)
        display.pack(fill="both", expand=True)

        self.text = tk.Text(display, wrap="word", font=("Segoe UI", 11))
        self.text.pack(fill="both", expand=True)

    # Helpers
    def _update_sections(self):
        deporte = self.deporte_actual.get()
        secciones = ["historia"]
        if "deportistas" in CONTENIDO[deporte]:
            secciones.append("deportistas")
        if "juegos recientes" in CONTENIDO[deporte]:
            secciones.append("juegos recientes")
        if "peleas recientes" in CONTENIDO[deporte]:
            secciones.append("peleas recientes")
        secciones.append("apuestas")

        # Actualiza menú de secciones
        menu = self.sections_menu["menu"]
        menu.delete(0, "end")
        for sec in secciones:
            menu.add_command(label=sec, command=lambda s=sec: self.seccion_actual.set(s))
        self.seccion_actual.set(secciones[0])
        self._update_display()

    def _update_display(self):
        self.text.delete("1.0", "end")
        deporte = self.deporte_actual.get()
        seccion = self.seccion_actual.get()

        data = CONTENIDO[deporte]
        if seccion in ("historia", "juegos recientes", "peleas recientes"):
            self.text.insert("end", f"{seccion.title()} - {deporte.title()}\n\n")
            self.text.insert("end", data.get(seccion, "Sin información"))
        elif seccion == "deportistas":
            self.text.insert("end", f"Deportistas destacados - {deporte.title()}\n\n")
            for nombre, desc in data["deportistas"].items():
                self.text.insert("end", f"- {nombre}: {desc}\n")
        elif seccion == "apuestas":
            ap = data["apuestas"]
            self.text.insert("end", f"Sistema de apuestas - {deporte.title()}\n\n")
            self.text.insert("end", f"Mínimo para participar: {ap['minimo']}\n")
            self.text.insert("end", f"{ap['etiqueta']}: {', '.join(ap['opciones'])}\n")
            self.text.insert("end", "\nUsa el botón 'Abrir apuestas' para jugar con saldo simulado.")

    # Ventanas secundarias
    def _mostrar_deportistas(self):
        deporte = self.deporte_actual.get()
        if "deportistas" not in CONTENIDO[deporte]:
            messagebox.showinfo("Info", "Este deporte no tiene lista de deportistas.")
            return
        nombres = list(CONTENIDO[deporte]["deportistas"].keys())
        nombre = simpledialog.askstring("Deportistas", f"Escoge un deportista:\n{', '.join(nombres)}")
        if not nombre:
            return
        # Normaliza capitalización
        match = None
        for n in nombres:
            if n.lower() == nombre.strip().lower():
                match = n
                break
        if match:
            desc = CONTENIDO[deporte]["deportistas"][match]
            messagebox.showinfo(match, desc)
        else:
            messagebox.showwarning("No encontrado", "No hay información para ese nombre.")

    def _mostrar_eventos(self):
        deporte = self.deporte_actual.get()
        key = "juegos recientes" if "juegos recientes" in CONTENIDO[deporte] else "peleas recientes"
        if key in CONTENIDO[deporte]:
            messagebox.showinfo("Eventos recientes", CONTENIDO[deporte][key])
        else:
            messagebox.showinfo("Eventos recientes", "Sin información disponible.")

    def _abrir_apuestas(self):
        deporte = self.deporte_actual.get()
        ap = CONTENIDO[deporte]["apuestas"]
        minimo = ap["minimo"]
        opciones = ap["opciones"]

        try:
            deal = simpledialog.askinteger("Apuestas", "¿Cuánto dinero vas a apostar hoy?")
        except Exception:
            deal = None

        if not deal:
            return

        if deal < minimo:
            messagebox.showwarning("Mínimo no cumplido", f"Gracias, pero el mínimo es {minimo}.")
            return

        self.dinero = deal
        self.apuestas_activas = opciones.copy()
        self._ventana_apuestas(opciones)

    def _ventana_apuestas(self, opciones):
        win = tk.Toplevel(self)
        win.title("Apuestas")
        win.geometry("520x420")
        win.resizable(False, False)

        saldo_var = tk.StringVar(value=f"Tienes {self.dinero} monedas.")
        tk.Label(win, textvariable=saldo_var, font=("Segoe UI", 11, "bold")).pack(pady=8)
        tk.Label(win, text=f"En competencia: {', '.join(opciones)}").pack()

        eleccion_var = tk.StringVar(value=opciones[0])
        ttk.OptionMenu(win, eleccion_var, eleccion_var.get(), *opciones).pack(pady=6)

        apuesta_entry = ttk.Entry(win)
        apuesta_entry.pack(pady=6)
        apuesta_entry.insert(0, "100")

        resultado_var = tk.StringVar(value="Esperando apuesta...")
        tk.Label(win, textvariable=resultado_var, fg="blue").pack(pady=8)

        def jugar():
            nonlocal opciones
            try:
                apuesta = int(apuesta_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Cantidad no válida.")
                return
            if apuesta <= 0 or apuesta > self.dinero:
                messagebox.showerror("Error", "Cantidad no válida.")
                return

            ganador = random.choice(opciones)
            elegido = eleccion_var.get()
            if elegido == ganador:
                self.dinero += apuesta
                resultado_var.set(f"Ganaste {apuesta} monedas. Ganador: {ganador}")
            else:
                self.dinero -= apuesta
                resultado_var.set(f"Perdiste {apuesta} monedas. Ganador: {ganador}")
            saldo_var.set(f"Tienes {self.dinero} monedas.")

            if self.dinero <= 0:
                messagebox.showinfo("Fin", "Te has quedado sin dinero. Fin del juego.")
                win.destroy()

        def salir():
            messagebox.showinfo("Gracias", "Gracias por jugar. ¡Vuelve pronto!")
            win.destroy()

        btn_frame = tk.Frame(win)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Apostar", command=jugar).grid(row=0, column=0, padx=8)
        tk.Button(btn_frame, text="Salir", command=salir).grid(row=0, column=1, padx=8)

    def _reset_apuestas(self):
        self.dinero = 0
        self.apuestas_activas = []
        messagebox.showinfo("Reinicio", "Se reinició el estado de apuestas.")

if __name__ == "__main__":
    app = App()
    app._update_sections()
    app.mainloop()
