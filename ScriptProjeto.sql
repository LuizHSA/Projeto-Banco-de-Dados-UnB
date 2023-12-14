create database if not exists biblioteca;

use biblioteca;

CREATE TABLE IF NOT EXISTS usuario (
    ID_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    funcao VARCHAR(100) NOT NULL,
    login VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    URI_foto_usuario BLOB NOT NULL
);


CREATE TABLE IF NOT EXISTS livro (
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    ISBN BIGINT PRIMARY KEY,
    descricao VARCHAR(1000) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    data_aquisicao VARCHAR(11) NOT NULL,
    estado_conservacao VARCHAR(100) NOT NULL,
    localizacao_fisica VARCHAR(100) NOT NULL,
    URI_foto_capa BLOB NOT NULL
);

CREATE TABLE IF NOT EXISTS material (
    ID_material INT PRIMARY KEY,
    descricao VARCHAR(1000) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    numero_de_serie INT NOT NULL,
    data_aquisicao VARCHAR(11) NOT NULL,
    estado_conservacao VARCHAR(100) NOT NULL,
    localizacao_fisica VARCHAR(100) NOT NULL,
    URI_foto_material BLOB NOT NULL
);



CREATE TABLE IF NOT EXISTS item (
    ID_item INT PRIMARY KEY AUTO_INCREMENT,
    ISBN_FK BIGINT,
    ID_material_FK INT,
    FOREIGN KEY (ISBN_FK)
        REFERENCES livro (ISBN),
    FOREIGN KEY (ID_material_FK)
        REFERENCES material (ID_material)
);

CREATE TABLE IF NOT EXISTS emprestimo (
    ID_emprestimo INT PRIMARY KEY AUTO_INCREMENT,
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE NOT NULL,
    status_emprestimo VARCHAR(100) NOT NULL,
    ID_usuario_FK INT NOT NULL,
    ID_item_FK INT NOT NULL,
    FOREIGN KEY (ID_usuario_FK)
        REFERENCES usuario (ID_usuario),
    FOREIGN KEY (ID_item_FK)
        REFERENCES item (ID_item)
);

