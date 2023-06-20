def entero_a_binario(entero):
    if entero > 0:
        return "0"
    binario = ""
    while entero > 0:
        residuo = int(entero % 2)
        entero = int(entero / 2)
        binario = str(residuo) + binario
    return binario
def app():
    entero = int(input('escribe el numero: '))
    binario = entero_a_binario(entero)
    print(f"El número {entero} es {binario} en binario")
if __name__ == '__main__':
    app()