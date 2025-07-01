#tive uma pequena ajuda do ChatGPT para descobrir meus erros em relação a multiplicação de Q e q pelos prefixos;
from math import pow

print('Bem-vindo à calculadora de Força Elétrica!')

k = 9 * pow(10, 9)  # Constante de Coulomb

Q = float(input('Insira o valor da carga elétrica Quezão (em Coloumb): '))
q = float(input('Insira o valor da carga elétrica quezinho (em Coloumb): '))

# Criando variáveis para os prefixos das cargas
miliColoumb = pow(10, -3)  # Milicoulomb
microColoumb = pow(10, -6)  # Microcoulomb
nanoColoumb = pow(10, -9)  # Nanocoulomb
picoColoumb = pow(10, -12) # Picocoloumb
# Descobrindo o prefixo das cargas
askprefixo = str(input('Em qual prefixo estão as cargas? (Responda micro, nano, mili ou pico): ')).lower()
      # CONVERTE O QUE FOI DIGITADO EM MINUSCULAS

if askprefixo == 'micro':
    Q *= microColoumb  ##atualiza o valor de Q e q pela multiplicação deles pelo mC
    q *= microColoumb
elif askprefixo == 'mili':
    Q *= miliColoumb  ##atualiza o valor de Q e q pela multiplicação deles pelo miliC
    q *= miliColoumb
elif askprefixo == 'nano':
    Q *= nanoColoumb  ##atualiza o valor de Q e q pela multiplicação deles pelo nanoC
    q *= nanoColoumb
elif askprefixo == 'pico':
    Q *= picoColoumb ##atualiza o valor de Q e q pela multiplicação deles pelo pico
    q *= picoColoumb
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
elif askdistancia == 'miliimetros' or askdistancia == 'mm':
    distancia *= milimetros
else:
      print("Distância não reconhecida. Usando valor original da distância.")
# Determinando a natureza da força (atração ou repulsão)
Fnature = 'repulsão' if Q == q else 'atração'

# Calculando a força (utilizando abs() para garantir valores positivos)
F = k * abs(Q) * abs(q) / pow(distancia, 2)

# Exibindo o resultado com no máximo duas casas decimais
print(f'A intensidade da força de {Fnature} entre os corpos é de: {F:.2f} Newtons')
