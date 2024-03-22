CREATE TABLE founder(
	founder_id integer PRIMARY KEY,
	full_name TEXT NOT NULL,
	birth_place TEXT NOT NULL,
	birthday date
);

CREATE TABLE brand(
	brand_id integer PRIMARY KEY,
	name varchar(32) NOT NULL,
	fk_brand_founder integer REFERENCES founder(founder_id) NOT NULL,
	UNIQUE(fk_brand_founder)
);



CREATE TABLE car(
	car_id integer PRIMARY KEY,
	model TEXT NOT NULL,
	fk_car_brand integer REFERENCES brand(brand_id) NOT NULL
);

INSERT INTO founder
VALUES
(1, 'Ферруччо Ламборгини', 'Ченто, Феррара, Италия', '1916-04-28'),
(2, 'Альфьери Мазерати', 'Болонья, Королевство Италия', '1887-09-23'),
(3, 'Фердинанд Порше', 'Мафферсдоф, Австро-Венгрия', '1951-01-30')
;

INSERT INTO brand
VALUES
(1, 'Lamborghini', 1),
(2, 'Maserati', 2),
(3, 'Volkswagen', 3)
;

INSERT INTO car
VALUES
(1, 'Diablo', 1),
(2, 'Egoista', 1),
(3, 'MC12', 2),
(4, 'MC20', 2),
(5, 'Passat CC', 3),
(6, 'Jetta', 3)
;