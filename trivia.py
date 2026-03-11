contador=0

nombre=input("Ingrese su nombre")
print(f"Bienvevenido, {nombre}")

respuesta1_usuario=input("Qué es verde, rojo por dentro y tiene semillas de sandía?")
respuesta1="sandía"
if respuesta1==respuesta1_usuario:
    contador=contador+1

respuesta2_usuario=input("Qué animal hace miau?")
respuesta2="gato"
if respuesta2==respuesta2_usuario:
    contador=contador+1
