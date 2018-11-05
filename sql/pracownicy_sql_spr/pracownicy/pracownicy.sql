DROP TABLE IF EXISTS pracownicy;
DROP TABLE IF EXISTS kontakty;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS stanowiska;

CREATE TABLE pracownicy(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     imie TEXT,
     nazwisko TEXT,
     kod INTEGER,
     miasto_z TEXT,
     ulica TEXT,
     data_u DATE,
     miasto_u TEXT
);

CREATE TABLE kontakty(
	id_p INTEGER PRIMARY KEY AUTOINCREMENT,
	typ_k BOOLEAN,
	kontakt INTEGER,
	uwagi TEXT,
    FOREIGN KEY (id_p) REFERENCES pracownicy(id)
);
    
CREATE TABLE place(
	id_p INTEGER PRIMARY KEY AUTOINCREMENT,
	id_s INTEGER,
	placa DECIMAL,
	data_z DATE,
    FOREIGN KEY (id_p) REFERENCES pracownicy(id),
    FOREIGN KEY (id_s) REFERENCES stanowiska(id)
);
    
CREATE TABLE stanowiska(
	id_s INTEGER PRIMARY KEY AUTOINCREMENT,
	stanowisko TEXT
);

