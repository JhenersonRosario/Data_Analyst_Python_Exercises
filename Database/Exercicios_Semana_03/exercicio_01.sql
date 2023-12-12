CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255),
    Email VARCHAR(255) UNIQUE NOT NULL,
    DataCadastro DATE,
    ComprasRealizadas INT DEFAULT 0,
    EnderecoEntregaID INT
);

CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255),
    Preco DECIMAL(10, 2),
    Descricao TEXT
);

CREATE TABLE Enderecos (
    EnderecoID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    Rua VARCHAR(255),
    Cidade VARCHAR(255),
    Estado VARCHAR(255),
    CEP VARCHAR(10)
);

CREATE TABLE Compras (
    CompraID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    DataCompra DATE,
    ValorTotal DECIMAL(10, 2),
    CONSTRAINT FK_Cliente FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

CREATE TABLE ItensCompra (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,
    CompraID INT,
    ProdutoID INT,
    Quantidade INT,
    CONSTRAINT FK_Compra FOREIGN KEY (CompraID) REFERENCES Compras(CompraID),
    CONSTRAINT FK_Produto FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);


CREATE TABLE Brindes (
    BrindeID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    DataResgate DATE,
    CONSTRAINT FK_ClienteBrinde FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);