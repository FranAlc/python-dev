# 05 El precio para un vuelo es de $8800 en clase turista y se aplica un incremento del 30% en primera clase. Se ingresan la cantidad de pasajes vendidos de clase turista y de primera clase. Obtener la recaudación total del vuelo.

precio_turista = 8800
primera_clase = 0.3

print("Ingresa la cantidad de pasajes vendidos de clase turista y de primera clase: ")
pasajes_turista = int(input("Clase turista: "))
pasajes_pc = int(input("Primera clase: "))

recaudacion_turista = pasajes_turista * precio_turista
recaudacion_pc = pasajes_pc * precio_turista * (1 + primera_clase)
recaudacion_total = recaudacion_turista + recaudacion_pc

print(f"La recaudacion total es: $ {recaudacion_total}")
