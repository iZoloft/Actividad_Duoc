# Requerimientos
# 1.	Mostrar menú de productos: 
# El programa debe mostrar el siguiente menú:
# 1. Pokébola → $1000
# 2. Poción → $1500
# 3. Revivir → $3000
# 4. Baya → $500
# 5. Finalizar compra
# ________________________________________
# 2.	Ingreso de productos: 
# •	El usuario debe poder seleccionar productos ingresando el número correspondiente. 
# •	Validar que la opción ingresada sea correcta (entre 0 y 4). 
# •	Si la opción es inválida, mostrar un mensaje de error y volver a pedirla. 
# ________________________________________
# 3.	Cantidad de productos: 
# •	Por cada producto seleccionado, pedir la cantidad. 
# •	Validar que la cantidad sea un número entero positivo. 
# ________________________________________
# 4.	Acumulación de compra: 
# •	Calcular el total acumulado de la compra. 
# •	Llevar un contador de la cantidad total de productos comprados. 
# ________________________________________
# 5.	Sistema de descuentos: 
# Aplicar los siguientes descuentos:
# •	🔹 Si el total de la compra supera los $5000 → aplicar 10% de descuento. 
# •	🔹 Si compra más de 10 productos en total → aplicar un 5% adicional. 
# •	🔹 Si el entrenador compra al menos 3 “Revivir” → aplicar un 15% adicional SOLO sobre ese producto. 
#  Los descuentos son acumulables.
# ________________________________________
# 6.	Uso de bandera (flag): 
# •	Usar una bandera para verificar si el usuario compró al menos un producto antes de finalizar. 
# •	Si no compró nada, mostrar un mensaje:
# "No has realizado ninguna compra." 
# ________________________________________
# 7.	Manejo de errores: 
# •	Utilizar try-except para evitar que el programa se rompa ante entradas inválidas (por ejemplo, letras en vez de números). 
# ________________________________________
# 8.	Salida final:
# Mostrar un resumen con: 
# •	Total bruto 
# •	Total de descuentos aplicados 
# •	Total final a pagar 
# •	Cantidad total de productos comprados 




# Requerimientos de Git (OBLIGATORIO)
# 1.	Crear un repositorio público en GitHub con el nombre: 
# tienda-pokemon
# 2.	En la descripción del repositorio, escribir algo como: 
# "Simulación de una tienda Pokémon desarrollada en Python. Proyecto enfocado en el uso de estructuras de control, validación de datos, manejo de errores y control de versiones con Git."
# 3.	Aplicar los comandos aprendidos en clases, como por ejemplo: 
# •	git init 
# •	git add 
# •	git commit 
# •	git push 
# •	Uso de mensajes de commit claros (ej: "Agrega menú de productos", "Implementa descuentos", etc.) 
# 4.	El repositorio debe incluir: 
# •	El archivo principal del programa (.py)
# 5.	Enviar la URL del repositorio a través de AVA.

contador_cantidad = 0
contador_valor = 0
contador_revivir = 0
dscto_producto = 0
dscto_valor = 0
dscto_revivir = 0 
total_revivir = 0
suma_dsctos_revivir = 0
hizo_compra = True
flag = True
print("Bienvenido a la tienda PokéMarket")
while flag:
    try:
        productos = int(input("Menú de productos \n 1. Pokébola $1000 \n 2. Poción $1500 \n 3. Revivir $3000 \n 4. Banja $500 \n 5. Finalizar compra \n"))
        if productos < 1 or productos > 5:
            flag = False
        if productos == 1:
            valor_producto = 1000
            cantidad = int(input("¿Cuantas unidades va a comprar?\n"))
            contador_valor = valor_producto * cantidad + contador_valor
            contador_cantidad = contador_cantidad + cantidad
        elif productos == 2:
            valor_producto = 1500
            cantidad = int(input("¿Cuantas unidades va a comprar?\n"))
            contador_valor = valor_producto * cantidad + contador_valor
            contador_cantidad = contador_cantidad + cantidad
        elif productos == 3:
            valor_producto = 3000
            cantidad = int(input("¿Cuantas unidades va a comprar?\n"))
            contador_valor = valor_producto * cantidad + contador_valor
            contador_cantidad = contador_cantidad + cantidad
            contador_revivir = contador_revivir + cantidad
        elif productos == 4:
            valor_producto = 500
            cantidad = int(input("¿Cuantas unidades va a comprar?\n"))
            contador_valor = valor_producto * cantidad + contador_valor
            contador_cantidad = contador_cantidad + cantidad
        elif productos == 5:
            flag = False
        else:
            print("Coloque un valor entre 1 y 5")
        continuar = int(input("desea seguir comprando? 1.Si   2.No\n"))
        if continuar == 2:
            flag = False
        elif continuar == 1:
            flag = True
        else:
            print("Debes colocar 1 o 2")
    except:
        print("Valor debe ser entre 1 y 5")

if contador_revivir >= 3:
    total_gastado_revivir = contador_revivir * 3000
    suma_dsctos_revivir = total_gastado_revivir * .15

if contador_valor > 5000:
    dscto_valor = .10
if contador_cantidad > 10:
    dscto_producto = .05

suma_dsctos = (contador_valor * dscto_valor) + (contador_valor * dscto_producto)
total_dsctos = suma_dsctos + suma_dsctos_revivir
subtotal = contador_valor - total_dsctos

if contador_cantidad == 0:
    hizo_compra = False

if hizo_compra == False:
    print("No realizo ninguna compra")
else:
    print(f"La cantidad de productos seleccionados es de {contador_cantidad}\nEl valor Neto de la compra es de {contador_valor}")
    print(f"Subtotal: ${subtotal}")
    print(f"Total en descuentos: ${total_dsctos}")
