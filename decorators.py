# Definindo um decorator
def my_decorator(func):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        func()
        print("Algo está acontecendo depois da função ser chamada.")

    return wrapper


# Aplicando o decorator a uma função
@my_decorator
def say_hello():
    print("Olá!")


# Chamando a função
say_hello()
