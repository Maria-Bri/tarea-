#Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
#programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
#un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
#del programa:
#Introduzca las Horas: 20
#Introduzca la Tarifa por hora: nueve
#Error, por favor introduzca un número
#Introduzca las Horas: cuarenta
#Error, por favor introduzca un número

try:
    horas = int(input("Introduzca las Horas\n"))
    tarifa = int(input("Introduzca la Tarifa por Hora\n"))

    if horas>40 :
        salario = float((40*tarifa) + (horas-40)*1.5*tarifa)
    else :
        salario = float(horas*tarifa)
    print("Salario: ",salario)

except:
    print("Error, por favor introduzca un número")