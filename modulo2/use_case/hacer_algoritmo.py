# El usuario debe digitar su nombre, edad, y dos números. Luego podrá seleccionar una opción de un listado con las 4 operaciones básicas (Suma, Resta, División y Multiplicación) marcando su número correspondiente (1 - 4). Luego que elija la opción deseada, se debe realizar el cálculo de los 2 números con dicha operación e imprimir el cálculo. 

print("mi nombre es")
usename = input("toshio")

print("dime tu edad")
edad = input("28")
  print("genera lo numero del 1 al 10: ")
input()  
 
while menu >4:
 menu = int(input("opciones de operacion: \n 1)suma \n 2)resta \n 3)multiplicacion \n 4)division \n"))  

 

# 2.Aqui usamos if y elif para digitar el resultado de la opcion escogida por el usuario.

if menu == 1:
  print("la suma de" , numero1, "y" , numero2, "es igual a" ,(numero1+numero2) )
elif menu == 2:
  print("la resta de" , numero1, "menos" , numero2, "es igual a ", (numero1-numero2)) 
elif menu == 3:
  print("la multiplicacion de" , numero1, "por" , numero2, "es igual a", (numero1*numero2))
elif menu == 4:
    

    if numero2 == 0:
      print("el segundo numero no puede ser igual a 0")  
    else:
      print("la division de" , numero1, "entre" , numero2, "es igual a", (numero1/numero2))    
else:
  print("por favor digita una opcion correcta") 

