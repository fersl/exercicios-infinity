import funcoes

while True:
    print(f"{' CALCULADORA ':=^30}")
    print(f"[1] - SOMA\n"
          f"[2] - SUBTRAÇÃO\n"
          f"[3] - MULTIPLICAÇÃO\n"
          f"[4] - DIVISÃO\n"
          f"[5] - SAIR")
    opcao = input("Digite a opção desejada: ")
    print(f"{'':-^30}")
    if opcao == '5':
        break
    else:
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        print(f"{'':-^30}")

        match opcao:
            case '1' | 'SOMA' | 'soma':
                resultado = funcoes.soma(x, y)
                print(f"{x} + {y} = {resultado}")
            case '2' | 'SUBTRAÇÃO' | 'subtração':
                resultado = funcoes.subtracao(x, y)
                print(f"{x} - {y} = {resultado}")
            case '3' | 'MULTIPLICAÇÃO' | 'multiplicação':
                resultado = funcoes.multiplicacao(x, y)
                print(f"{x} * {y} = {resultado}")
            case '4' | 'DIVISÃO' | 'divisão':
                resultado = funcoes.divisao(x, y)
                print(f"{x} / {y} = {resultado}")
