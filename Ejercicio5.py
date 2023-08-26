#Ejercicio 5: Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
Celsius = float(input("Digite grados en Celsius\n"))
Fahrenheit = float(( Celsius * 9/5) + 32) 
print("Los grados en Fahrenheit es: " , Fahrenheit)