numero=input("Vou dobrar o numero q vc digitar:")

# Quando dar error em alguma linha do código, pula para except 
try:
    if numero.isdigit():
        print(f"O dobro de {float(numero)} é {float(numero)*2:.2f}")
except:
    print("Vc não digitou um número ")