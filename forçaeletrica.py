#tive uma pequena ajuda do ChatGPT para descobrir meus erros em relação a multiplicação de Q e q pelos prefixos, futuramente irei adicionar a funcionalidade de converter as medidas de distancia caso não estiverem em metros.
from math import pow

print('Bem-vindo à calculadora de Força Elétrica!')

k = 9 * pow(10, 9)  # Constante de Coulomb

Q = float(input('Insira a carga elétrica de Q: '))
q = float(input('Insira a carga elétrica de q: '))

# Criando variáveis para os prefixos das cargas
microColoumb = pow(10, -6)  # Microcoulomb
nanoColoumb = pow(10, -9)  # Nanocoulomb
miliColoumb = pow(10, -3)  # Milicoulomb

# Descobrindo o prefixo das cargas
askprefixo = input(
    'Em qual prefixo estão as cargas? (Responda micro, nano ou mili): ').lower()  # CONVERTE O QUE FOI DIGITADO EM MINUSCULAS

if askprefixo == 'micro':
    Q *= microColoumb  ##atualiza o valor de Q e q pela multiplicação deles pelo mC
    q *= microColoumb
elif askprefixo == 'mili':
    Q *= miliColoumb  ##atualiza o valor de Q e q pela multiplicação deles pelo miliC
    q *= miliColoumb
elif askprefixo == 'nano':
    Q *= nanoColoumb  ##atualiza o valor de Q e q pela multiplicação deles pelo nanoC
    q *= nanoColoumb
else:
    print("Prefixo não reconhecido. Usando o valor original das cargas.")

distancia = float(input('Insira a distância entre os corpos: '))

# variáveis para converter outras medidas em metro
centimetros = pow(10, -1)
milimetros = pow(10, -3)

askdistancia = str(
    input('Em qual medida está a distância ( Responda metros (m), centimentros(cm), milimetros(mm): ')).lower()

if askdistancia == 'centimetros' or askdistancia == 'cm':
    distancia *= centimetros
if askdistancia == 'miliimetros' or askdistancia == 'mm':
    distancia *= milimetros
# Determinando a natureza da força (atração ou repulsão)
Fnature = 'repulsão' if Q == q else 'atração'

# Calculando a força (utilizando abs() para garantir valores positivos)
F = k * abs(Q) * abs(q) / pow(distancia, 2)

# Exibindo o resultado com no máximo duas casas decimais
print(f'A intensidade da força de {Fnature} entre os corpos é de: {F:.2f} Newtons')
