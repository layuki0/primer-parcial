#Este es una venta de conciertos
print("Este es tiketmater para el concierto de Guns and Roses")

tipo_boleto = int(input ("¿Que tipo de boleto quieres? (1. General, 2. VIP) "))

if tipo_boleto == 1:
    print("El costo sera de $1500")
    a=1500
elif tipo_boleto == 2:
    print("El costo sera de $6500")
    a=6500
else:
    print("Opcion no valida")


cantidad = int(input("¿Cuantos boletos quieres comprar? "))

if tipo_boleto == 1:
        print("Los asientos disponibles son de la fila a,b,c,d,e,f,g,h,i,j")
        b = input("¿Que asiento deseas? (a1.a2.a3.a4.a5.a6.a7.a8.a9.a10.b1.b2.b3.b4.b5.b6.b7.b8.b9.b10.c1.c2.c3.c4.c5.c6.c7.c8.c9.c10.d1.d2.d3.d4.d5.d6.d7.d8.d9.d10....) ")
elif tipo_boleto == 2:
    print("Los asientos disponibles son de la fila k,l,m,n,o,p")
    b = input("¿Que asiento deseas? (k1.k2.k3.k4.k5.k6.k7.k8.k9.k10.l1.l2.l3.l4.l5.l6.l7.l8.l9.l10.m1.m2.m3.m4.m5.m6.m7.m8.m9.m10.n1.n2.n3.n4.n5.n6.n7.n8.n9.n10.o1.o2.o3.o4.o5.o6.o7.o8.o9.o10.p1.p2.p3.p4.p5.p6.p7.p8.p9.p10) ")

total = a*cantidad

print("El total a pagar es: $" + str(total))

if total > 10000:
    print("se te realizara un descuento del 15%")
    total = total - (total * 0.15)
    print("El total a pagar con descuento es: $" + str(total))
elif total > 20000:
    print("se te realizara un descuento del 30%")
    total = total - (total * 0.30)
    print("El total a pagar con descuento es: $" + str(total))
print("Su asiento es " +b,"el costo total sera: $" + str(total),"y su tipo de boleto es "+ str(tipo_boleto),"que disfrute el concierto")
