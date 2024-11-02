import sqlite3
from typing import List, Optional, Tuple


class Setor:
    def __init__(self, id: Optional[int], nome: str):
        self.id = id
        self.nome = nome


    @property
    def info(self) -> str:
        """ Retorna informações do setor """
        return f"ID: {self.id}, Nome: {self.nome}"


class Colaboradores:
    def __init__(self, id: Optional[int], nome: str, email: str, setor_id: Optional[int]):
        self.id = id
        self.nome = nome
        self.email = email
        self.setor_id = setor_id


    @property
    def info(self) -> str:
        """ Retorna informações do colaborador """
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}, ID Setor: {self.setor_id}"


class Database:
    def __init__(self, nome_banco: str) -> None:
        try:
            self.conn = sqlite3.connect(nome_banco)
            self.cursor = self.conn.cursor()
            self.criar_tabelas()
        except sqlite3.Error as erro:
            print(f"Erro ao se conectar ao banco de dados: {erro}")


    def criar_tabelas(self) -> None:
        try:
            self.cursor.execute('''
                CREATE TABELE IF NOT EXISTS setores (
                    id INTERGER PRIMARY KEY,
                    nome TEXT NOT NULL
                )
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS colaboradores (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    setor_id INTEGER,
                    FOREIGN KEY (setor_id) REFERENCES setores (id)
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Erro ao criar tabelas: {erro}")


    def gravar_txt(self, colaborador: Colaboradores) -> None:
        try:
            with open('colaboradores_info.txt', 'a') as file:
                file.write(colaborador.info + "\n")
        except IOError as erro:
            print(f"Erro ao gravar colaboradores no arquivo: {erro}")


    def criar_setor(self, setor: Setor) -> None:
        try:
            self.cursor.execute('INSERT INTO setores (nome) VALUES (?)',(setor.nome,))
            setor.id = self.cursor.lastrowid
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Erro ao criar setor CLASSE: {erro}")


    def criar_colaboradores(self, colaborador: Colaboradores) -> None:
        try:
            self.cursor.execute('INSERT INTO colaboradores (nome, email, setor_id) VALUES (?, ?, ?)',
                                (colaborador.nome, colaborador.email, colaborador.setor_id))
            colaborador.id = self.cursor.lastrowid
            self.conn.commit()
            self.gravar_txt(colaborador)
        except sqlite3.Error as erro:
            print(f"Erro ao criar novo colaborador: {erro}")


    def buscar_todos_colaboradores(self) -> List[Tuple[int, str, str, Optional[int]]]:
        try:
            self.cursor.execute('SELECT * FROM colaboradores')
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Erro ao buscar colaboradores: {erro}")
            return []


    def buscar_todos_setores(self) -> List[Tuple[int, str]]:
        try:
            self.cursor.execute('SELECT * FROM setores')
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Erro ao buscar setores: {erro}")
            return []


    def atualizar_colaborador_por_id(self, id: int, nome: str, email: str, setor_id: int) -> None:
        try:
            self.conn.execute('''
                UPDATE colaboradores
                SET nome = ?, email = ?, setor_id = ?
                WHERE id = ?
            ''', (nome, email, setor_id, id))
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Erro ao atualizar colaborador: {erro}")


    def remover_colaborador(self, id: int) -> None:
        try:
            self.cursor.execute('DELETE FROM colaboradores WHERE id = ?', (id,))
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Erro ao remover colaborador: {erro}")


    def remover_setor(self, id: int) -> None:
        try:
            self.conn.execute('DELETE FROM setores WHERE id = ?', (id,))
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Erro ao remover setor: {erro}")


    @staticmethod
    def fechar_conexao(conn: sqlite3.Connection) -> None:
        try:
            conn.close()
        except sqlite3.Error as erro:
            print(f"Erro ao fechar a conexao com o banco de dados: {erro}")


class Crud:
    def __init__(self, database: Database) -> None:
        self.database = database


    def criar_setor(self) -> None:
        try:
            nome = input("Informe o nome do setor: ")
            setor = Setor(None, nome)
            self.database.criar_setor(setor)
            print(f"Setor '{nome}' criado com sucesso!")
        except ValueError as erro:
            print(f"Erro ao criar setor CRUD: {erro}")


    def criar_colaborador(self) -> None:
        try:
            nome = input("Informe o nome do colaborador: ")
            email = input("Informe o email do colaborador: ")
            setor_id = int(input("Informe o ID do setor do colaborador"))
            colaborador = Colaboradores(None, nome, email, setor_id)
            self.database.criar_colaboradores(colaborador)
            print(f"Colaborador '{nome}' criado com sucesso!")
        except ValueError as erro:
            print(f"Erro ao criar colaborador: {erro}")


    def ler_setores(self) -> List[Tuple[int, str]]:
        return self.database.buscar_todos_setores()


    def ler_colaboradores(self) -> List[Tuple[int, str, str, Optional[int]]]:
        return self.database.buscar_todos_colaboradores()


    def atualizar_colaboradores(self) -> None:
        try:
            id = int(input("Informe o ID do colabor a ser atualizado: "))
            nome = input("Informe o novo nome do colaborador: ")
            email = input("Informe o novo email do colaborador: ")
            setor_id = input("Informe o novo ID do setor do colaborador: ")
            self.database.atualizar_colaborador_por_id(id, nome, email, setor_id)
            print(f"Colaborador ID '{id}' atualizado com sucesso!")
        except ValueError as erro:
            print(f"Erro ao atualizar colaborador: {erro}")


if __name__ == "__main__":
    database = Database('empresa.db')
    crud = Crud(database)

    while True:
        print("\nEscolha uma opção: ")
        print("1. Criar Setor")
        print("2. Criar Colaborador")
        print("3. Listar Setores")
        print("4. Listar Colaboradores")
        print("5. Atualizar Colaboradores")
        print("6. Sair")

        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            crud.criar_setor()
        elif opcao == '2':
            crud.criar_colaborador()
        elif opcao == '3':
            setores = crud.ler_setores()
            for setor in setores:
                print(setor)
        elif opcao == '4':
            colaboradores = crud.ler_colaboradores()
            for colaborador in colaboradores:
                print(colaborador)
        elif opcao == '5':
            crud.atualizar_colaboradores()
        elif opcao == '6':
            Database.fechar_conexao(database.conn)
            print("Conexão encerrada")
            break
        else:
            print("Opção inválida. Tente novamente.")