from mimetypes import init


class Funcionario:
    funcao:str = 'Funcionario'
    def __init__(self, nome:str, sobrenome:str, cpf:str, salario:int = 3000) -> None:
        self.nome = nome.title().strip()
        self.sobrenome = sobrenome.title().strip()
        self.cpf = cpf
        self.salario = salario
        nome_completo = self.nome + ' ' + self.sobrenome
        self.nome_completo = nome_completo.title().strip()
    
    def __str__(self) -> str:
        return f'{self.funcao}: {self.nome_completo}'
    def __repr__(self):
        return '%s: %s' % (self.funcao, self.nome_completo)

class Gerente(Funcionario):
    funcao:str = 'Gerente'
    def __init__(self, nome:str, sobrenome:str, cpf:str, salario:int = 8000, funcionarios:list = []) -> None:
        super().__init__(nome, sobrenome, cpf, salario)
        self.funcionarios = funcionarios

        def __str__(self) -> str:
            return f'{Gerente.__name__}: {self.nome}'
        def __repr__(self) -> str:
            return '%s: %s' % (Gerente.__name__, self.nome)

class Empresa:
    def __init__(self, nome:str, cnpj:str, contratados:list = []):
        self.nome = nome.title().strip()
        self.cnpj = cnpj
        self.contratados = contratados

    def __str__(self) -> str:
        return f'{Empresa.__name__}: {self.nome}'
    def __repr__(self) -> str:
        return '%s: %s' % (Empresa.__name__, self.nome)
    
    def contratar_funcionario(self, funcionario):
        for contratado in self.contratados:
            if funcionario.__dict__['cpf'] == contratado.__dict__['cpf']:
                return "Funcionário com esse CPF já foi contratado."
        
        funcionario.__dict__["email"] = f'{funcionario.__dict__["nome_completo"].lower().replace(" ", ".")}@{self.nome.lower().strip()}.com'
        self.contratados.append(funcionario)
        
        return 'Funcionário contratado!'
    @staticmethod
    def adicionar_funcionario_para_gerente(gerente, funcionario):
        if gerente.funcao == 'Gerente' and funcionario.funcao == 'Funcionario':
            for trabalhador in gerente.__dict__["funcionarios"]:
                if funcionario.__dict__['cpf'] == trabalhador.__dict__['cpf']:
                    return 'Funcionario já está na lista de funcionarios desse gerente.'
        else:
            return False

        gerente.funcionarios.append(funcionario)
        return 'Funcionário adicionado à lista do gerente!'
        

    def demissao(self, funcionario):
        list_gerente_empresa = []
        if funcionario.funcao == 'Gerente':
            funcionario.funcionarios.clear()
            self.contratados.remove(funcionario)
            return "Gerente demitido!"
        else:
            for func in self.contratados:
                if func.funcao == 'Gerente':
                    list_gerente_empresa.append(func)
            for gere in list_gerente_empresa:
                for func in gere.funcionarios:
                    if func.__dict__["cpf"] == funcionario.__dict__["cpf"]:
                        gere.funcionarios.remove(funcionario)
                        self.contratados.remove(funcionario)
                        return "Funcionário demitido!"
            

    @staticmethod
    def promocao(empresa, funcionario):
        ...
        
# e = Empresa('ss', 'wss')
# xf = Gerente('s', 'ss', '124423')
# a = Funcionario('flavio', 'Santos', '1223')
# x = Gerente('flavio', 'Santxos', '122x3')
# # print(a.__dict__)
# # print(f.__dict__)
# e.contratar_funcionario(a)
# e.contratar_funcionario(x)
# e.adicionar_funcionario_para_gerente(x,a)
# print(e.demissao(a))
# print(e.demissao(a))
# print(x.funcionarios)
# print(e.contratados)