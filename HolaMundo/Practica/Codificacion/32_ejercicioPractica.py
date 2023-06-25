# 1.
def combinacion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)


combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8)
#                  (1, 2, 3, 4, 5, 6, 7, 8) >> muestra solamente del 1 en adelante el *args
#           p1  p2


# 2.
def combinacion(p1, p2, *args, p4, p5):
    print(p1)
    print(p2)
    print(args)
    print(p4)
    print(p5)


# p4>> se le aloja que su valor sera 500, se le debe de especificar ya que *args toma todos los valores despues del 1 e inclusive
combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, p4=500, p5=600)
