#llamamos los Datos
salario =input("Ingrese El Salario: ")
impuesto = int(salario)
#Ahora Si Comparamos 
if impuesto > 12000000 and impuesto < 15000000:
    total = float(impuesto*0.03)
    resultado= str(total)
    print("El impuesto Que Debe Pagar Es De " + resultado)
    
elif impuesto >15000001 and impuesto < 20000000:
    total = float(impuesto*0.05)
    resultado= str(total)
    print("El impuesto Que Debe Pagar Es De " + resultado)
    
elif impuesto> 20000001 and impuesto< 30000000:
    total = float(impuesto*0.08)
    resultado= str(total)
    print("El impuesto Que Debe Pagar Es De " + resultado)
    
elif impuesto> 30000000:
    total = float(impuesto*0.1)
    resultado= str(total)
    print("El impuesto Que Debe Pagar Es De " + resultado)
else:
    print("Tu sueldo Esta Fuera Del Rango")