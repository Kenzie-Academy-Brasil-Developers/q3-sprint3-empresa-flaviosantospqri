from mimetypes import init


class Funcionario:
    funcao:str = 'Funcionario'
    def __init__(self, nome:str, sobrenome:str, cpf:str, salario:int = 3000) -> None:
        self.nome = nome.capitalize().strip()
        self.sobrenome = sobrenome.title().strip()
        self.cpf = cpf
        self.salario = salario
        nome_completo = self.nome + ' ' + self.sobrenome
        self.nome_completo = nome_completo.title().strip()
    
    def __str__(self) -> str:
        return f'{self.funcao}: {self.nome_completo}'
    def __repr__(self) -> str:
        return '%s: %s' % (self.funcao, self.nome_completo)

class Empresa:
    def __init__(self, nome:str, cnpj:str, contratados:list = []) -> None:
        self.nome = nome.title().strip()
        self.cnpj = cnpj
        self.contratados = contratados

    def __str__(self) -> str:
        return f'{Empresa.__name__}: {self.nome}'
    def __repr__(self) -> str:
        return '%s: %s' % (Empresa.__name__, self.nome)
    
    def contratar_funcionario(self,funcionario):
        cpf_current = funcionario.__dict__
        for contrado in self.contratados:
            if cpf_current == contrado['cpf']:
                return "Funcionário com esse CPF já foi contratado."
        self.contratados.append(funcionario)
         

class Gerente(Funcionario):
    funcao:str = 'Gerente'
    def __init__(self, nome:str, sobrenome:str, cpf:str, salario:int = 8000, funcionarios:list = []) -> None:
        super().__init__(nome, sobrenome, cpf, salario)
        self.funcionarios = funcionarios

        def __str__(self) -> str:
            return f'{Gerente.__name__}: {self.nome}'
        def __repr__(self) -> str:
            return '%s: %s' % (Gerente.__name__, self.nome)
jose = Gerente("jose", "francisco   pereira", 11122233344)

e = Empresa('miro', '123451')
e.contratar_funcionario(jose)