def add(x, y):
    return x + y;

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return pow(x, y)

print()
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potência")
print()

operation = int(input("Operação a efetuar (1, 2, 3, 4 ou 5): "))

num1 = float(input("Primeiro Número: "))
num2 = float(input("Segundo Número: "))

print()

if (operation == 1):
    print(num1, " + ", num2, " = ", add(num1, num2))
elif (operation == 2):
    print(num1, " - ", num2, " = ", subtract(num1, num2))
elif (operation == 3):
    print(num1, " * ", num2, " = ", multiply(num1, num2))
elif (operation == 4):
        print(num1, " / ", num2, " = ", divide(num1, num2))
elif (operation == 5):
    print(num1, " ^ ", num2, " = ", power(num1, num2))
