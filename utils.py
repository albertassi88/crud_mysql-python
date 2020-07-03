import MySQLdb

def conectar():

    try:
        conn = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='albertassi88',
            passwd='R@dio88FM'
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro de conexão: {e}')


def desconectar(conn):

    if conn:
        conn.close()


def listar():

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        for produto in produtos:
            print("...............")
            print(f'ID {produto[0]}')
            print(f'Nome {produto[1]}')
            print(f'Preço {produto[2]}')
            print(f'Estoque {produto[3]}')
            print("...............")
        else:
            print("Não existe produtos cadastrados!")

    desconectar(conn)


def inserir():

    conn = conectar()
    cursor = conn.cursor()
    nome = input('Digite o nome do produto:')
    preco = float(input('Digite o preço do produto:'))
    estoque = int(input('Digite a quantidade no estoque:'))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print('Não foi possivel inserir o produto!')

    desconectar(conn)


def atualizar():

    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Digite o ID:'))
    nome = input(('Digite o novo nome do produto:'))
    preco = float(input('Digite o novo preço do produto:'))
    estoque = int(input('Digite a nova quantidade em estoque do produto'))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE = id={id}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso!')
    else:
        print('Não foi possível atualizar o novo produto!')

    desconectar(conn)


def deletar():

    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Digite o id do produto para ser excluído'))
    cursor.execute(f"DELETE FROM produtos WHERE id={id}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O id {id} foi excluido com sucesso!')
    else:
        print('Não foi possivel excluir o produto!')
    desconectar(conn)


def menu():

    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida!')
    else:
        print('Opção inválida!')
