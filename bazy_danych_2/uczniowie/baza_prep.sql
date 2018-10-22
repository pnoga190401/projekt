DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS klasy;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie (
id INTEGER PRIMARY KEY AUTOINCREMENT,
imie TEXT(15),
nazwisko TEXT(20),
plec BOOLEAN(2),
id_klasa INTEGER(2),
egz_hum NUMERIC(2),
egz_jez NUMERIC(2),
FOREIGN KEY (id_klasa) REFERENCES klasy(id)
);

CREATE TABLE klasy (
id INTEGER PRIMARY KEY AUTOINCREMENT,
klasa INTEGER(2),
rok_naboru INTEGER(4),
rok_matury INTEGER(4)

);

CREATE TABLE przedmioty (
id INTEGER PRIMARY KEY AUTOINCREMENT,
przedmiot TEXT(15),
imie_naucz TEXT(15) DEFAULT "",
nazwisko_naucz INTEGER(20) DEFAULT "",
plec_naucz TEXT(1) DEFAULT ""
);

CREATE TABLE oceny (
id INTEGER PRIMARY KEY AUTOINCREMENT,
datad DATE(15),
id_uczen INTEGER(3),
id_przedmiot INTEGER(3),
oceny DECIMAL,
FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);
