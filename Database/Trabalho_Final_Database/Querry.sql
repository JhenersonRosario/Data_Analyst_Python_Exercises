CREATE TABLE Enderecos(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Rua VARCHAR(255),
    RuaNumero VARCHAR(10),
    Cidade VARCHAR(255),
    Bairro VARCHAR(255),
    CEP INT(8),
    UF CHAR(2)
);

CREATE TABLE Fornecedores (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeEmpresa VARCHAR(255),
    EnderecoID INT,
    FOREIGN KEY (EnderecoID) REFERENCES Enderecos(ID)
);

CREATE TABLE Clientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeEmpresa VARCHAR(255),
    EnderecoID INT,
    FOREIGN KEY (EnderecoID) REFERENCES Enderecos(ID)
);


CREATE TABLE Camisetas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NomeModelo VARCHAR(255),
    Descricao TEXT,
    Preco DECIMAL(10,2)
);

CREATE TABLE Vendas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    DataVenda DATE,
    ClienteID INT,
    CamisetaID INT,
    QuantidadeVendida INT,
    ValorTotal DECIMAL(10, 2),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID),
    FOREIGN KEY (CamisetaID) REFERENCES Camisetas(ID)
);