CREATE DATABASE amazon;

use amazon;

CREATE TABLE amazonreviews(
	id INT NOT NULL AUTO_INCREMENT,
	asin VARCHAR(255) NULL,
	helpful VARCHAR(255) NULL,
	overall INT NULL,
	reviewText VARCHAR(255) NULL,
	reviewTime DATE NULL,
	reviewerID VARCHAR(255) NULL,
	reviewerName VARCHAR(255) NULL,
	summary VARCHAR(255) NULL,
	unixReviewTime INT NULL,
	PRIMARY KEY (id)
	);

LOAD DATA LOCAL INFILE 'C:/Users/user/Documents/Big Database and Data system/Lab1/50043-Project/backend/setup/kindle_reviews.csv' 
INTO TABLE amazonreviews FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' 
;