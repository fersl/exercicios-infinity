class Computador:
    def __init__(self, modelo, fabricante, processador, ram, hd_total, hd_ocupado):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.ram = ram
        self.hd_total = hd_total
        self.hd_ocupado = hd_ocupado
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print("O computador foi ligado.")

    def desligar(self):
        self.ligado = False
        print("O computador foi desligado.")

    def limparHD(self, espaco_liberado):
        novo_hd_ocupado = self.hd_ocupado - espaco_liberado
        if (novo_hd_ocupado > 0) and (novo_hd_ocupado <= self.hd_total):
            self.hd_ocupado = novo_hd_ocupado
            print(f"Operação realizada com sucesso.\n"
                  f"HD: {self.hd_ocupado}/{self.hd_total}")
        else:
            print(f"Erro na operação. O espaço total ocupado deve ser no mínimo 0.\n"
                  f"HD: {self.hd_ocupado}/{self.hd_total}")

    def ocuparHD(self, espaco_ocupado):
        novo_hd_ocupado = self.hd_ocupado + espaco_ocupado
        if (novo_hd_ocupado > 0) and (novo_hd_ocupado <= self.hd_total):
            self.hd_ocupado = novo_hd_ocupado
            print(f"Operação realizada com sucesso.\n"
                  f"HD: {self.hd_ocupado}/{self.hd_total}")
        else:
            print(
                f"Erro na operação. Você está tentando ocupar mais espaço que o total suportado pelo HD.\n"
                f"HD: {self.hd_ocupado}/{self.hd_total}")


# MAIN---------------------------------------------
print(f"{' Criação de novo computador ':-^30}")
modelo = input("Digite o modelo do computador: ")
fabricante = input("Digite o nome do fabricante: ")
processador = input("Digite as informações do processador: ")
ram = float(input("Digite o a cacidade da ram, em gigabytes: "))
hd_total = float(input("Digite a capacidade total do HD, em gigabytes: "))
hd_ocupado = float(input("Digite a quanidade ocupada do HD, em gigabytes: "))

novo_computador = Computador(modelo,
                             fabricante, processador, ram, hd_total, hd_ocupado)

novo_computador.ligar()
while True:
    print(f"{' Menu de Operações ':=^50}")
    print(f"[1] Ocupar HD.\n"
          f"[2] Liberar HD\n"
          f"[3] Desligar Computador.\n")
    opcao = int(input("Digite o número da operação desejada: "))
    print(f"{'':=^50}")
    if opcao == 3:
        novo_computador.desligar()
        break
    elif opcao == 1:
        espaco_ocupado = int(
            input("Digite a quantidade a ser ocupada no HD, em gigabytes: "))
        novo_computador.ocuparHD(espaco_ocupado)
    elif opcao == 2:
        espaco_liberado = int(
            input("Digite a quantidade a ser liberada no HD, em gigabytes: "))
        novo_computador.limparHD(espaco_liberado)
