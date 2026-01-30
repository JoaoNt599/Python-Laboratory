"""
No domínio de uma aplicação para uma Loja de Assistência técnica observa-se a ocorrência
das seguintes entidades: Técnico, Atendente, Cliente, Serviço, Solicitação deServiço e Material.

O Cliente liga para a loja de assistência técnica e solicita a realização de um serviço.

O Atendente é quem atende o cliente e registra a solicitação de serviço. O Atendente definequem será o
técnico que atenderá o cliente (Atribuição do serviço) e registra a atribuição nasolicitação de serviço.

O Técnico registra a data de início do serviço, realiza o serviço e registra a data de conclusão.
Quando o técnico utiliza algum material (produtos) na realização do serviço ele também registra na solicitação
de serviço quais materiais utilizou. Assim, o cliente pode saber quem realizou o serviço, quando o serviço foi
realizado e quais materiais foram utilizados.

Na utilização da aplicação, tanto o atendente como o técnico usam o sistema para fazerem seus registros de informações.
O técnico possui como características nome, cpf, telefone. O Cliente possui as características nome, cpf, endereço e
telefone.

O Atendente possui as características nome e cpf. A Solicitação de Serviço possui como características, número de
identificação, data de solicitação, data de início, data término, além disso deve apresentar quem é o cliente, quem é
o técnico e quais materiais foram utilizados.

A entidade Solicitação de Serviço, pode informar a data da solicitação, quem é o cliente, quem foi o atendente, quem foi
o técnico que realizou o serviço e também quais materiais foram utilizados. Serviço tem como características número de
identificação, descrição e valor. Material tem como características número de identificação, descrição e valor.

Todas as entidades devem possuir um comportamento chamado “exibeInformacoes” para mostrar os dados internos.

"""

from datetime import datetime
from typing import List, Optional


class Pessoa:
    def __init__(self, nome: str, cpf: str, telefone: Optional[str] = None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


    @property
    def exibe_informacoes(self) -> str:
        return  f'Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}'


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, endereco: str, telefone: Optional[str] = None):
        super().__init__(nome, cpf, telefone)
        self.endereco = endereco


    @property
    def exibe_informacoes(self) -> str:
        info = super().exibe_informacoes
        return f'{info}, Endereco: {self.endereco}'


class Atendente(Pessoa):
    pass


class Tecnico(Pessoa):
    pass


class Material:
    def __init__(self, id_material: int, descricao: str, valor: float):
        self.id_material = id_material
        self.descricao = descricao
        self.valor = valor


    @property
    def exibe_informacoes(self) -> str:
        return f'ID Material: {self.id_material}, Descrição: {self.descricao}, Valor: R$ {self.valor}'


class Servico:
    def __init__(self, id_servico: int, descricao: str, valor: float):
        self.id_servico = id_servico
        self.descricao = descricao
        self.valor = valor


    @property
    def exibe_informacoes(self) -> str:
        return f'ID Serviço: {self.id_servico}, Descrição: {self.descricao}, Valor: R$ {self.valor}'


class SolicitacaoServico:
    def __init__(self, numero_id: int, cliente: Cliente, atendente: Atendente, servico: Servico):
        self.numero_id = numero_id
        self.data_solicitacao = datetime.now()
        self.data_inicio: Optional[datetime] = None
        self.data_termino: Optional[datetime] = None
        self.cliente = cliente
        self.atendente = atendente
        self.tecnico: Optional[Tecnico] = None
        self.servico = servico
        self.materiais = []   # list[Material] = []


    def atribuir_tecnico(self, tecnico: Tecnico) -> None:
        try:
            self.tecnico = tecnico
            print(f'Técnico {tecnico.nome} atribuído à solicitaçao {self.numero_id}.')
        except Exception as erro:
            print(f'Erro ao atribuir técnico: {erro}')


    def iniciar_servico(self) -> None:
        try:
            if self.tecnico is None:
                raise ValueError("Técnico não atribuído.")
            self.data_inicio = datetime.now()
            print(f'Serviço {self.numero_id} iniciado em {self.data_inicio}')
        except ValueError as erro:
            print(f'Erro ao iniciar o servico: {erro}')


    def concluir_servico(self) -> None:
        try:
            if self.data_inicio is None:
                raise ValueError("Serviço ainda não iniciado.")
            self.data_termino = datetime.now()
            print(f'Serviço {self.numero_id} concluído em {self.data_termino}.')
        except ValueError as erro:
            print(f'Erro ao concluir o serviço: {erro}')


    def adicionar_material(self, material: Material) -> None:
        try:
            self.materiais.append(material)
            print(f'Material {material.descricao} adicionado à solicitação {self.numero_id}.')
        except Exception as erro:
            print(f'Erro ao adicionar material: {erro}')


    @property
    def exibe_informacoes(self) -> str:
        info_cliente = self.cliente.exibe_informacoes
        info_atendente = self.atendente.exibe_informacoes
        info_tecnico = self.tecnico.exibe_informacoes if self.tecnico else "Técnico não atribuído"
        info_servico = self.servico.exibe_informacoes
        info_materiais = ', '.join([material.exibe_informacoes for material in self.materiais]) or "Nenhum material utilizado"

        return (
            f'Número ID: {self.numero_id}\n'
            f'Data Solicitação: {self.data_solicitacao}\n'
            f'Data Início: {self.data_inicio}\n'
            f'Data Término: {self.data_termino}\n'
            f'Cliente: {info_cliente}\n'
            f'Técnico: {info_tecnico}\n'
            f'Serviço: {info_servico}\n'
            f'Materiais: {info_materiais}\n'
        )


if __name__ == "__main__":
    try:
        cliente = Cliente("João Silva", "123.456.789-00", "Rua das Flores, 123", "11999999999")
        atendente = Atendente("Maria Oliveira", "987.654.321-00")
        tecnico = Tecnico("Carlos Lima", "111.222.333-44", "11888888888")
        servico = Servico(1, "Troca de Tela", 300.0)
        material1 = Material(101, "Tela LCD", 150.0)
        material2 = Material(102, "Cola Especial", 20.0)

        solicitacao = SolicitacaoServico(1, cliente, atendente, servico)
        solicitacao.atribuir_tecnico(tecnico)
        solicitacao.iniciar_servico()
        solicitacao.adicionar_material(material1)
        solicitacao.adicionar_material(material2)
        solicitacao.concluir_servico()

        print(solicitacao.exibe_informacoes)

    except Exception as e:
        print(f"Erro geral na aplicação: {e}")