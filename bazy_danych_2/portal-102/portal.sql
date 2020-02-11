DROP TABLE IF EXISTS uzytkownicy;
CREATE TABLE uzytkownicy (
	idu CHAR(8) PRIMARY KEY AUTOINCREMENT,
	imie VARCHAR(30) NOT NULL CHECK(imie <> ''),
	nazwisko VARCHAR(30) NOT NULL CHECK(nazwisko <> ''),
	idp INTEGER REFERENCES panstwa(id
	plec CHAR(1)
);

DROP TABLE IF EXISTS zdjecia;
CREATE TABLE zdjecia (
	id_zdjecia INTEGER PRIMARY KEY AUTOINCREMENT,
	data DATE NOT NULL(30),
	idu INTEGER REFERENCES uzytkownicy(idu),
	szerokosc INTEGER,
	wysokosc INTEGER,
	FOREIGN KEY (idu) REFERENCES (uzytkownicy, idu)
	ON DELETE CASCADE
);

DROP TABLE IF EXISTS znajomosci;
CREATE TABLE znajomosci (
	idu_1 INTEGER NOT NULL REFERENCES uzytkowicy(idu) ON DELETE CASCADE,
	idu_1 INTEGER NOT NULL REFERENCES uzytkowicy(idu) ON DELETE CASCADE,
    data DATE(30)
	nazwa VARCHAR(30) NOT NULL
);

DROP TABLE IF EXISTS panstwa;
CREATE TABLE panstwa (
	idp INTEGER PRIMARY KEY AUTOINCREMENT,
	nazwa VARCHAR(30) NOT NULL
);

#ang constraints
