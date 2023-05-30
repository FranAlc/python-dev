# Callbacks

promedio = lambda *args: sum(args) / len(args)


def aprobatorio(calificacion): return calificacion >= 7

def es_aprobatorio(calificacion):
    return calificacion >= 90


def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}')
    else:
        print('No aprobaste la materia')


mostrar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 7)
