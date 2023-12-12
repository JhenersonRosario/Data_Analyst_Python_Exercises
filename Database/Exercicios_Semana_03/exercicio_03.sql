CREATE TABLE Categorias (
    CategoriaID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(50) NOT NULL
);

CREATE TABLE Subcategorias (
    SubcategoriaID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(50) NOT NULL,
    CategoriaID INT,
    CONSTRAINT FK_Categoria_Subcategoria FOREIGN KEY (CategoriaID) REFERENCES Categorias(CategoriaID)
);

CREATE TABLE Usuarios (
    UsuarioID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    DataCadastro DATE,
    Plano VARCHAR(50)
);


CREATE TABLE Videos (
    VideoID INT PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(255) NOT NULL,
    DuracaoMinutos INT,
    CategoriaID INT,
    SubcategoriaID INT,
    CONSTRAINT FK_Categoria_Video FOREIGN KEY (CategoriaID) REFERENCES Categorias(CategoriaID),
    CONSTRAINT FK_Subcategoria_Video FOREIGN KEY (SubcategoriaID) REFERENCES Subcategorias(SubcategoriaID)
);

CREATE TABLE Visualizacoes (
    VisualizacaoID INT PRIMARY KEY AUTO_INCREMENT,
    UsuarioID INT,
    VideoID INT,
    TempoAssistidoMinutos INT,
    Pausas INT,
    DataVisualizacao DATE,
    CONSTRAINT FK_Usuario_Visualizacao FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID),
    CONSTRAINT FK_Video_Visualizacao FOREIGN KEY (VideoID) REFERENCES Videos(VideoID)
);