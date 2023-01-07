nasa_info = {}
medias = {}

while True:
    nome_asteroide = input('Digite o nome do asteóide: ')
    distancias = input(
        'Digite os valores das distâncias separados por vírugla: ').split(',')
    distancias = [float(i) for i in distancias]
    nasa_info[nome_asteroide] = distancias

    flag = input('Deseja continuar? s/n ')
    if flag == 'n':
        break

for asteroide in nasa_info:
    distancias = nasa_info[asteroide]
    media = sum(distancias) / len(distancias)
    medias[asteroide] = media

print(f" \n{' MÉDIAS DOS ASTEROIDES ':-^60} ")
for item in medias:
    print(f"Asteróide: {item}   Média das Distâncias: {medias[item]:.2f}")
print(f" {'':-^60} ")
