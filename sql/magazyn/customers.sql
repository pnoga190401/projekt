DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS subscrtiptions;

CREATE TABLE customers(
 customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
 customer_name TEXT,
 address TEXT
);

CREATE TABLE orders(
	order_id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER,
	subscrtiption_id INTEGER,
	purchase_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (subscrtiption_id) REFERENCES subscription(id)
);
    
CREATE TABLE subscrtiptions(
	subscrtiption_id INTEGER PRIMARY KEY AUTOINCREMENT,
	desctiption TEXT,
	price_per_month DECIMAL,
	subscrtiption_length TEXT
);

