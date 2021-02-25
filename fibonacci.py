def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

#Vamos a aplicar aqui la memoización
def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[0]
    except KeyError: #Pedir perdon y no pedir permiso
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado 

        return resultado


if __name__ == '__main__':
    n = int(input("Escoge un número: ")) 
    resultado = fibonacci_dinamico(n)
    print(resultado)
