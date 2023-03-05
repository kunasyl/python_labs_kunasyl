CREATE TABLE resources (
	RESOURCE_ID INTEGER PRIMARY KEY NOT NULL,
	RESOURCE_NAME TEXT DEFAULT NULL,
	RESOURCE_PAGE_URL TEXT DEFAULT NULL,
	articles_class TEXT NOT NULL,   -- tag of list of articles
	title_cut TEXT NOT NULL,   -- title
    top_tag TEXT NOT NULL,   -- article url
	bottom_tag TEXT NOT NULL   -- content
);


INSERT INTO resources
VALUES 
	(
		10,
		"https://forbes.kz",
		"https://forbes.kz/news?page={page_number}",	
		"news__list",
		"news__mini-info",
		"news__mini-info",
		"inner-news"
	),
	(
		20,
		"https://www.zakon.kz",
		"https://www.zakon.kz/news/?p={page_number}",
		"zmainCard_item", 
		"zmainCard-content",	
		"", 
		"content"
	),
	(
		30,
		"https://kapital.kz",
		"https://kapital.kz/news?page={page_number}",
		"main-news__txt",
		"main-news__name",
		"main-news__name",
		"article__body"
	)
;
