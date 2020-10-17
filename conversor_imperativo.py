#Forma imperativa

base1 = int(input("Ingrese la base de el número que desea convertir: "))
numero = input("Ingrese el número teniendo en cuenta la base en la que se encentra: ")
base2 = int(input("Ingrese la base a la cual desea convertir el numero: "))
cadenaConversion = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
numero_base10 = 0
numero = numero[::-1]
for i in range(0, len(numero), 1):
    if ord(numero[i]) >= 65:
        numero_base10 += int(ord(numero[i]) - 55) * (base1** i) 
    else:
        numero_base10 += int(ord(numero[i]) - 48) * (base1** i)

if (base2==10):
    print(numero_base10)
elif numero_base10 < base2:
    print(cadenaConversion[numero_base10])
elif(numero_base10 < 100):
    print(cadenaConversion[numero_base10//base2] + cadenaConversion[numero_base10%base2])
elif(numero_base10 < 1000):
    print(cadenaConversion[numero_base10//base2] + cadenaConversion[(numero_base10//base2)//base2] + cadenaConversion[numero_base10%base2])
elif(numero_base10 < 10000):
    print(cadenaConversion[numero_base10//base2] + cadenaConversion[(numero_base10//base2)//base2] + cadenaConversion[((numero_base10//base2)//base2)//base2] + cadenaConversion[numero_base10%base2])
elif(numero_base10 < 100000):
    print(cadenaConversion[numero_base10//base2] + cadenaConversion[(numero_base10//base2)//base2] + cadenaConversion[((numero_base10//base2)//base2)//base2] + cadenaConversion[(((numero_base10//base2)//base2)//base2)//base2] + cadenaConversion[numero_base10%base2])    
