# ETAPAS:
# Un sistema que consulte la edad, y de acuerdo a ella indique si la persona es mayor de edad o no.

try:
    edad = int(input("Ingrese su edad\n"))
    if edad >= 18:
        print("Es mayor a 18 años")
    else:
        print("Es menor de edad")
except:
    print("Valor ingresado debe ser numérico")

# Crear un programa de validación de usuario y contraseña (consultar usuario y contraseña), los únicos dos usuarios conectados son:
# User1: pedro   	Contraseña1: 1234
# User2: angel		Contraseña2: a4s1

user1 = "pedro"
contraseña1 = 1234
user2 = "angel"
contraseña2 = "a4s1"

user = input("Ingrese su usuario\n")
contraseña = input("Ingrese su contraseña\n")

if user == user1 and contraseña == contraseña1 or user == user2 and contraseña == contraseña2:
    print(f"Hola {user}")
else:
    print("Credenciales invalidas")
    
# Solicitar el ingreso de 3 notas por pantalla, luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación), finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el promedio sea igual o mayor a 4.0.

try:

    acum_nota = 0
    cantidad = 3
    for x in range (cantidad):
        notas = float(input("Ingrese su nota\n"))
        acum_nota = acum_nota + notas
    promedio = acum_nota / cantidad
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

    pregunta = int(input("¿Cuál de los siguientes animales vive en el agua? \n 1. Perro \n 2. Cocodrilo \n 3. Conejo \n 4. Tiburón \n"))
    if pregunta == 2:
        puntaje = 0.5
    elif pregunta == 4:
        puntaje = 1
    else:
        puntaje = 0
    print(f"Usted ha obtenido {puntaje} puntos.")

# De la misma forma del ejercicio anterior, debes crear un formulario con 3 pre-guntas (4 respuestas por cada pregunta) de un tema a elección, ya sea pe-lículas, series, caricaturas, entre otras.

# Asignar puntaje a cada pregunta y dependiendo del puntaje generar una escala de notas, así cuando los usuarios respondan las 3 preguntas se les muestra mediante una salida por pantalla su puntaje obtenido y la nota que equivale.

    pregunta2 = int(input("¿Qué es lo mejor para apagar el fuego? \n 1. Extintor \n 2. Leña \n 3. Agua \n 4. Fuego \n"))
    if pregunta2 == 3:
        puntaje2 = 0.5
    elif pregunta2 == 1:
        puntaje2 = 1
    else:
        puntaje2 = 0

    pregunta3 = int(input("¿De qué color era el caballo blanco de Napoleón? \n 1. Caballo \n 2. Blanco \n 3. Café \n 4. Azul \n"))
    if pregunta3 == 1:
        puntaje3 = 0.5
    elif pregunta3 == 2:
        puntaje3 = 1
    else:
        puntaje3 = 0

    pregunta4 = int(input("En Breaking Bad ¿Quien cocina metanfetamina? \n 1. Jesse Pinkman \n 2. Walter White \n 3. Walter Jr. \n 4. Skyler White \n"))
    if pregunta4 == 1:
        puntaje4 = 0.5
    elif pregunta4 == 2:
        puntaje4 = 1
    else:
        puntaje4 = 0

    suma_puntajes = puntaje2 + puntaje3 + puntaje4
    if suma_puntajes == 3:
        nota_final = 7.0
    elif suma_puntajes == 2.5:
        nota_final = 6.0
    elif suma_puntajes == 2:
        nota_final = 5.0
    elif suma_puntajes == 1.5:
        nota_final = 4.0
    elif suma_puntajes == 1:
        nota_final = 3.0
    elif suma_puntajes == 0.5:
        nota_final = 2.0
    else:
        nota_final = 1.0
    print(f"Usted ha obtenido {suma_puntajes} puntos.")
    print(f"Su nota es de {nota_final}")

except:
    print("Valor debe ser numérico")