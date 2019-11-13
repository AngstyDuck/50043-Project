CREATE DATABASE amazon;

use amazon;

CREATE TABLE amazonreviews(
	id BIGINT(20) NOT NULL AUTO_INCREMENT,
	asin VARCHAR(255) NULL,
	helpful VARCHAR(255) NULL,
	overall BIGINT(20) NULL,
	reviewText VARCHAR(255) NULL,
	reviewTime DATE NULL,
	reviewerID VARCHAR(255) NULL,
	reviewerName VARCHAR(255) NULL,
	summary VARCHAR(255) NULL,
	unixReviewTime BIGINT(20) NULL,
	primary key (id)
	);

LOAD DATA LOCAL INFILE '~/50043-Project/backend/setup/kindle_reviews.csv' 
INTO TABLE amazonreviews FIELDS TERMINATED BY '~'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
;
