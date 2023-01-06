from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, estado, renda):
        self.estado = estado
        self.renda = renda
        self.imposto = 0.0

    @abstractmethod
    def declararImpostos(self):
        pass

    def exibirDados(self):
        # print(f"Estado: {self.estado}\n"
        #       f"Renda: {self.renda}\n"
        #       f"Imposto: {self.imposto}")
        pass

class PessoaFisica(Pessoa):
    def __init__(self, estado, renda, nome, cpf, nascimento):
        super().__init__(estado, renda)
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento

    def declararImpostos(self):
        if self.renda > 2000:
            self.imposto = 0.05 * self.renda
        else:
            self.imposto = 0
        return self.imposto

    def exibirDados(self):
        atributos = vars(self)
        for attr in atributos:
            print(f"{attr}: {atributos[attr]}")

        # print(f"Nome: {self.nome}\n"
        #       f"CPF: {self.cpf}\n"
        #       f"Nascimento: {self.nascimento}")
        # super().exibirDados()

class PessoaJuridica(Pessoa):
    def __init__(self, estado, renda, cnpj, razaoSocial, nomeFantasia):
        super().__init__(estado, renda)
        self.cnpj = cnpj
        self.razaoSocial = razaoSocial
        self.nomeFantasia = nomeFantasia

    def declararImpostos(self):
        self.imposto = 0.2 * self.renda

    def exibirDados(self):
        atributos = vars(self)
        print(self.__class__.__name__)
        for attr in atributos:
            print(f"{attr}: {atributos[attr]}")
        # print(f"CNPJ: {self.cnpj}\n"
        #       f"Razão Social: {self.razaoSocial}\n"
        #       f"Nome Fantasia: {self.nomeFantasia}")
        # super().exibirDados()

#------------------------------------------------------------------------------
pessoa1 = PessoaFisica("Ceará", 3000, "Fulano", 111111, "29/3/23")
pessoa2 = PessoaJuridica("Ceará", 20000, 999999999999, "Seila", "Empresinha")

pessoa1.declararImpostos()
pessoa2.declararImpostos()

pessoa1.exibirDados()
print("----------------")
pessoa2.exibirDados()

vars1 = vars(pessoa1)
vars2 = vars(pessoa2)

