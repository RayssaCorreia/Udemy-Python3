#Boas praticas 
""""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
     <- Contagem de complexidade (ruim)
Nomes explicativos 
"""

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 101  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade = 70 #  1  Velocidade atual do carro
local_carro = 100 # Local em que o carro está na estrada

carro_alta_velocidade = velocidade > RADAR_1
carro_dentro_velocidade = velocidade <= RADAR_1
carro_dentro_range_multa = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                           local_carro <= (LOCAL_1 + RADAR_RANGE)
        
if carro_dentro_velocidade:
    print("Velocidade dentro da norma")

if carro_alta_velocidade:
    print("Passou da velocidade")
    
if carro_dentro_range_multa and \
    carro_alta_velocidade :
    print("Carro multado no radar 1")
    
#PLUS
# local na memória. EX: 140351018245384
print(f"\nLocal da variavel 'velocidade' na memória {id(velocidade)}")