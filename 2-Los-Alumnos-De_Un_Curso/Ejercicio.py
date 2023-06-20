#Llamamos Los Datos
Nombre =input("Ingrese El Nombre: ")
Sexo = input("Ingrese El Genero (F=Femenino), (M=Masculino)")
#Validamos y Verificamos A Que Grupo Pertenece Por Su Genero
if Nombre <"M":
    if Sexo == "F":
        print("Perteneces Al Grupo A")
    else:
        print("Pertences Al Grupo B")
elif Nombre > "N":
    if Sexo == "M":
        print("Pertecenes Al Grupo A")
    else:
        print("Pertenes Al Grupo B")