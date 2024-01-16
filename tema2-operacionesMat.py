numero1=20
numero2=4
print("La suma es ",(numero1+numero2))
print("La resta es ",(numero1-numero2))
print("La multiplicacion es ",(numero1*numero2))
print("La division es ",(numero1/numero2))
print("La division exacta es ",(numero1//numero2))
print("La potencia es ",(numero1**numero2))




texto1="Hola"
texto2="Mundo"

textoFinal=texto1+" "+texto2
print(textoFinal)

print("El saludo es:  %s %s" %(texto1, texto2))


saludoFinal="Saludo {} {}".format(texto1,texto2)
print(saludoFinal)

saludoFinal2 = "Saludo 2: {y} {x}".format(x=texto1,y=texto2)
print(saludoFinal2)


