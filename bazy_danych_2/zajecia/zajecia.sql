
DROP TABLE IF EXISTS osoby;
DROP TABLE IF EXISTS zajecia;
DROP TABLE IF EXISTS obiekty;
DROP TABLE IF EXISTS wejscia;
CREATE TABLE obiekty(
    id_obiektu INTEGER PRIMARY KEY,
    nazwa VARCHAR(20)
    
);

DROP TABLE IF EXISTS osoby;
CREATE TABLE osoby (
    id_osoby INTEGER PRIMARY KEY,
    nazwisko VARCHAR(30) NOT NULL,
    imie VARCHAR(30) NOT NULL,
    plec CHAR(1) DEFAULT ''
);


DROP TABLE IF EXISTS zajecia;
CREATE TABLE zajecia (
    id_zajec INTEGER PRIMARY KEY,
    id_obiektu INTEGER,
    nazwa VARCHAR(30),
    cena DECIMAL,
    FOREIGN KEY (id_obiektu) REFERENCES obiekty(id_obiektu)
);

DROP TABLE IF EXISTS wejscia;
CREATE TABLE wejscia (
    id_wejscia INTEGER PRIMARY KEY,
    id_osoby INTEGER,
    data DATE,
    id_zajec INTEGER,
    FOREIGN KEY (id_osoby) REFERENCES osoby(id_osoby),
    FOREIGN KEY (id_zajec) REFERENCES zajecia(id_zajec)
);
