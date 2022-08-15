"""agenda com sql"""
import sqlite3


class AgendaDB:
    # vou receber um arquivo de base de dados no meu init
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        # crio a variavel para receber o meu codigo sql se inserção de dados
        # coloco o comando INSERT OR IGNORE pra casos de duplicações de dados onde eu coloquei que nao queria
        # para previnir que de erro no meu codigo
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        # igual fiz no inserir eu crio uma variavel para armazenar meu comando sql de update
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        # fiz da mesma maneira armazenando na minha variavel meu comando sql de DELETE
        consulta = 'DELETE FROM agenda  WHERE id=?'
        # lembrando que o valor que eu passo é uma tupla entao sempre por uma virgula quando eu mandar apenas um valor
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        # buscando na minha base de dados todos os valores igausi ao meu valor ou que contenha meu valor passado
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        # a porcentagem serve pra dizer que poder qualquer valor parecido tanto para esquerda tanto para direita
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')

    # agenda.inserir('diogo', '11444444')
    # agenda.inserir('Miguel', '11444422')
    # agenda.inserir('Maria', '11444433')
    # agenda.inserir('Laryssa', '11444455')
    agenda.inserir('Diogo  Lucas', '103333')
    agenda.inserir('Maria  Lucas', '1033355')
    agenda.inserir('Miguel Lucas', '1033399')
    agenda.inserir('Lucas Lima', '10333676')
    agenda.editar('Maria Leonidia', '11444477', 10)
    agenda.excluir(9)

    agenda.buscar('lucas')
    # agenda.listar()
