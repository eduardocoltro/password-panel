from fila import Fila
fila = Fila()
senhas = []
contador = 0

def verificaOpcao():

    global contador
    if opcaoDesejada == 1:
        print(f"Sua senha reservada é {contador} ")
        fila.enqueue(contador)
        contador += 1
        menu()

    elif opcaoDesejada == 2:
        senhas.append(fila._vet[0])
        print(f"Sua senha no momento é {fila._vet[0]} ")
        fila.dequeue()
        menu()

    elif opcaoDesejada == 3:
        print(f"Senhas já realizadas: {senhas}")
        menu()

    else:
        print(f"Esta opção não existe, tente novamente ")
        menu()

def menu():
    global opcaoDesejada
    opcaoDesejada = int(input(
        "Tecle 1 se você quer obter uma nova senha | Tecle 2 se você quer realizar uma nova senha | Tecle 3 se você quer obter senhas já realizadas: "))
    verificaOpcao()

menu()
