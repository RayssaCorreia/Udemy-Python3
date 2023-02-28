nome = input("nome: ")
sobre_nome = input("sobre_nome: ")
# Gruda um na frente do outro 
print (nome + sobre_nome)

primeiro_valor = input("digiti um numero: ")
segundo_valor = input("digiti outro numero: ")

int(primeiro_valor)
int(segundo_valor)

if primeiro_valor or segundo_valor != type(int):
    print("isso não é um numero")
elif primeiro_valor > segundo_valor:
    print(f" {primeiro_valor = } é maior que o {segundo_valor = }")
else:
    print(f"o segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}")

