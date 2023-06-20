def triangulo(n):
    return "\n".join([" "*(n-i)+"*"*(i+i-1) for i in range(1,n+1)])
numero=int(input("indica un numero: "))
print(triangulo(numero))