import os
os.system("cls")

VIDRIAGON_POR_SOLDADO = 3
TEMPERATURA_CONGELACION = -15

soldados_inmaculados = int(input("Ingrese la cantidad de soldados inmaculados: "))
soldados_dothrakis  = int(input("Ingrese la cantidad de soldados dothrakis:  "))
vidriagon_disponible = int(input("Ingrese la cantidad de dagas disponibles:  "))
temp_actual = float(input("Ingrese la temperatura actual: "))
existen_dragones = input("Daenerys llevo sus dragones? si - no: ")

ejercito_total = soldados_inmaculados + soldados_dothrakis
vidriagon_necesario = ejercito_total *  VIDRIAGON_POR_SOLDADO
deficit_armas = vidriagon_necesario - vidriagon_disponible

if ejercito_total >= 20_000 and existen_dragones == "si" and vidriagon_disponible >= vidriagon_necesario:
    mensaje = print("¡Victoria Absoluta! El Rey de la Noche ha sido derrotado sin problemas.")

elif ejercito_total >= 10_000 and existen_dragones == "si" and temp_actual <= TEMPERATURA_CONGELACION or deficit_armas < 0:
    mensaje = print(f"Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastróficas. Faltaron {deficit_armas} dagas.")

elif ejercito_total < 10_000 and existen_dragones == "si" and temp_actual > TEMPERATURA_CONGELACION:
    mensaje = print("Retirada Táctica: No somos suficientes, pero los dragones nos dieron tiempo para huir hacia el sur.")

else:
    mensaje = "Derrota Total: Invernalia ha caído. Comienza la Larga Noche..."  
print(mensaje)