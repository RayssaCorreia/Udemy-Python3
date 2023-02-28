nome = "João"
sobre_nome = "Silvestre"
idade = 40
ano_nascimento = 2023 - idade
maior_de_idade= idade >= 18
altura = 1.62
peso = 60
imc = peso / (altura**2)
a= "A"
b= "B"
c= 2.1

string = " {letra_c} \n a = {} \n b = {} \n c ={letra_c:.2f} \n "
teste = string.format( a, b, letra_c =c)
print (teste)

print ("Nome:", nome)
print ("Sobre nome:", sobre_nome)
print ("idade:", idade)
print ("ano de nascimento:",ano_nascimento)
print ("imc:", imc)
if maior_de_idade == True: 
    print ("você é maior de idade:", maior_de_idade)
else:
    print ("você é menor de idade:", maior_de_idade)
