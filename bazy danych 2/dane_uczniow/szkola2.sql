DROP TABLE IF EXISTS oceny;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS uczniowie;

CREATE TABLE oceny (
id_ucznia INTEGER NOT NULL,
ocena INTEGER(3),
data_ DATE(10),
id_przedmiotu TEXT(1)
);

CREATE TABLE przedmioty (
id_przedmiotu INTEGER(1) NOT NULL,
nazwa_przedmiotu TEXT(15),
nazwisko_naucz TEXT(20),
imie_naucz TEXT(15),
FOREIGN KEY (id_przedmiotu) REFERENCES przedmioty(id_przedmiotu)
);

CREATE TABLE uczniowie (
id_ucznia INTEGER ORIMARY KEY NOT NULL,
nazwisko TEXT(20),
imie TEXT(15),
ulica TEXT(15),
dom INTEGER(3),
id_klasy INTEGER NOT NULL,
FOREIGN KEY (id_ucznia) REFERENCES uczeniowie(id_ucznia)
);
