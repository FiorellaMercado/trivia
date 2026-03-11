contador=0

nombre=input("Ingrese su nombre")
print(f"Bienvevenido, {nombre}")
print("")

respuesta1_usuario=input("Qué es verde, rojo por dentro y tiene semillas de sandía? ")
respuesta1="sandía"
if respuesta1==respuesta1_usuario:
    contador=contador+1

respuesta2_usuario=input("Qué animal hace miau? ")
respuesta2="gato"
if respuesta2==respuesta2_usuario:
    contador=contador+1

respuesta3_usuario=input("De qué color era el caballo blanco del Mcal. López? ")
respuesta3="blanco"
if respuesta3==respuesta3_usuario:
    contador=contador+1

respuesta4_usuario=input("Cuál es la primer letra del abecedario? ")
respuesta4="a"
if respuesta4==respuesta4_usuario:
    contador=contador+1

print(f"{nombre} hiciste {contador} puntos.")

if contador==4:
    print("Excelente")
elif contador >= 2:
    print("Muy bien")
else:
    print("Puedes mejorar")