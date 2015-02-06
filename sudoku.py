import sys

colum = 1
fila = 1
validacion = [0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 1


def cuadrante(n, m):
    n -= 1
    m -= 1
    cua = -1
    cua += n // 3 + 1
    cua += m // 3 * 3
    return cua


texto = open("sudoku_válido.txt","r")
contenido = texto.read().replace('\n' , '')
contenido = str(contenido.replace(',' , ''))
print (contenido)

for espacio in contenido:
    valor = int(contenido[i-1])
    if valor < 1 or valor > 9:
        print("Tipo de sudoku invalido")
        sys.exit(0)
    validacion[fila-1] += valor
    validacion[colum-1] += valor
    validacion[cuadrante(colum, fila)-1] += valor
    validacion[valor-1] += 1
    colum += 1
    i += 1
    if colum == 10:
        colum = 1
        fila += 1
j = 0
for final in validacion:
    if validacion[j] != 144:
        print("El resultado es incorrecto")
        sys.exit(0)
    j +=1
print("¡Felicidades resolviste el sudoku!")
