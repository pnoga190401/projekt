CREATE TABLE ucznowie (
	id_ucz CHAR(8) PRIMARY KEY,
	imie VARCHAR(30) NOT NULL,
	nazwisko VARCHAR(30) NOT NULL,
	klasa CHAR(4) DEFAULT
);

CREATE TABLE oceny (
	id_oceny INTEGER PRIMARY KEY AUTO_INCREMENT,
	data DATE(30),
	id_ucz CHAR(8) NOT NULL,
	id_przedm INTEGER,
	ocena DECIMAL(3,2)
	FOREIGN KEY (id_ucz) REFERENCES (uczniowie, id_ucz)
	ON DELETE CASCADE
);

#tabela slownikowa
CREATE TABLE przedmioty (
	id_przedm INTEGER PRIMARY KEY AUTO_INCREMENT,
	nazwa VARCHAR(30) NOT NULL
);

#ang constraints