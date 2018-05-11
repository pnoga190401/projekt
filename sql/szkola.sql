DROP TABLE IF EXISTS tbUczniowie;
DROP TABLE IF EXISTS tbKlasa;

CREATE TABLE tbUczniowie
(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 imie TEXT,
 nazwisko TEXT,
 plec INTEGER,
 id_klasa INTEGER,
 egzHum NUMERIC NOT NULL DEFAULT 0,
 egzMat NUMERIC NOT NULL DEFAULT 0,
 egzJez NUMERIC NOT NULL DEFAULT 0,
 FOREIGN KEY (id_klasa) REFERENCES tbKlasa(id)
);

CREATE TABLE tbKlasa
(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	klasa TEXT,
	rokNaboru INTEGER,
	rokMatury INTEGER
);

INSERT INTO tbKlasa(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1A', 2017, 2020);
INSERT INTO tbKlasa VALUES (NULL, '2A', 2016, 2019);
INSERT INTO tbKlasa VALUES (NULL, '1C', 2017, 2020);
INSERT INTO tbUczniowie(id, imie, nazwisko, plec, id_klasa, egzHum, egzMat, egzJez)
VALUES(NULL, 'Adam', 'Nowak', 0, 3, 70.5, 80, 90);
INSERT INTO tbUczniowie VALUES (NULL, Paulina, Noga, 1, 1, 70, 80, 80);

UPDATE tbUczniowie SET egzJez = 100 WHERE id = 1;