# Serie sumatoria de n

def sumatoria(n):
    suma = 0
    l=[]
    for i in range(1,n+1):
        suma += i
        l.append(suma)
    return l


#s Serie fibonacci 
def fibonacci(n):
    a = 1
    b = 1
    l=[]
    if(n==1):
        l.append(a)
    elif(n==2):
        l.append(b)
    else:
        a,b=b,a+b
        l.append(b)
    return l
    
    
    #Serie multiplicacion
def multiplicar(a, b):
    resultado = a * b
    return resultado
x = 5
y = 3
resultado_multiplicacion = multiplicar(x, y)
print(f"El resultado de {x} * {y} es: {resultado_multiplicacion}")

