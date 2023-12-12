CREATE TABLE Participantes (
    ParticipanteID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    DataNascimento DATE,
    Sexo ENUM('Masculino', 'Feminino', 'Outro'),
    Altura DECIMAL(5, 2),
    Peso DECIMAL(5, 2),
    EquipeID INT
);


CREATE TABLE Equipes (
    EquipeID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    Cidade VARCHAR(255),
    TreinadorID INT
);

CREATE TABLE Treinadores (
    TreinadorID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(255) NOT NULL,
    DataNascimento DATE,
    Sexo ENUM('Masculino', 'Feminino', 'Outro')
);


CREATE TABLE Partidas (
    PartidaID INT PRIMARY KEY AUTO_INCREMENT,
    DataPartida DATE,
    HoraPartida TIME,
    Local VARCHAR(255),
    EquipeCasaID INT,
    EquipeVisitanteID INT
);

CREATE TABLE Placares (
    PlacarID INT PRIMARY KEY AUTO_INCREMENT,
    PartidaID INT,
    EquipeID INT,
    Pontos INT
);

ALTER TABLE Participantes ADD CONSTRAINT FK_Equipe_Participante FOREIGN KEY (EquipeID) REFERENCES Equipes(EquipeID);

ALTER TABLE Equipes ADD CONSTRAINT FK_Treinador_Equipe FOREIGN KEY (TreinadorID) REFERENCES Treinadores(TreinadorID);

ALTER TABLE Partidas ADD CONSTRAINT FK_EquipeCasa_Partida FOREIGN KEY (EquipeCasaID) REFERENCES Equipes(EquipeID);
ALTER TABLE Partidas ADD CONSTRAINT FK_EquipeVisitante_Partida FOREIGN KEY (EquipeVisitanteID) REFERENCES Equipes(EquipeID);

ALTER TABLE Placares ADD CONSTRAINT FK_Partida_Placar FOREIGN KEY (PartidaID) REFERENCES Partidas(PartidaID);
ALTER TABLE Placares ADD CONSTRAINT FK_Equipe_Placar FOREIGN KEY (EquipeID) REFERENCES Equipes(EquipeID);