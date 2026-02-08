import random   
numero_aleatorio = random.randint(1,100)
cuentaIntentos = 1
ESC=chr(27)
estilo=0
color=37
fondo=44
print(f"{ESC}[{estilo};{color};{fondo}m ¡Bienvenido al juego para adivinar el número!{ESC}[0m", end="")
print("\N{smiling face with sunglasses}")
intentos=int(input("¿En cuántos intentos quieres adivinar el número? (No más de 10): "))
ESC=chr(27)
estilo=0
color=36
fondo=40
print(f"{ESC}[{estilo};{color};{fondo}m Estoy pensando en un número entre 1 y 100. ¿Puedes adivinarlo?{ESC}[0m", end="")
print("\N{thinking face}")
num=int(input("Adivina el número: "))
while num != numero_aleatorio and cuentaIntentos < intentos:
    cuentaIntentos += 1
    if num < numero_aleatorio:
        ESC=chr(27)
        estilo=0
        color=33
        fondo=40
        print(f"{ESC}[{estilo};{color};{fondo}m El número es mayor. Intenta de nuevo.{ESC}[0m")
    else:
        ESC=chr(27)
        estilo=0
        color=31
        fondo=40
        print(f"{ESC}[{estilo};{color};{fondo}m El número es menor. Intenta de nuevo.{ESC}[0m")
    num=int(input("Adivina el número: "))
if num == numero_aleatorio:
        ESC=chr(27)
        estilo=0
        color=32
        fondo=40
        print(f"{ESC}[{estilo};{color};{fondo}m ¡Felicidades! Adivinaste el número en {cuentaIntentos} intentos.{ESC}[0m")
        print("\N{party popper}")
else:
        ESC=chr(27)
        estilo=0
        color=31
        fondo=40
        print(f"{ESC}[{estilo};{color};{fondo}m Lo siento, no adivinaste el número. El número era {numero_aleatorio}.{ESC}[0m")
        print("\N{disappointed face}")