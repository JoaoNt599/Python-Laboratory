""" Agenda Telefonica """


class Contato:
    def __init__(self, fone: str, nome: str) -> None:
        self.__fone = fone
        self.__nome = nome


    def __str__(self) -> str:
        resultado = f"\nNome: {self.__nome}"
        resultado += f"\nFone: {self.__fone}"
        return resultado


    @property
    def fone(self) -> str:
        return self.__fone


    @property
    def nome(self) -> str:
        return self.__nome


    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome


class RepositorioContatos:
    def __init__(self):
        self.__repositorio_contatos = []


    @property
    def repositorio_contatos(self) -> []:
        return self.__repositorio_contatos


    def incluir(self, contato: Contato) -> Contato:
        resultado = None
        if not contato == None:
            self.__repositorio_contatos.append(contato)
            resultado = contato
        else:
            print("Um contato deve ser fornecido.")
        return resultado


    def atulizar(self, indice: int, contato: Contato) -> None:
        """ Recebe um objeto Contato, localiza-o no repositorio e atualiza seus dados"""
        if (contato == None):
            print("Um contato deve ser fornecido.")
        elif (indice == None):
            print("Um indice deve ser fornecido.")
        elif (indice < 0):
            print("O indice não deve ser negativo")
        else:
            self.__repositorio_contatos[indice] = contato
            resultado = contato
        return resultado


    def excluir_por_indice(self, indice: int) -> None:
        """ Recebe o indice do contato de repositorio e o remove """
        resultado = None
        if (indice == None):
            print("Um indice deve ser fornecido.")
        elif (indice < 0):
            print("O indice não deve ser negativo.")
        else:
            resultado = self.__repositorio_contatos.pop(indice)
        return resultado


    def consultar_indice_por_nome(self, nome: str) -> None:
        """ Recebe o nome do contato e retorna se existir no repositorio; se não, retorna  -1 """
        resultado = -1
        indice = -1
        for i in range(0, len(self.__repositorio_contatos)):
            contato = self.__repositorio_contatos[i]
            if contato.nome == nome:
                indice = i
        if indice != -1:
            resultado = indice
        return resultado


    def existe(self, contato: Contato) -> bool:
        """
        Recebe um objeto Contato e retorna True caso exista algum com mesmo telefone;
        Se não, retorna False
        """
        resultado = False
        for c in self.__repositorio_contatos:
            if c.fone == contato.fone:
                resultado = True
                break
        return resultado


    def vazio(self) -> bool:
        return (len(self.__repositorio_contatos) == 0)


class CadastroContatos:
    def __init__(self):
        self.__repositorio_contatos = RepositorioContatos()


    @property
    def repositorio_contatos(self) -> []:
        return self.__repositorio_contatos


    def incluir(self, contato: Contato) -> Contato:
        resultado = None
        if self.__repositorio_contatos.existe(contato):
            input("Contato ja cadastrado. Tecle enter...")
        else:
            resultado = self.__repositorio_contatos.incluir(contato)
        return resultado


    def alterar(self, contato: Contato) -> Contato:
        resultado = None
        if self.__repositorio_contatos.consultar_indice_por_nome(contato.nome) == -1:
            input("Contato nao encontrado. Tecle enter...")
        else:
            indice = self.__repositorio_contatos.consultar_indice_por_nome(contato.nome)
            resultado = self.__repositorio_contatos.atulizar(indice, contato)
        return resultado


    def excluir(self, contato: Contato) -> Contato:
        resultado = None
        if not self.__repositorio_contatos.existe(contato):
            input("Contato nao encontrado. Tecle enter...")
        else:
            indice = self.__repositorio_contatos.consultar_indice_por_nome(contato.nome)
            if indice != -1:
                resultado = self.__repositorio_contatos.excluir_por_indice(indice)
        return resultado


    def consultar(self, nome: str) -> Contato:
        resultado = None
        if not  self.__repositorio_contatos.existe(nome):
            print("Contato nao encontrado.")
        else:
            indice = self.__repositorio_contatos.consultar_indice_por_nome(nome)
            if indice != -1:
                resultado = self.__repositorio_contatos.excluir_por_indice(indice)
        return resultado


class ContatosApp:
    def __init__(self):
        self.__regras_negocio = CadastroContatos()
        self.__loop_principal()


    def __exibe_menu(self) -> None:
        self.__limpar_tela()
        print("\n Selecione uma opcao: ")
        print("\n 1. Incluir novo contato")
        print("\n 2. Alterar telefone de um contato")
        print("\n 3. Excluir um contato")
        print("\n 4. Consultar contato por nome")
        print("\n 5. Listar todos os contatos")
        print("\n")


    def __limpar_tela(self) -> None:
        print("\n" * 100)


    def __opcao_selecionada(self) -> int:
        opcao = input("Escolha uma opcao: ")
        if opcao == '':
            resultado = -1
        else:
            resultado = int(input(opcao))
        return resultado
        print("Confirme o selecao...")


    def __ler_dados_contato(self) -> Contato:
        self.__limpar_tela()
        fone = input("\nTelefone: ")
        nome = input("\nNome: ")
        resultado = Contato(fone, nome)
        return resultado


    def __loop_principal(self) -> None:
        opcao = -1
        while opcao != 6:
            self.__exibe_menu()
            opcao = self.__opcao_selecionada()
            if opcao == 1:
                contato = self.__ler_dados_contato()
                if self.__regras_negocio.incluir(contato) != None:
                    print("\nContato cadastrado com sucesso.")
            elif opcao == 2:
                contato = self.__ler_dados_contato()
                if self.__regras_negocio.alterar(contato) != None:
                    print("\nContato alterado com sucesso.")
            elif opcao == 3:
                self.__limpar_tela()
                fone = input("\nTelefone: ")
                if self.__regras_negocio.excluir(contato) != None:
                    print("\Contato excluido.")
            elif opcao == 4:
                self.__limpar_tela()
                nome = input("\nInforme o nome do contato a localizar: ")
                contato = self.__regras_negocio.consultar(nome)
                if contato != None:
                    print(f"\nContato encontrado: \n{contato}\n")
            elif opcao == 5:
                self.__limpar_tela()
                if not self.__regras_negocio.repositorio_contatos.vazio():
                    for contato in self.__regras_negocio.repositorio_contatos.repositorio_contatos:
                        print(f"\n{contato}\n")
                else:
                    print(f"\nNenhum contato cadastrado!")
            else:
                print("Opcao invalida!")
            if opcao != 6:
                input("Tecle enter para retornar ao menu...")


if __name__ == "__main__":
    app = ContatosApp()