print("Lenguajes interpretados \n" 
"Grupo: 60 \n" 
"UNAD\n" 
"\n")

#imprta libreria para ejecutar el algoritmo que incluye el valor de euler que es apróximadamente 2.71828
import math 

#Asigna valores el usuario
resistencia = float(input("Anota la resistencia en ohmios: "))
capacitancia = float(input("Anota la capacitancia en faradios: " ))
voltaje_Vin = float(input("Anota el voltaje en voltios: "))
print("\n") 
tiempo = int(input ("Ingresa el número de tiempos que desea analizar: "))

print("\n") #espacio, para ver más organizado el programa


#Se calcula primero el circuito RC en estado transitorio, producto de la resistencia y la
#capacitancia, asigando valor a tau (τ)
tau = resistencia * capacitancia
segundos = []

#se itera la secuencia de tiempo, es decir las veces que se va a ejecutar el algoritmo
#de acuerdo al número de veces que el usuario que haya asignado cada segundo
for i in range(tiempo):
    time = float(input(f"ingresa el tiempo {i+1} en segundos: ")) #asigna una variable de tipo float
    segundos.append(time) #se imprime el tiempo el nuevo tiempo cada segundo hasta llegar 
                          #al número limite ingresado por el usuario   

print("\n")  #espacio, para ver más organizado el programa

contador = 0 #asigna una variable contador = 0 para hacer el conteo desde el segundo asignado

#Nos permite ejecutar el algoritmo las veces que el usuario haya asignado a la vaiable tiempo

while contador < len(segundos):# Incrementa el contador en cada segundo 
    time = segundos[contador] 
    exponente = math.exp(-time/tau)
    capacitor_Vout = voltaje_Vin * (1 - exponente)
    print(f"En {time} segundos el voltaje del capacitor es {capacitor_Vout:.4f} voltios")
    contador += 1




