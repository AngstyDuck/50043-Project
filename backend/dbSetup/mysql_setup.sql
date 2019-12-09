CREATE DATABASE amazon;

USE amazon;

-- Create and fill up amazonreviews table; create trigger
CREATE TABLE amazonreviews(
	id BIGINT(20)  NOT NULL AUTO_INCREMENT,
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

LOAD DATA LOCAL INFILE '~/Desktop/50043-Project-lfs/kindle_reviews.csv' 
INTO TABLE amazonreviews 
	FIELDS TERMINATED BY ',' ENCLOSED BY '"'
	LINES TERMINATED BY '\n'
IGNORE 1 ROWS 
;

create trigger review_trigger before insert on `amazonreviews` for each row set NEW.reviewerID=uuid();


-- Create table for logs
CREATE TABLE logs(
	id BIGINT(20) NOT NULL AUTO_INCREMENT,
	datetime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- on update, current datetime will be updated as well
	log_msg VARCHAR(510) NULL,
	PRIMARY KEY (id)
	);

CREATE USER 'ubuntu'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'ubuntu'@'localhost';
FLUSH PRIVILEGES;

