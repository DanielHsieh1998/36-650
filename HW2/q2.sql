DROP TABLE rdata;

CREATE TABLE rdata(
	id serial,
	a varchar(5) UNIQUE NOT NULL,
	b varchar(5) UNIQUE NOT NULL,
	moment date DEFAULT '2020-01-01',
	x numeric(5,2) CHECK(x>0)
);


