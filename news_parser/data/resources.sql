CREATE TABLE resources (
	RESOURCE_ID INTEGER PRIMARY KEY NOT NULL,
	RESOURCE_NAME TEXT DEFAULT NULL,
	RESOURCE_URL TEXT DEFAULT NULL,
	RESOURCE_PAGE_URL TEXT DEFAULT NULL,
	article_div_class TEXT NOT NULL,
	article_title TEXT NOT NULL,
    article_url TEXT NOT NULL,
    time TEXT NOT NULL,
	article_date TEXT NOT NULL,
	article_content TEXT NOT NULL
);

-- DELETE FROM resources;

INSERT INTO resources
VALUES 
	(
		10,
		"https://forbes.kz",
		"https://forbes.kz/news",
		"https://forbes.kz/news?page={page_number}",	
		"news__list",
		"news__mini-info",
		"news__mini-info",
		"news__mini-date",
		"article__date",
		"inner-news"
	)	
;


(
	20,
	"https://www.zakon.kz"
	"https://www.zakon.kz/news",
	"https://www.zakon.kz/news/?p={page_number}",
	"zmainCard_item",   -- card_md z-col-lg-3 z-col-md-3
	"title",
		
),
(
	30,
	"https://www.inform.kz/ru/lenta",
	"https://www.inform.kz/ru/lenta/{page_number}",
	"",
	"",
	"",
	"time_article_bl_mob",
),