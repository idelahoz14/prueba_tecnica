-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXIST users;

CREATE TABLE users (
	"id"	INTEGER NOT NULL,
	"firstName"	TEXT NOT NULL,
	"middleName"	TEXT,
	"lastName"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"zipCode"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
