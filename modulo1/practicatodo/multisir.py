# ejercicio multiplicar sin el operador(*)

# a*b = a_1 + a_b + a_3...+ a_b


def multiplicar(a, b):
    if b == 0:
     return 0
    elif b == 1:
      return a
    else: 
       return a + multiplicar(a, b - 1)


if_name_== "_main_" 
    resultado = multiplicar(3, 19)
   print("resultado")       





