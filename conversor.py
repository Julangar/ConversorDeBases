
#Forma funcional
def convertir_a_base_decimal(numero, base):  # Funcion recibe _numero en cadena y base original en int
    numeroconvertido = 0   # Variable para guardar el numero convertido
    numero = str(numero)  # Convertir numero en cadena
    base = int(base)      # Convertir base en entero
    numero = numero[::-1] # Damos vuelta al numero para multiplicar por su potencia
    for i in range(0, len(numero), 1):  # Contamos potencia "i" desde 0 hasta maxima posicion numero
        if ord(numero[i]) >= 65:  # Si el caracter ASCII es (A=65) o mayor, convertilo a numero
            numeroconvertido += int(ord(numero[i]) - 55) * pow(base, i)  # Restamos 55 para convertir Letra en Numero
        else:
            numeroconvertido += int(ord(numero[i]) - 48) * pow(base, i); # Convertimos numero asci en numero int
                                                                           # Multiplicamos numero por la base
                                                                           # elevada a la posicion, y lo suma a
                                                                           # la variable numeroconvertido
    return numeroconvertido  # Retornamos el numero convertido en formato int

def convertir_entre_bases(n, base, base2):
    cadenaConversion = "0123456789ABCDEFGHIJKLMNOPQRSTUV"
    n = convertir_a_base_decimal(n,base) #Se convierte el numero dado a decimal
    if base2 == 10: #Si la base a la que se desea convertir es 10 se deja el valor en base decimal
        return n
    elif n < base2: # Si el numero es menor que la base se pasa su respectiva representacion el la base a convertir
      return cadenaConversion[n]
    else: # Se utiliza la division entera para hallar el residuo y se utiliza el modulo para el ultimo digito
      return convertir_entre_bases((n//base2), 10, base2) + cadenaConversion[n%base2]

while True:      
    base1 = input("Ingrese la base de el número que desea convertir: ")
    numero = input("Ingrese el número teniendo en cuenta la base en la que se encentra: ")
    base2 = int(input("Ingrese la base a la cual desea convertir el numero: "))
    print(convertir_entre_bases(numero,base1,base2))
    repetir = int(input("Si desea realizar otra conversion ingrese 0, sino ingrese 1: "))
    if(repetir == 1):
        break