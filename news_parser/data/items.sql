CREATE TABLE items (
	id INTEGER PRIMARY KEY NOT NULL,
	res_id INTEGER DEFAULT NULL,
	link TEXT DEFAULT NULL,
	title TEXT NOT NULL,
	content TEXT NOT NULL,
    nd_date INTEGER NOT NULL,
    s_date INTEGER NOT NULL,
    not_date TEXT NOT NULL
);

-- delete from items;