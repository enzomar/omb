CREATE TABLE IF NOT EXISTS easycontainer.transaction (
    number INT NOT NULL AUTO_INCREMENT,
	uuid VARCHAR(36) NOT NULL,
	creator_uuid VARCHAR(36)  NOT NULL,
	partner_uuid VARCHAR(36)  NOT NULL,
	creation_timestamp_gmt TIMESTAMP NOT NULL,
	document BLOB,
	creator_keys VARCHAR(3072),
	partner_keys VARCHAR(3072),
	items TEXT NOT NULL,	
	note TEXT,
	status VARCHAR(100),
	INDEX (creator_uuid, partner_uuid),
	KEY (number),
	PRIMARY KEY (uuid)
);