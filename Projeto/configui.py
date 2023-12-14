#!C:\Users\Vitor\Desktop\proj\BD\ui\venv\Scripts\python.exe
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
import mysql.connector

conexao = mysql.connector.connect(#Preecnher com os dados do servidor
    host='sql10.freesqldatabase.com',
    user = 'sql10668594',
    password = 'mrQZRkRKnB',
    database = 'sql10668594'
)

cursor = conexao.cursor()
#CREATE
def inserir_usuario(nome, sobrenome, funcao, login, senha, uri):
    comando = f'INSERT INTO usuario (nome, sobrenome, funcao, login, senha, URI_foto_usuario) VALUES ("{nome}", "{sobrenome}", "{funcao}", "{login}", "{senha}", "{uri}")'
    cursor.execute(comando)
    conexao.commit()
#READ
def ler_usuario():
    comando = 'SELECT * FROM usuario'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado
#UPDATE
def atualizar_usuario(ID_usuario,nome, sobrenome, funcao, login, senha, uri):
    comando = f'UPDATE usuario SET nome = "{nome}", sobrenome = "{sobrenome}", funcao = "{funcao}", login = "{login}", senha = "{senha}", URI_foto_usuario = "{uri}" WHERE ID_usuario = {ID_usuario}'
    cursor.execute(comando)
    conexao.commit()
#DELETE
def deletar_usuario(ID_usuario):
    comando = f'DELETE FROM usuario WHERE ID_usuario = {ID_usuario}'
    cursor.execute(comando)
    conexao.commit()



#CREATE
def inserir_livro(titulo, autor, ISBN, descricao, categoria, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_capa):
    comando = f'INSERT INTO livro (titulo, autor, ISBN, descricao, categoria, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_capa) VALUES ("{titulo}", "{autor}", "{ISBN}", "{descricao}", "{categoria}", "{str(data_aquisicao)}", "{estado_conservacao}", "{localizacao_fisica}", "{URI_foto_capa}")'
    cursor.execute(comando)
    conexao.commit()
#READ
def ler_livro():
    comando = 'SELECT * FROM livro'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado
#UPDATE
def atualizar_livro(titulo, autor, ISBN, descricao, categoria, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_capa):
    comando = f'UPDATE livro SET titulo = "{titulo}", autor = "{autor}", descricao = "{descricao}", categoria = "{categoria}", data_aquisicao = "{str(data_aquisicao)}", estado_conservacao = "{estado_conservacao}", localizacao_fisica = "{localizacao_fisica}", URI_foto_capa = "{URI_foto_capa}" WHERE ISBN = {ISBN}'
    cursor.execute(comando)
    conexao.commit()
#DELETE
def deletar_livro(ISBN):
    comando = f'DELETE FROM livro WHERE ISBN = {ISBN}'
    cursor.execute(comando)
    conexao.commit()



#CREATE
def inserir_mateiral (id, descricao, categoria, numero_de_serie, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_material):
    comando = f'INSERT INTO material ( ID_material, descricao, categoria, numero_de_serie, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_material) VALUES ("{id}", "{descricao}", "{categoria}", {numero_de_serie}, {str(data_aquisicao)}, "{estado_conservacao}", "{localizacao_fisica}", "{URI_foto_material}")'
    cursor.execute(comando)
    conexao.commit()
#READ
def ler_material():
    comando = 'SELECT * FROM material'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado
#UPDATE
def atualizar_material(id, descricao, categoria, numero_de_serie, data_aquisicao, estado_conservacao, localizacao_fisica, URI_foto_material):
    comando = f'UPDATE material SET descricao = "{descricao}", categoria = "{categoria}", numero_de_serie = {numero_de_serie}, data_aquisicao = {str(data_aquisicao)}, estado_conservacao = "{estado_conservacao}", localizacao_fisica = "{localizacao_fisica}", URI_foto_material = "{URI_foto_material}" WHERE ID_material = {id}'
    cursor.execute(comando)
    conexao.commit()
#DELETE
def deletar_material(ID_material):
    comando = f'DELETE FROM material WHERE ID_material = {ID_material}'
    cursor.execute(comando)
    conexao.commit()



#CREATE
def inserir_emprestimo(data_emprestimo, data_devolucao_prevista, status_emprestimo, ID_usuario_FK, ID_item_FK):
    comando = f'INSERT INTO emprestimo (data_emprestimo, data_devolucao_prevista, status_emprestimo, ID_usuario_FK, ID_item_FK) VALUES ("{data_emprestimo}", "{data_devolucao_prevista}", "{status_emprestimo}", {ID_usuario_FK}, {ID_item_FK})'
    cursor.execute(comando)
    conexao.commit()

#READ
def ler_emprestimo():
    comando = 'SELECT * FROM emprestimo'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

#UPDATE
def atualizar_emprestimo(ID_emprestimo, data_emprestimo, data_devolucao_prevista, status_emprestimo, ID_usuario_FK, ID_item_FK):
    comando = f'UPDATE emprestimo SET data_emprestimo = "{data_emprestimo}", data_devolucao_prevista = "{data_devolucao_prevista}", status_emprestimo = "{status_emprestimo}", ID_usuario_FK = {ID_usuario_FK}, ID_item_FK = {ID_item_FK} WHERE ID_emprestimo = {ID_emprestimo}'
    cursor.execute(comando)
    conexao.commit()

#DELETE
def deletar_emprestimo(ID_emprestimo):
    comando = f'DELETE FROM emprestimo WHERE ID_emprestimo = {ID_emprestimo}'
    cursor.execute(comando)
    conexao.commit()




#CREATE
def inserir_item(ISBN_FK, ID_material_FK):
    comando = f'INSERT INTO item (ISBN_FK, ID_material_FK) VALUES ( {ISBN_FK}, {ID_material_FK})'
    cursor.execute(comando)
    conexao.commit()

#READ
def ler_item():
    comando = 'SELECT * FROM item'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

#UPDATE
def atualizar_item(ID_item, ISBN_FK, ID_material_FK):
    comando = f'UPDATE item SET ISBN_FK = {ISBN_FK}, ID_material_FK = {ID_material_FK} WHERE ID_item = {ID_item}'
    cursor.execute(comando)
    conexao.commit()

#DELETE
def deletar_item(ID_item):
    comando = f'DELETE FROM item WHERE ID_item = {ID_item}'
    cursor.execute(comando)
    conexao.commit()




class CadastraPessoa(QMainWindow):#OK!æ
    
    def __init__(self, widget,tipo):
        super(CadastraPessoa, self).__init__()
        uic.loadUi('cadastra.ui', self)
        self.setWindowTitle('Cadastro')
        self.setWindowIcon(QIcon("imgs\icons8-book-50.png"))   
        self.widget = widget 
        self.show()
        self.tipo = tipo
        self.userLogado = []

        self.cadastrarBtn.clicked.connect(self.cadastrar)
        self.VoltarBtn.clicked.connect(self.voltar)
        
        
        #se for membro, define a label TipoLabel como Membro
        self.labelDefinir()
        

    
    def cadastrar(self):
        if self.nomeTxt.text() == '' or self.sobrenomeTxt.text() == ''  or self.usernameTxt.text() == '' or self.senhaTxt.text() == '':
            QMessageBox.about(self, 'Erro!', 'Preencha todos os campos!')
        else:
            if self.tipo == 'MEM':
                inserir_usuario(self.nomeTxt.text(), self.sobrenomeTxt.text(),'MEM', self.usernameTxt.text(), self.senhaTxt.text(), self.imgTxt.text() )
            else:
                #se for a primeria vez que um ADM é cadastrado, ele é armazenado na variavel userLogado do mesmo modo que será salvo no banco de dados
                if len(ler_usuario()) == 0:
                    self.userLogado = [1, self.nomeTxt.text(), self.sobrenomeTxt.text(), 'ADM', self.usernameTxt.text(), self.senhaTxt.text(), self.imgTxt.text().encode('utf-8')]
                    inserir_usuario(self.nomeTxt.text(), self.sobrenomeTxt.text(),'ADM', self.usernameTxt.text(), self.senhaTxt.text(), self.imgTxt.text() )
                    #fecha a window
                    self.widget.close()
                else:    
                    inserir_usuario(self.nomeTxt.text(), self.sobrenomeTxt.text(),'ADM', self.usernameTxt.text(), self.senhaTxt.text(), self.imgTxt.text() )
                

            #vai para a tela anterior e remove o widget atual
            self.widget.removeWidget(self)
            self.widget.setCurrentIndex(0)
            QMessageBox.about(self, 'Sucesso!', 'Cadastro realizado com sucesso!')

    def voltar(self):
        self.widget.setCurrentIndex(0)

    def labelDefinir(self):
        if self.tipo == 'MEM':
            self.TipoLabel.setText("Membro")
        else:
            self.TipoLabel.setText("Administrador")

                       
class Login(QMainWindow):#OK!

    def __init__(self,widgetlogin):
        super(Login, self).__init__()
        uic.loadUi('login.ui', self)
        self.show()
        self.userLogado = []
        self.widget = widgetlogin
        self.pessoas = ler_usuario()

        self.loginBtn.clicked.connect(self.login)

    def login(self):
        self.userLogado = self.acha_login()
        if self.userLogado == []:
            QMessageBox.about(self, 'Erro!', 'Usuário ou senha incorretos!')
        else:
            QMessageBox.about(self, 'Sucesso!', 'Login realizado com sucesso!')
            #fecha o widget
            self.widget.close()
            
            


    def acha_login(self):
        if self.usernameTxt.text() == '' or self.senhaTxt.text() == '':
            QMessageBox.about(self, 'Erro!', 'Preencha todos os campos!')
        else:
            for usuario in self.pessoas:
                if usuario[4] == self.usernameTxt.text() and usuario[5] == self.senhaTxt.text():
                    return usuario
            return []
    
class MenuADM(QMainWindow):#OK!

    def __init__(self, userLogado, widget):
        super(MenuADM, self).__init__()
        uic.loadUi('MenuAdm.ui', self)
        for usuario in ler_usuario():
            if usuario[0] == userLogado[0]:
                userLogado = usuario
                break
        self.widget = widget

        self.perfBtn.clicked.connect(self.perfil)
        self.livroBtn.clicked.connect(self.livro)
        self.matBtn.clicked.connect(self.material)
        self.addLivroBtn.clicked.connect(self.newLivro)
        self.addMatBtn.clicked.connect(self.newMaterial)
        self.membrosbtn.clicked.connect(self.membros)
        self.admBtn.clicked.connect(self.newPessoa)
        self.lblNome.setText(userLogado[1])

    def perfil(self):
        self.widget.setCurrentIndex(1)

    def newLivro(self):
        self.widget.setCurrentIndex(2)

    def livro(self):
        #verifica se existe algum livro no banco de dados
        if len(ler_livro()) == 0:
            QMessageBox.about(self, 'Erro!', 'Não há livros cadastrados!')
        else:
            self.widget.setCurrentIndex(3)

    def newMaterial(self):
        self.widget.setCurrentIndex(4)

    def material(self):
        #verifica se existe algum material no banco de dados
        if len(ler_material()) == 0:
            QMessageBox.about(self, 'Erro!', 'Não há materiais cadastrados!')
        else:
            self.widget.setCurrentIndex(5)

    def membros(self):
        #verifica se existe algum membro no banco de dados
        membro = False
        for usuario in ler_usuario():
            if usuario[3] == 'MEM':
                membro = True
                break
        if membro == False:
            QMessageBox.about(self, 'Erro!', 'Não há membros cadastrados!')
        else:
            self.widget.setCurrentIndex(6)

        

    def newPessoa(self):
        #pergunta qual o tipo de usuario que deseja cadastrar
        if QMessageBox.question(self, 'Confirmação', 'Deseja cadastrar um ADM?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.widget.addWidget(CadastraPessoa(self.widget, 'ADM'))
            self.widget.setCurrentIndex(7)
        else:
            self.widget.addWidget(CadastraPessoa(self.widget, 'MEM'))
            self.widget.setCurrentIndex(7)
           
class CadastraLivro(QMainWindow):#OK!æ

    def __init__(self, widget):
        super(CadastraLivro, self).__init__()
        uic.loadUi('Cadastro_Livro.ui', self)
        self.show()
        self.widget = widget

        self.Botao_Confirma.clicked.connect(self.cadastrar)
        self.Botao_Volta.clicked.connect(self.cancelar)
    def cadastrar(self):
        if self.Titulo_txt.text() == ' ' or self.Autor_txt.text() == ' ' or self.ISBN_txt.text() == ' ' or self.Descricao_txt.toPlainText() == ' ' or self.Categoria_txt.text() == ' ' or self.Data_txt.text() == ' ' or self.Estado_Conservacao_txt.text() == ' ' or self.Localizacao_txt.text() == ' ' or self.URI_txt.text() == ' ' :
            QMessageBox.about(self, 'Erro!', 'Preencha todos os campos!')
        else: 
            inserir_livro(self.Titulo_txt.text(), self.Autor_txt.text(), self.ISBN_txt.text(), self.Descricao_txt.toPlainText(), self.Categoria_txt.text(), str(self.Data_txt.text()), self.Estado_Conservacao_txt.text(), self.Localizacao_txt.text(), self.URI_txt.text())
            inserir_item(self.ISBN_txt.text(), "NULL")
            QMessageBox.about(self, 'Sucesso!', 'Cadastro realizado com sucesso!')
            self.widget.setCurrentIndex(0)
    def cancelar(self):
        self.widget.setCurrentIndex(0)

class ADMLivro(QMainWindow):#OK!

    def __init__(self, widget):
        super(ADMLivro, self).__init__()
        uic.loadUi('LivroADM.ui', self)
        self.show()
        self.widget = widget
        self.i = 0
        self.livros = ler_livro()

        self.BotaoVoltar.clicked.connect(self.voltar)
        self.BotaoAnterior.clicked.connect(self.anterior)
        self.BotaoProximo.clicked.connect(self.proximo)
        self.BotaoSalvar.clicked.connect(self.salvar)
        self.BotaoExcluir.clicked.connect(self.excluir)

        #ativa o botao de proximo
        self.BotaoProximo.setEnabled(True)
        #desativa o botao de anterior
        self.BotaoAnterior.setEnabled(False)
        if len(self.livros) > 0:
            self.mostrar()

    def voltar(self):
        self.widget.setCurrentIndex(0)

    def anterior(self):
        if self.i > 0:
            self.i -= 1
            self.mostrar()
            #ativa o botao de proximo
            self.BotaoProximo.setEnabled(True)
        else:
            #desativa o botao de anterior
            self.BotaoAnterior.setEnabled(False)
            self.BotaoProximo.setEnabled(True)

    def proximo(self):
        if self.i < len(self.livros) - 1:
            self.i += 1
            self.mostrar()
            #ativa o botao de anterior
            self.BotaoAnterior.setEnabled(True)
        else:
            #desativa o botao de proximo
            self.BotaoProximo.setEnabled(False)
            self.BotaoAnterior.setEnabled(True)

    def salvar(self):
        if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja editar este livro?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            atualizar_livro(self.TituloTxt.text(), self.AutorTxt.text(), self.ISBNTxt.text(), self.DescricaoTxt.toPlainText(), self.CategoriaTxt.text(), str(self.DataTxt.text()), self.EstadoConservacaoTxt.text(), self.LocalizacaoTxt.text(), self.URITxt.text())
            QMessageBox.about(self, 'Sucesso!', 'Livro editado com sucesso!')
            self.widget.setCurrentIndex(0)

    def excluir(self):
        #localiza o item associado ao livro
        item = []
        for item1 in ler_item():
            if item1[1] == self.livros[self.i][2]:
                item = item1
                break
        #localiza os todos os emprestimos associados ao livro
        emps = []
        for emprestimo in ler_emprestimo():
            if emprestimo[5] == item[0]:
                emps.append(emprestimo)
        achou = False
        for emprestimo in emps:
            if emprestimo[3] == 'EMPRESTADO':
                achou = True
                break
        if achou == True:
            QMessageBox.about(self, 'Erro!', 'Não é possível excluir um livro com empréstimos pendentes!')
        else:
            if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja excluir este livro?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                #remove os emprestimos associados ao livro
                for emprestimo in emps:
                    deletar_emprestimo(emprestimo[0])
                #remove o item associado ao livro
                deletar_item(item[0])
                deletar_livro(self.livros[self.i][2])
                QMessageBox.about(self, 'Sucesso!', 'Livro excluído com sucesso!')
                self.i = 0
                self.mostrar()
                self.widget.setCurrentIndex(0)

    def mostrar(self):
        self.TituloTxt.setText(self.livros[self.i][0])
        self.AutorTxt.setText(self.livros[self.i][1])
        self.ISBNTxt.setText(str(self.livros[self.i][2]))
        self.DescricaoTxt.setText(self.livros[self.i][3])
        self.CategoriaTxt.setText(self.livros[self.i][4])
        self.DataTxt.setText(self.livros[self.i][5])
        self.EstadoConservacaoTxt.setText(self.livros[self.i][6])
        self.LocalizacaoTxt.setText(self.livros[self.i][7])
        self.URITxt.setText(self.livros[self.i][8].decode('utf-8'))

class CadastraMaterial(QMainWindow):#OK!

    def __init__(self, widget):
        super(CadastraMaterial, self).__init__()
        uic.loadUi('Cadastro_Material.ui', self) 
        self.show()
        self.widget = widget

        self.Botao_Confirma.clicked.connect(self.cadastrar)
        self.Botao_Volta.clicked.connect(self.cancelar)
    def cadastrar(self):
        if self.ID_txt.text() == ' ' or self.Numero_Serie_txt.text() == ' ' or self.Categoria_Txt.text() == ' ' or self.Categoria_Txt_2.text() == ' ' or self.Estado_Conservacao_txt.text() == ' '  or self.Localizacao_txt.text() == ' ' or self.URI_txt.text() == ' ' or self.Descricao_txt.toPlainText == ' ' :
            QMessageBox.about(self, 'Erro!', 'Preencha todos os campos!')
        else:
            inserir_mateiral(self.ID_txt.text(), self.Descricao_txt.toPlainText(), self.Categoria_Txt.text(), self.Numero_Serie_txt.text(), str(self.Categoria_Txt_2.text()), self.Estado_Conservacao_txt.text(), self.Localizacao_txt.text(), self.URI_txt.text())
            inserir_item("NULL", self.ID_txt.text())
            QMessageBox.about(self, 'Sucesso!', 'Cadastro realizado com sucesso!')
            self.widget.setCurrentIndex(0)
    def cancelar(self):
        self.widget.setCurrentIndex(0)

class ADMMaterial(QMainWindow):#OK!
    
        def __init__(self, widget):
            super(ADMMaterial, self).__init__()
            uic.loadUi('MaterialADM.ui', self)
            self.show()
            self.widget = widget
            self.i = 0
            self.materiais = ler_material()
    
            self.BotaoVoltar.clicked.connect(self.voltar)
            self.BotaoAnterior.clicked.connect(self.anterior)
            self.BotaoAvanca.clicked.connect(self.proximo)
            self.BotaoSalvar.clicked.connect(self.salvar)
            self.BotaoExcluir.clicked.connect(self.excluir)

            #ativa o botao de proximo
            self.BotaoAvanca.setEnabled(True)
            #desativa o botao de anterior
            self.BotaoAnterior.setEnabled(False)

            if len(self.materiais) > 0:
                self.mostrar()

        def voltar(self):
            self.widget.setCurrentIndex(0)

        def anterior(self):
            if self.i > 0:
                self.i -= 1
                self.mostrar()
                #ativa o botao de proximo
                self.BotaoAvanca.setEnabled(True)
            else:
                #desativa o botao de anterior
                self.BotaoAnterior.setEnabled(False)
                self.BotaoAvanca.setEnabled(True)

        def proximo(self):
            if self.i < len(self.materiais) - 1:
                self.i += 1
                self.mostrar()
                #ativa o botao de anterior
                self.BotaoAnterior.setEnabled(True)
            else:
                #desativa o botao de proximo
                self.BotaoAvanca.setEnabled(False)
                self.BotaoAnterior.setEnabled(True)

        def salvar(self):
            if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja editar este material?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                atualizar_material(self.IDTxt.text(), self.DescricaoTxt.toPlainText(), self.CategoriaTxt.text(), self.NumeroSerieTxt.text(), str(self.DataTxt.text()), self.EstadoConservacaoTxt.text(), self.LocalizacaoTxt.text(), self.URITxt.text())
                QMessageBox.about(self, 'Sucesso!', 'Material editado com sucesso!')
                self.widget.setCurrentIndex(0)

        def excluir(self):
            #localiza o item associado ao material
            item = []
            for item1 in ler_item():
                if item1[2] == self.materiais[self.i][0]:
                    item = item1
                    break
            #localiza os todos os emprestimos associados ao material
            emps = []
            for emprestimo in ler_emprestimo():
                if emprestimo[5] == item[0]:
                    emps.append(emprestimo)

            achou = False
            for emprestimo in emps:
                if emprestimo[3] == 'EMPRESTADO':
                    achou = True
                    break
            if achou == True:
                QMessageBox.about(self, 'Erro!', 'Não é possível excluir um material com empréstimos pendentes!')
            else:
                if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja excluir este material?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    #remove os emprestimos associados ao material
                    for emprestimo in emps:
                        deletar_emprestimo(emprestimo[0])
                    #remove o item associado ao material
                    deletar_item(item[0])
                    deletar_material(self.materiais[self.i][0])                  
                    QMessageBox.about(self, 'Sucesso!', 'Material excluído com sucesso!')
                    self.i = 0
                    self.mostrar()
                    self.widget.setCurrentIndex(0)

        def mostrar(self):
            self.IDTxt.setText(str(self.materiais[self.i][0]))
            self.DescricaoTxt.setText(self.materiais[self.i][1])
            self.CategoriaTxt.setText(self.materiais[self.i][2])
            self.NumeroSerieTxt.setText(str(self.materiais[self.i][3]))
            self.DataTxt.setText(self.materiais[self.i][4])
            self.EstadoConservacaoTxt.setText(self.materiais[self.i][5])
            self.LocalizacaoTxt.setText(self.materiais[self.i][6])
            self.URITxt.setText(self.materiais[self.i][7].decode('utf-8'))
    
    
        
        def cancelar(self):
            self.widget.setCurrentIndex(0)

class ADMMembros(QMainWindow):#OK!
        
    def __init__(self, widget):
        super(ADMMembros, self).__init__()
        uic.loadUi('MembroADM.ui', self)
        self.show()
        self.widget = widget
        self.i = 0
        #salva apenas os usuarios que não são ADM	
        self.usuarios = []
        for usuario in ler_usuario():
            if usuario[3] != 'ADM':
                self.usuarios.append(usuario)

        self.VoltarButton.clicked.connect(self.voltar)
        self.AnteriorButton.clicked.connect(self.anterior)
        self.AvancarButton.clicked.connect(self.proximo)
        self.EmpButton.clicked.connect(self.emprestimos)
        self.ExcluirButton.clicked.connect(self.excluir)
        self.SalvarButton.clicked.connect(self.salvar)

        if len(self.usuarios) != 0:
            self.mostrar()
        


        #ativa o botao de proximo
        self.AvancarButton.setEnabled(True)
        #desativa o botao de anterior
        self.AnteriorButton.setEnabled(False)

        if len(self.usuarios) > 0:
            self.mostrar()
        


    def emprestimos(self):
        self.widget.addWidget(EmpsCliente(self.widget, self.usuarios[self.i]))
        self.widget.setCurrentIndex(7)
 
    def voltar(self):
        self.widget.setCurrentIndex(0)

    def anterior(self):
        if self.i > 0:
            self.i -= 1
            self.mostrar()
            #ativa o botao de proximo
            self.AvancarButton.setEnabled(True)
        else:
            #desativa o botao de anterior
            self.AnteriorButton.setEnabled(False)
            self.AvancarButton.setEnabled(True)
    
    def proximo(self):
        if self.i < len(self.usuarios) - 1:
            self.i += 1
            self.mostrar()
            #ativa o botao de anterior
            self.AnteriorButton.setEnabled(True)
        else:
            #desativa o botao de proximo
            self.AvancarButton.setEnabled(False)
            self.AnteriorButton.setEnabled(True)

    def mostrar(self):
        self.NomeTxt.setText(self.usuarios[self.i][1])
        self.SobrenomeTxt.setText(self.usuarios[self.i][2])
        self.LoginTxt.setText(self.usuarios[self.i][4])
        self.SenhaTxt.setText(self.usuarios[self.i][5])
        self.LinkTxt.setText(self.usuarios[self.i][6].decode('utf-8'))

    def excluir(self):
        #localiza os todos os emprestimos associados ao usuario
        emps = []
        for emprestimo in ler_emprestimo():
            if emprestimo[4] == self.usuarios[self.i][0]:
                emps.append(emprestimo)
        #verifica se o usuario tem emprestimos pendentes
        achou = False
        for emprestimo in emps:
            if emprestimo[3] == 'EMPRESTADO':
                achou = True
                break
        if achou == True:
            QMessageBox.about(self, 'Erro!', 'Não é possível excluir um membro com empréstimos pendentes!')
        else:
            if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja excluir este membro?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                #remove os emprestimos associados ao usuario
                for emprestimo in emps:
                    deletar_emprestimo(emprestimo[0])
                deletar_usuario(self.usuarios[self.i][0])
                QMessageBox.about(self, 'Sucesso!', 'Membro excluído com sucesso!')
                self.widget.setCurrentIndex(0)
    
    def salvar(self):
        if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja editar este membro?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            atualizar_usuario(self.usuarios[self.i][0], self.NomeTxt.text(), self.SobrenomeTxt.text(), self.usuarios[self.i][3], self.LoginTxt.text(), self.SenhaTxt.text(), self.LinkTxt.text())
            QMessageBox.about(self, 'Sucesso!', 'Membro editado com sucesso!')
            self.widget.setCurrentIndex(6)

class EmpsCliente(QMainWindow):#OK!æ

    def __init__(self, widget, cliente):
        super(EmpsCliente, self).__init__()
        uic.loadUi('EmpADM.ui', self)
        self.show()
        self.widget = widget
        self.i = 0
        self.cliente = cliente
        self.emprestimos = []
        for emprestimo in ler_emprestimo():
            if emprestimo[4] == cliente[0]:
                self.emprestimos.append(emprestimo)
        
        self.pushButton.clicked.connect(self.excluir)
        self.VoltarButton.clicked.connect(self.voltar)
        self.RemoveButton.clicked.connect(self.anterior)
        self.AvancarButton.clicked.connect(self.proximo)

        #ativa o botao de proximo
        self.AvancarButton.setEnabled(True)
        self.RemoveButton.setEnabled(False)
        if len(self.emprestimos) > 0:
            self.mostrar()


    def voltar(self):
        self.widget.removeWidget(self)
        self.widget.setCurrentIndex(6)

    def anterior(self):
        if self.i > 0:
            self.i -= 1
            self.mostrar()
            #ativa o botao de proximo
            self.AvancarButton.setEnabled(True)
        else:
            #desativa o botao de anterior
            self.RemoveButton.setEnabled(False)
            self.AvancarButton.setEnabled(True)

    def proximo(self):
        if self.i < len(self.emprestimos) - 1:
            self.i += 1
            self.mostrar()
            #ativa o botao de anterior
            self.RemoveButton.setEnabled(True)
        else:
            #desativa o botao de proximo
            self.AvancarButton.setEnabled(False)
            self.RemoveButton.setEnabled(True)

    def excluir(self):#altera o estado do emprestimo para devolvido caso ele esteja emprestado
        if self.emprestimos[self.i][3] == 'EMPRESTADO':
            if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja devolver este item de um membro?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                atualizar_emprestimo(self.emprestimos[self.i][0], self.emprestimos[self.i][1], self.emprestimos[self.i][2], 'DEVOLVIDO', self.emprestimos[self.i][4], self.emprestimos[self.i][5])
                QMessageBox.about(self, 'Sucesso!', 'Item devolvido com sucesso!')
                self.widget.setCurrentIndex(0)
        else:
            QMessageBox.about(self, 'Erro!', 'Este item já foi devolvido!')
             
    def mostrar(self):
        #localiza o item que está no empréstimo i, em seguida, verifica se o item é um livro ou material e busca salva os dados do item em uma variavel
        for item in ler_item():
            if item[0] == self.emprestimos[self.i][5]:
                if item[2] == None :
                    for livro in ler_livro():
                        if livro[2] == item[1]:
                            self.TituloLabel.setText(livro[0])
                            self.CategoriaLabel.setText(livro[4])
                            self.DataLabel.setText(self.emprestimos[self.i][2])
                            self.EstadoLabel.setText(livro[6])
                            self.LocalizacaoLabel.setText(livro[7])
                            self.URILabel.setText(livro[8].decode('utf-8'))
                            break
                else:
                    for material in ler_material():
                        if material[0] == item[2]:
                            self.TituloLabel.setText(str(material[0]))
                            self.CategoriaLabel.setText(material[2])
                            self.DataLabel.setText(self.emprestimos[self.i][2])
                            self.EstadoLabel.setText(material[5])
                            self.LocalizacaoLabel.setText(material[6])
                            self.URILabel.setText(material[7].decode('utf-8'))
                            break
                break
        
class MenuMEM(QMainWindow):#OK!

    def __init__(self, userLogado, widget):
        super(MenuMEM, self).__init__()
        uic.loadUi('MenuMembro.ui', self)
        #busca no banco de dados os dados mais recentes do usuario usando o ID como base
        for usuario in ler_usuario():
            if usuario[0] == userLogado[0]:
                self.userLogado = usuario
                break

        self.widget = widget

        self.ContaButton.clicked.connect(self.perfil)
        self.LivroButton.clicked.connect(self.livro)
        self.MateriaisButton.clicked.connect(self.material)
        self.DevolucoesButton.clicked.connect(self.emprestimo)
        self.label.setText(userLogado[1])

    def perfil(self):
        self.widget.setCurrentIndex(1)

    def livro(self):
        #verifica se existe algum livro no banco de dados
        if len(ler_livro()) == 0:
            QMessageBox.about(self, 'Erro!', 'Não há livros cadastrados!')
        else:
            self.widget.setCurrentIndex(2)

    def material(self):
        #verifica se existe algum material no banco de dados
        if len(ler_material()) == 0:
            QMessageBox.about(self, 'Erro!', 'Não há materiais cadastrados!')
        else:
            self.widget.setCurrentIndex(3)
    
    def emprestimo(self):
        #verifica se o usuario tem emprestimos
        achou = False
        for emprestimo in ler_emprestimo():
            if emprestimo[4] == self.userLogado[0]:
                achou = True
                break
        
        if achou == False:
            QMessageBox.about(self, 'Erro!', 'Você não possui empréstimos!')
        else:
            self.widget.setCurrentIndex(4)
    
class Perfil(QMainWindow):#OK!

    def __init__(self, userLogado, widget):
        super(Perfil, self).__init__()
        uic.loadUi('Conta.ui', self)
    
        self.userLogado = userLogado

        self.widget = widget

        #carrega os dados do usuario nos campos e permite a edição caso seja administrador
        self.nomeTxt.setText(self.userLogado[1])
        self.sobrenomeTxt.setText(self.userLogado[2])
        self.loginTxt.setText(self.userLogado[4])
        self.senhaTxt.setText(self.userLogado[5])
        self.linkTxt.setText(self.userLogado[6].decode('utf-8'))
        if self.userLogado[3] == 'ADM':
            self.LabelFunc.setText('Administrador')
        else:
            self.LabelFunc.setText('Membro')
            
    
        
        self.excluirBtn.clicked.connect(self.excluir)
        self.editarBtn.clicked.connect(self.editar)
        self.voltarBtn.clicked.connect(self.voltar)

        #se o usuario for um membro não permitir a alteração dos dados
        if self.userLogado[3] == 'MEM':
            self.nomeTxt.setEnabled(False)
            self.sobrenomeTxt.setEnabled(False)
            self.loginTxt.setEnabled(False)
            self.senhaTxt.setEnabled(False)
            self.linkTxt.setEnabled(False)
            self.editarBtn.setEnabled(False)


    def editar(self):
        #pergunta se o usuario tem certeza que deseja editar
        if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja editar seus dados?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            atualizar_usuario(self.userLogado[0], self.nomeTxt.text(), self.sobrenomeTxt.text(), self.userLogado[3], self.loginTxt.text(), self.senhaTxt.text(), self.linkTxt.text())
            QMessageBox.about(self, 'Sucesso!', 'Dados editados com sucesso!')
            self.widget.setCurrentIndex(0)

    def voltar(self):
        self.widget.setCurrentIndex(0)

    def excluir(self):
        #verifica se o usuario é membro e tem emprestimos pendentes
        if self.userLogado[3] == 'MEM':
            achou = False	
            for emprestimo in ler_emprestimo():
                if emprestimo[4] == self.userLogado[0] and emprestimo[3] == 'EMPRESTADO':
                    achou = True
            
            if achou == True:
                QMessageBox.about(self, 'Erro!', 'Você não pode excluir sua conta com empréstimos pendentes!')
            else:
                if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja excluir sua conta?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    #localiza os empresimos do usuario e os exclui
                    for emprestimo in ler_emprestimo():
                        if emprestimo[4] == self.userLogado[0]:
                            deletar_emprestimo(emprestimo[0])
                    deletar_usuario(self.userLogado[0])
                    QMessageBox.about(self, 'Sucesso!', 'Conta excluída com sucesso!')
                    #fecha o widget
                    self.widget.close()
        else:
            #permite o administrador excluir a excluir sua propria conta caso exista mais de um administrador
            n = 0
            for usuario in ler_usuario():
                if usuario[3] == 'ADM':
                    n += 1
            if n > 1:
                if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja excluir sua conta?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    deletar_usuario(self.userLogado[0])
                    QMessageBox.about(self, 'Sucesso!', 'Conta excluída com sucesso!')
                    #fecha o widget
                    self.widget.close()
            else:
                QMessageBox.about(self, 'Erro!', 'Não é possível excluir a conta de um único administrador!')
            
class BuscarLivroMEM(QMainWindow):#OK!

    def __init__(self, widget, userLogado):
        super(BuscarLivroMEM, self).__init__()
        uic.loadUi('Livro.ui', self)
        self.userLogado = userLogado
        self.widget = widget
        self.i = 0
        #salva apenas os livros que não estão em um empréstimo não devolvido
        self.livros = ler_livro()


        self.BotaoVoltar.clicked.connect(self.voltar)
        self.BotaoAnterior.clicked.connect(self.anterior)
        self.BotaoProximo.clicked.connect(self.proximo)
        self.BotaoEmprestimo.clicked.connect(self.emprestar)

        #ativa o botao de proximo
        self.BotaoProximo.setEnabled(True)
        #desativa o botao de anterior
        self.BotaoAnterior.setEnabled(False)
        if len(self.livros) != 0:

            self.mostrar()
        

    def emprestar(self):
        livro = self.livros[self.i]
        todos_itens = ler_item()
        todos_emprestimos = ler_emprestimo()
        achou = False
        for emprestimo in todos_emprestimos:
            for item in todos_itens:
                if item[0] == emprestimo[5] and livro[2] == item[1] and emprestimo[3] == 'EMPRESTADO':
                    achou = True
                    break
        if achou == False:
            if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja fazer um empréstimo deste livro?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                #insere o emprestimo no banco de dados
                data = datetime.datetime.now()
                datadevol = data + datetime.timedelta(days=7)
                data = data.strftime('%d/%m/%Y')
                datadevol = datadevol.strftime('%d/%m/%Y')
                for item in ler_item():
                    if item[1] == self.livros[self.i][2]:
                        inserir_emprestimo(data, datadevol, 'EMPRESTADO', self.userLogado[0], item[0])
                        QMessageBox.about(self, 'Sucesso!', 'Empréstimo feito com sucesso!')
                        self.widget.setCurrentIndex(0)
                        break
                
        else:
            QMessageBox.about(self, 'Erro!', 'Este livro já está emprestado!')
    def voltar(self):
        self.widget.setCurrentIndex(0)

    def anterior(self):
        if self.i > 0:
            self.i -= 1
            self.mostrar()
            #ativa o botao de proximo
            self.BotaoProximo.setEnabled(True)
        else:
            #desativa o botao de anterior
            self.BotaoAnterior.setEnabled(False)
            self.BotaoProximo.setEnabled(True)
    
    def proximo(self):
        if self.i < len(self.livros) - 1:
            self.i += 1
            self.mostrar()
            #ativa o botao de anterior
            self.BotaoAnterior.setEnabled(True)
        else:
            #desativa o botao de proximo
            self.BotaoProximo.setEnabled(False)
            self.BotaoAnterior.setEnabled(True)

    def mostrar(self):
        self.LivrosLabel.setText(self.livros[self.i][0])
        self.AutorTxt.setText(self.livros[self.i][1])
        self.ISBNTxt.setText(str(self.livros[self.i][2]))
        self.DescricaoTxt.setText(self.livros[self.i][3])
        self.CategoriaTxt.setText(self.livros[self.i][4])
        self.DataTxt.setText(self.livros[self.i][5])
        self.EstadoConservacao.setText(self.livros[self.i][6])
        self.LocalizacaoTxt.setText(self.livros[self.i][7])
        self.URITxt.setText(self.livros[self.i][8].decode('utf-8'))

class BuscarMaterialMEM(QMainWindow):#OK

    def __init__(self, widget, userLogado):
        super(BuscarMaterialMEM, self).__init__()
        uic.loadUi('Material.ui', self)
        self.userLogado = userLogado
        self.widget = widget
        self.i = 0
        self.materiais = ler_material()

        self.BotaoVoltar.clicked.connect(self.voltar)
        self.BotaoAnterior.clicked.connect(self.anterior)
        self.BotaoAvanca.clicked.connect(self.proximo)
        self.BotaoEmprestimo.clicked.connect(self.emprestar)

        #ativa o botao de proximo
        self.BotaoAvanca.setEnabled(True)
        #desativa o botao de anterior
        self.BotaoAnterior.setEnabled(False)
        if len(self.materiais) != 0:
            self.mostrar()
        
    def emprestar(self):
        achou = False
        material = self.materiais[self.i]
        todos_itens = ler_item()
        todos_emprestimos = ler_emprestimo()
        for emprestimo in todos_emprestimos:
            for item in todos_itens:
                if item[0] == emprestimo[5] and material[0] == item[2] and emprestimo[3] == 'EMPRESTADO':
                    achou = True
                    break
        if achou == False:
            if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja fazer um empréstimo deste material?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                #insere o emprestimo no banco de dados
                data = datetime.datetime.now()
                datadevol = data + datetime.timedelta(days=7)
                data = data.strftime('%d/%m/%Y')
                datadevol = datadevol.strftime('%d/%m/%Y')
                #acha a fk do item que está sendo emprestado
                for item in ler_item():
                    if item[2] == self.materiais[self.i][0]:
                        inserir_emprestimo(data, datadevol, 'EMPRESTADO', self.userLogado[0], item[0])
                        break
                QMessageBox.about(self, 'Sucesso!', 'Empréstimo feito com sucesso!')
                self.widget.setCurrentIndex(0)
        else:
            QMessageBox.about(self, 'Erro!', 'Este material já está emprestado!')

    def voltar(self):
        self.widget.setCurrentIndex(0)

    def anterior(self):
        if self.i > 0:
            self.i -= 1
            self.mostrar()
            #ativa o botao de proximo
            self.BotaoAvanca.setEnabled(True)
        else:
            #desativa o botao de anterior
            self.BotaoAnterior.setEnabled(False)
            self.BotaoAvanca.setEnabled(True)

    def proximo(self):
        
            if self.i < len(self.materiais) - 1:
                self.i += 1
                self.mostrar()
                #ativa o botao de anterior
                self.BotaoAnterior.setEnabled(True)
            else:
                #desativa o botao de proximo
                self.BotaoAvanca.setEnabled(False)
                self.BotaoAnterior.setEnabled(True)

    def mostrar(self):
        self.IDTxt.setText(str(self.materiais[self.i][0]))
        self.DescricaoTxt.setText(self.materiais[self.i][1])
        self.CategoriaTxt.setText(self.materiais[self.i][2])
        self.NumeroSerieTxt.setText(str(self.materiais[self.i][3]))
        self.DataTxt.setText(self.materiais[self.i][4])
        self.EstadoConservacaoTxt.setText(self.materiais[self.i][5])
        self.LocalizacaoTxt.setText(self.materiais[self.i][6])
        self.URITxt.setText(self.materiais[self.i][7].decode('utf-8'))

class ConsultarEmpsMEM(QMainWindow):#OK

    def __init__(self, widget, userLogado):
        super(ConsultarEmpsMEM, self).__init__()
        uic.loadUi('Devolucao.ui', self)
        for usuario in ler_usuario():
            if usuario[0] == userLogado[0]:
                userLogado = usuario
                break
        self.widget = widget
        self.i = 0
        self.emprestimos = []
        for emprestimo in ler_emprestimo():
            if emprestimo[4] == userLogado[0]:
                self.emprestimos.append(emprestimo)
        
        self.devolverBtn.clicked.connect(self.devolver)
        self.voltarBtn.clicked.connect(self.voltar)
        self.antBtn.clicked.connect(self.anterior)
        self.proxBtn.clicked.connect(self.proximo)
        #deixa o botao de anterior desativado
        self.antBtn.setEnabled(False)
        self.proxBtn.setEnabled(True)
        if len(self.emprestimos) != 0:
            self.mostrar()
        
        

    def voltar(self):
        self.widget.setCurrentIndex(0)

    def anterior(self):
        if self.i > 0:
            self.i -= 1
            self.mostrar()
            #ativa o botao de proximo
            self.proxBtn.setEnabled(True)
        else:
            #desativa o botao de anterior
            self.antBtn.setEnabled(False)
            self.proxBtn.setEnabled(True)

    def proximo(self):
        if self.i < len(self.emprestimos) - 1:
            self.i += 1
            self.mostrar()
            #ativa o botao de anterior
            self.antBtn.setEnabled(True)
        else:
            #desativa o botao de proximo
            self.proxBtn.setEnabled(False)
            self.antBtn.setEnabled(True)

    def devolver(self):
        if QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja devolver o item?', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            atualizar_emprestimo(self.emprestimos[self.i][0], self.emprestimos[self.i][1], self.emprestimos[self.i][2], 'DEVOLVIDO', self.emprestimos[self.i][4], self.emprestimos[self.i][5])
            QMessageBox.about(self, 'Sucesso!', 'Item devolvido com sucesso!')
            self.widget.setCurrentIndex(0)
    

    def mostrar(self):
        if self.emprestimos != []:    
            #verifica se o emprestimo ja foi devolvido
            titulo = ''
            if self.emprestimos[self.i][3] == 'DEVOLVIDO':
                self.devolverBtn.setEnabled(False)
            else:
                self.devolverBtn.setEnabled(True)
            #busca dentro de livro ou material o titulo do item
            todos_itens = ler_item()
            for item in todos_itens:
                if item[0] == self.emprestimos[self.i][5]:
                    for livro in ler_livro():
                        if livro[2] == item[1]:
                            titulo = "Livro : " + str(livro[1])
                            break
                    for material in ler_material():
                        if material[0] == item[2]:
                            titulo = material[1]
                            titulo = "Material : " + material[1]
                            break
                    break
            self.dataEmpTxt.setText(self.emprestimos[self.i][1])
            self.dataDevTxt.setText(self.emprestimos[self.i][2])
            self.statusTxt.setText(self.emprestimos[self.i][3])
            self.tituloItemTxt.setText(titulo)


def main():
    flag = False

    app = QtWidgets.QApplication([])
    widget = QtWidgets.QStackedWidget()
    
    
    widget.setWindowTitle('Login')
    widget.setWindowIcon(QIcon("imgs\icons8-book-50.png"))
    
    if ler_usuario() == []:
        CadastroAtual = CadastraPessoa(widget, 'ADM')
        widget.addWidget(CadastroAtual)
        widget.setCurrentIndex(0)
        flag = True
    else:
        LoginAtual = Login(widget)
        widget.addWidget(LoginAtual)
        widget.addWidget(CadastraPessoa(widget, 'MEM'))
        widget.setCurrentIndex(0)
        

    widget.setMinimumHeight(500)
    widget.setMinimumWidth(800)
    widget.show()
    app.exec_()

    if flag == True:
        userLogado = CadastroAtual.userLogado
    else:
        userLogado = LoginAtual.userLogado

    
    app2 = QtWidgets.QApplication([])
    widget2 = QtWidgets.QStackedWidget()
    widget2.setWindowIcon(QIcon("imgs\icons8-book-50.png"))
    
    #verifica se existe algum usuario logado
    if userLogado == [] or userLogado == None:
        pass
    else:
        if userLogado[3] == 'ADM':
            widget2.setWindowTitle('ADM')
            #menu adm 0
            widget2.addWidget(MenuADM(userLogado, widget2))
            #tela de perfil 1
            widget2.addWidget(Perfil(userLogado, widget2))
            #tela de adicionar livro 2
            widget2.addWidget(CadastraLivro(widget2))
            #tela de buscar livro 3
            widget2.addWidget(ADMLivro(widget2))
            #tela de adicionar 4
            widget2.addWidget(CadastraMaterial(widget2))
            #tela de buscar material e editar 5
            widget2.addWidget(ADMMaterial(widget2))
            #tela de consultar membros 6
            widget2.addWidget(ADMMembros(widget2))
            #tela de consultar emprestimos 
            #é adicionada apenas quando o usuario clica no botao de emprestimos   
            widget2.setMinimumHeight(800)
            widget2.setMinimumWidth(800)  
            widget2.show()
            app2.exec_()     
        elif userLogado[3] == 'MEM':
            widget2.setWindowTitle('Membros')
            #menu cliente 0
            widget2.addWidget(MenuMEM(userLogado, widget2))
            #tela de perfil 1
            widget2.addWidget(Perfil(userLogado, widget2))
            #tela de buscar livro(solicitar emprestimo) 2
            widget2.addWidget(BuscarLivroMEM(widget2, userLogado))
            #tela de buscar material(solicitar emprestimo) 3
            widget2.addWidget(BuscarMaterialMEM(widget2, userLogado))
            #tela de consultar emprestimos e devolver 4
            widget2.addWidget(ConsultarEmpsMEM(widget2, userLogado))
            widget2.setMinimumHeight(800)
            widget2.setMinimumWidth(800)  
            widget2.show()
            app2.exec_() 


       
    
  
if __name__ == '__main__':
    main()
cursor.close()
conexao.close()