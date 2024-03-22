

CREATE TABLE publisher
(
	publisher_id integer PRIMARY KEY,
	org_name varchar(128) NOT NULL,
	address TEXT NOT NULL,
	CONSTRAINT publisher_pkey PRIMARY KEY (publisher_id)
);

CREATE TABLE book
(
	book_id integer PRIMARY KEY,
	title text NOT NULL,
	isbn varchar(32) NOT NULL,
	fk_book_publisher integer REFERENCES publisher(publisher_id) NOT NULL
);


