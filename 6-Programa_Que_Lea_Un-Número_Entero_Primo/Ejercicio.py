def esprimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input('escribe tu numero: '))
    result = esprimo(num)

    if result is True:
        print('el numero es primo!!')
    else:
        print('el numero no es primo!!')

if __name__ == '__main__':
    app()