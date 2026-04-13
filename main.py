# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

# try:
#     edad = int(input("Ingrese su edad\n"))
#     if edad >= 18:
#         print("Es mayor a 18 años")
#     else:
#         print("Es menor de edad")
# except:
#     print("Valor ingresado debe ser numérico")

# # Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# # User1: pedro   	Contraseña1: 1234
# # User2: angel		Contraseña2: a4s1

# user1 = "pedro"
# contraseña1 = 1234
# user2 = "angel"
# contraseña2 = "a4s1"

# user = input("Ingrese su usuario\n")
# contraseña = input("Ingrese su contraseña\n")

# if user == user1 and contraseña1 or user == user2 and contraseña2:
#     print(f"Hola {user}")
# else:
#     print("Credenciales invalidas")
    
# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

acum_nota = 0
for x in range (3):
    notas = float(input("Ingrese su nota\n"))
    acum_nota = acum_nota + notas
promedio = acum_nota / 3
print(f"Su promedio es {promedio}")
if promedio >= 4:
    print("Aprobado")
else:
    print("Reprobado")

# Crear una salida por pantalla con la siguiente información:

# ¿Cuál de los siguientes animales vive en el agua?
# Perro
# Cocodrilo
# Conejo
# Tiburón



# Si la respuesta es Cocodrilo, asignar +0.5 a puntaje, si la res-puesta es Tiburón asignar +1.0 a puntaje, del cualquier otro caso, no asignar valor, finalmente crear una salida por panta-lla para mostrar el puntaje obtenido.

# De la misma forma del ejercicio anterior, debes crear un formulario con 3 pre-guntas (4 respuestas por cada pregunta) de un tema a elección, ya sea pe-lículas, series, caricaturas, entre otras.

# Asignar puntaje a cada pregunta y dependiendo del puntaje generar una escala de notas, así cuando los usuarios respondan las 3 preguntas se les muestra mediante una salida por pantalla su puntaje obtenido y la nota que equivale.

