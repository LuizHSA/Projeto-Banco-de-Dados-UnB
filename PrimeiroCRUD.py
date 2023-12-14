import mysql.connector

conexao = mysql.connector.connect(#Preecnher com os dados do servidor
    host='',
    user = '',
    password = '',
    database = ''
)

cursor = conexao.cursor()
#CREATE
def inserir_usuario(nome, sobrenome, funcao, login, senha, uri):
    comando = f'INSERT INTO usuario (nome, sobrenome, funcao, login, senha, URI_foto_usuario) VALUES ("{nome}", "{sobrenome}", "{funcao}", "{login}", "{senha}", "{uri}")'
    cursor.execute(comando)
    cursor.commit()
#READ
def ler_usuario():
    comando = 'SELECT * FROM usuario'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado
#UPDATE
def atualizar_usuario(ID_usuario,nome, sobrenome, funcao, login, senha, uri):
    comando = f'UPDATE usuario SET nome = "{nome}", sobrenome = "{sobrenome}", funcao = "{funcao}", login = "{login}", senha = "{senha}", URI_foto_usuario = "{uri}" WHERE id = {ID_usuario}'
    cursor.execute(comando)
    cursor.commit()
#DELETE
def deletar_usuario(ID_usuario):
    comando = f'DELETE FROM usuario WHERE id = {ID_usuario}'
    cursor.execute(comando)
    cursor.commit()



#CREATE
def inserir_livro(titulo, autor, ISBN, descricao, categoria, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_capa):
    comando = f'INSERT INTO livro (titulo, autor, ISBN, descricao, categoria, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_capa) VALUES ("{titulo}", "{autor}", "{ISBN}", "{descricao}", "{categoria}", {data_aquisicao}, "{estado_conservacao}", "{localizacao_fisica}", "{URI_foto_capa}")'
    cursor.execute(comando)
    cursor.commit() 
#READ
def ler_livro():
    comando = 'SELECT * FROM livro'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado
#UPDATE
def atualizar_livro(titulo, autor, ISBN, descricao, categoria, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_capa):
    comando = f'UPDATE livro SET titulo = "{titulo}", autor = "{autor}", descricao = "{descricao}", categoria = "{categoria}", data_aquisicao = {data_aquisicao}, estado_conservacao = "{estado_conservacao}", localizacao_fisica = "{localizacao_fisica}", URI_foto_capa = "{URI_foto_capa}" WHERE id = {ISBN}'
    cursor.execute(comando)
    cursor.commit()
#DELETE
def deletar_livro(ISBN):
    comando = f'DELETE FROM livro WHERE id = {ISBN}'
    cursor.execute(comando)
    cursor.commit()



#CREATE
def inserir_mateiral (titulo, descricao, categoria, numero_de_serie, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_material):
    comando = f'INSERT INTO material ( titulo, descricao, categoria, numero_de_serie, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_material) VALUES ("{titulo}", "{descricao}", "{categoria}", {numero_de_serie}, {data_aquisicao}, "{estado_conservacao}", "{localizacao_fisica}", "{URI_foto_material}")'
    cursor.execute(comando)
    cursor.commit()
#READ
def ler_material():
    comando = 'SELECT * FROM material'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado
#UPDATE
def atualizar_material(ID_material, titulo, descricao, categoria, numero_de_serie, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_material):
    comando = f'UPDATE material SET titulo = "{titulo}", descricao = "{descricao}", categoria = "{categoria}", numero_de_serie = {numero_de_serie}, data_aquisicao = {data_aquisicao}, estado_conservacao = "{estado_conservacao}", localizacao_fisica = "{localizacao_fisica}", URI_foto_material = "{URI_foto_material}" WHERE id = {ID_material}'
    cursor.execute(comando)
    cursor.commit()
#DELETE
def deletar_material(ID_material):
    comando = f'DELETE FROM material WHERE id = {ID_material}'
    cursor.execute(comando)
    cursor.commit()



#CREATE
def inserir_emprestimo(data_emprestimo, data_devolucao_prevista, status_emprestimo, ID_usuario_FK, ID_item_FK):
    comando = f'INSERT INTO emprestimo (data_emprestimo, data_devolucao_prevista, status_emprestimo, ID_usuario_FK, ID_item_FK) VALUES ({data_emprestimo}, {data_devolucao_prevista}, "{status_emprestimo}", {ID_usuario_FK}, {ID_item_FK})'
    cursor.execute(comando)
    cursor.commit()

#READ
def ler_emprestimo():
    comando = 'SELECT * FROM emprestimo'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

#UPDATE
def atualizar_emprestimo(ID_emprestimo, data_emprestimo, data_devolucao_prevista, status_emprestimo, ID_usuario_FK, ID_item_FK):
    comando = f'UPDATE emprestimo SET data_emprestimo = {data_emprestimo}, data_devolucao_prevista = {data_devolucao_prevista}, status_emprestimo = "{status_emprestimo}", ID_usuario_FK = {ID_usuario_FK}, ID_item_FK = {ID_item_FK} WHERE id = {ID_emprestimo}'
    cursor.execute(comando)
    cursor.commit()

#DELETE
def deletar_emprestimo(ID_emprestimo):
    comando = f'DELETE FROM emprestimo WHERE id = {ID_emprestimo}'
    cursor.execute(comando)
    cursor.commit()




#CREATE
def inserir_item(ISBN_FK, ID_material_FK):
    comando = f'INSERT INTO item (ISBN_FK, ID_material_FK) VALUES ( {ISBN_FK}, {ID_material_FK})'
    cursor.execute(comando)
    cursor.commit()

#READ
def ler_item():
    comando = 'SELECT * FROM item'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

#UPDATE
def atualizar_item(ID_item, ISBN_FK, ID_material_FK):
    comando = f'UPDATE item SET ISBN_FK = {ISBN_FK}, ID_material_FK = {ID_material_FK} WHERE id = {ID_item}'
    cursor.execute(comando)
    cursor.commit()

#DELETE
def deletar_item(ID_item):
    comando = f'DELETE FROM item WHERE id = {ID_item}'
    cursor.execute(comando)
    cursor.commit()


cursor.close()
conexao.close()