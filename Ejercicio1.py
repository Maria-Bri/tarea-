#Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.
#Introduzca las Horas: 45
#Introduzca la Tarifa por hora: 10
#Salario: 475.0

horas = int(input("Introduzca las Horas\n"))
tarifa = int(input("Introduzca la Tarifa por Hora\n"))

if horas>40 :
    salario = float((40*tarifa) + (horas-40)*1.5*tarifa)
else :
    salario = float(horas*tarifa)

print("Salario: ",salario)