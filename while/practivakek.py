#calificaciones 
alumnos =["jorge","cami","edgar","quezada"]
while True:
    for alumno in alumnos:
        print(f"el alumno es: {alumno}")
        if alumno == "jorge":
            mate=float(input("calificacion mate: "))
            historia=float(input("calificacion historia: "))
            español=float(input("calificacion español: "))
            idiomas=float(input("calificacion idiomas: "))
            quimica=float(input("calificacion quimica: "))
            fisica=float(input("calificacion fisica: "))
            pensamiento=float(input("calificacion pensamiento: "))
            promedio=(mate+historia+español+idiomas+quimica+fisica+pensamiento)/7
            print(f"el promedio de {alumno} es: {promedio}")
        elif alumno == "cami":
            mate=float(input("calificacion mate: "))
            historia=float(input("calificacion historia: "))
            español=float(input("calificacion español: "))
            idiomas=float(input("calificacion idiomas: "))
            quimica=float(input("calificacion quimica: "))
            fisica=float(input("calificacion fisica: "))
            pensamiento=float(input("calificacion pensamiento: "))
            promedio=(mate+historia+español+idiomas+quimica+fisica+pensamiento)/7
            print(f"el promedio de {alumno} es: {promedio}")
        elif alumno == "edgar":
            mate=float(input("calificacion mate: "))
            historia=float(input("calificacion historia: "))
            español=float(input("calificacion español: "))
            idiomas=float(input("calificacion idiomas: "))
            quimica=float(input("calificacion quimica: "))
            fisica=float(input("calificacion fisica: "))
            pensamiento=float(input("calificacion pensamiento: "))
            promedio=(mate+historia+español+idiomas+quimica+fisica+pensamiento)/7
            print(f"el promedio de {alumno} es: {promedio}")
        elif alumno == "quezada":
            mate=float(input("calificacion mate: "))
            historia=float(input("calificacion historia: "))
            español=float(input("calificacion español: "))
            idiomas=float(input("calificacion idiomas: "))
            quimica=float(input("calificacion quimica: "))
            fisica=float(input("calificacion fisica: "))
            pensamiento=float(input("calificacion pensamiento: "))
            promedio=(mate+historia+español+idiomas+quimica+fisica+pensamiento)/7
            print(f"el promedio de {alumno} es: {promedio}")
    break
def encontrar_mayor(promedio):
    return max(promedio)
mayor=encontrar_mayor([promedio])
print(f"el mayor promedio es: {mayor} y le pertenece a {alumno}")
