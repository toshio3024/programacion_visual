# hacer un programa que me pida mi edad, no permitir que sea menor de edad. al final que diga bienbenido.

print("cual es mi edad:")
edad =int(input())

while edad < 18:
  print("digita nuevamente tu edad")
  edad = int(input())
print ("edad aceptada")

if edad >= 18:  
   print("a que bar me gustaria ir")
   bar = input()
   

else:
   print(" si es menor de edad , debe esperar ser mayor de eda")
print("bienbenido")
