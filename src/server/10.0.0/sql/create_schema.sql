DROP TABLE ACT_Keys;
DROP TABLE CAT_Catalogues;
DROP TABLE ACT_Journals;
DROP TABLE TRX_Posting;
DROP TABLE TRX_Signatures;
DROP TABLE CAT_Items_i18n;
DROP TABLE CAT_Items;
DROP TABLE ACT_Transporter;
DROP TABLE ACT_Company;
DROP TABLE ACT_Users;



CREATE TABLE ACT_Users
(
  uuid varchar(36) NOT NULL,
  display_name varchar(128) NOT NULL,
  type char(1) NOT NULL DEFAULT 'T',
  created_at datetime NOT NULL DEFAULT NOW(),
  CONSTRAINT PK_Users PRIMARY KEY (uuid)
);


CREATE TABLE ACT_Transporter
(
  uuid varchar(36) NOT NULL,
  works_for varchar(36), 
  json json,
  CONSTRAINT PK_Users PRIMARY KEY (uuid)
);


CREATE TABLE ACT_Company
(
  uuid varchar(36) NOT NULL,
  json json,
  CONSTRAINT PK_Users PRIMARY KEY (uuid)
);


CREATE TABLE ACT_Journals
(
  posting varchar(36) NOT NULL,
  user varchar(36) NOT NULL,
  other_user varchar(36) NOT NULL,
  type char(1) NOT NULL COMMENT 'D: Delivers\nR: Receives\n',
  item varchar(36) NOT NULL,
  amount integer NOT NULL,
  datetime timestamp NOT NULL COMMENT 'Same value then theonein the posting',
  CONSTRAINT PK_Journals PRIMARY KEY (user, posting, other_user, item, type, amount, datetime)
);


CREATE TABLE ACT_Keys
(
  user varchar(36) NOT NULL,
  version tinyint NOT NULL,
  pubkey_PADES varchar(256) NOT NULL,
  pubkey_ESCD varchar(256) NOT NULL,
  created_at datetime NOT NULL DEFAULT NOW(),
  CONSTRAINT PK_Keys PRIMARY KEY (user, version)
);

CREATE TABLE CAT_Catalogues
(
  company varchar(36) NOT NULL,
  item varchar(36) NOT NULL,
  CONSTRAINT PK_Keys PRIMARY KEY (company, item)
);

CREATE TABLE CAT_Items
(
  uuid varchar(36) NOT NULL,
  type char(1),
  images_path varchar(512),
  json json COMMENT 'JSON',
  CONSTRAINT PK_Items PRIMARY KEY (uuid)
);

CREATE TABLE CAT_Items_i18n
(
  item varchar(36) NOT NULL,
  languageISO varchar(10) NOT NULL DEFAULT 'en',
  name varchar(256) NOT NULL,
  description varchar(1024),
  CONSTRAINT PK_Items_i18n PRIMARY KEY (item, languageISO)
);


CREATE TABLE TRX_Posting
(
  uuid varchar(36) NOT NULL,
  number bigint NOT NULL,
  languageISO varchar(10) DEFAULT 'en',
  creator varchar(36) NOT NULL,
  partner varchar(36) NOT NULL,
  note varchar(4096),
  document_uri varchar(512) NOT NULL COMMENT 'YYYY/MM/posting_uuid/posting_uuid.pdf (latest) YYYY/MM/posting_uuid/posting_uuid.pdf.status',
  creator_sign varchar(36) NOT NULL,
  partner_sign varchar(36),
  status char(20),
  lastupdate_at timestamp NOT NULL DEFAULT NOW(),
  created_at timestamp NOT NULL DEFAULT NOW(),
  CONSTRAINT PK_Posting PRIMARY KEY (uuid)
);

CREATE TABLE TRX_Signatures
(
  uuid varchar(36) NOT NULL,
  user varchar(36) NOT NULL,
  pubkey_PADES varchar(256),
  pubkey_ESCD varchar(256),
  biometrics varchar(2048),
  lat double DEFAULT 0,
  lng double DEFAULT 0,
  agent varchar(64) COMMENT 'mobile, browser....',
  signed_at datetime COMMENT 'to be extracted from the PDF/Document',
  CONSTRAINT PK_Signatures PRIMARY KEY (uuid)
);

ALTER TABLE ACT_Journals ADD CONSTRAINT FK_Journals_from
  FOREIGN KEY (user) REFERENCES ACT_Users (uuid);

ALTER TABLE ACT_Journals ADD CONSTRAINT FK_Journals_itam
  FOREIGN KEY (item) REFERENCES CAT_Items (uuid);

ALTER TABLE ACT_Journals ADD CONSTRAINT FK_Journals_to
  FOREIGN KEY (other_user) REFERENCES ACT_Users (uuid);

ALTER TABLE ACT_Journals ADD CONSTRAINT FK_Journals_posting
  FOREIGN KEY (posting) REFERENCES TRX_Posting (uuid);

ALTER TABLE ACT_Keys ADD CONSTRAINT FK_Keys_user
  FOREIGN KEY (user) REFERENCES ACT_Users (uuid);

ALTER TABLE ACT_Transporter ADD CONSTRAINT FK_Transporte_uuid
  FOREIGN KEY (uuid) REFERENCES ACT_Users (uuid);

ALTER TABLE ACT_Transporter ADD CONSTRAINT FK_Transporter_works_for
  FOREIGN KEY (works_for) REFERENCES ACT_Company (uuid); 
 
ALTER TABLE ACT_Company ADD CONSTRAINT FK_Company_uuid
  FOREIGN KEY (uuid) REFERENCES ACT_Users (uuid);  
 
ALTER TABLE CAT_Catalogues ADD CONSTRAINT FK_Catalogues_item
  FOREIGN KEY (item) REFERENCES CAT_Items (uuid);

ALTER TABLE CAT_Catalogues ADD CONSTRAINT FK_Catalogues_company 
  FOREIGN KEY (company) REFERENCES ACT_Company(uuid);


ALTER TABLE TRX_Posting ADD CONSTRAINT FK_Posting_creator
  FOREIGN KEY (creator) REFERENCES ACT_Users (uuid);

ALTER TABLE TRX_Posting ADD CONSTRAINT FK_Posting_creator_sign
  FOREIGN KEY (creator_sign) REFERENCES TRX_Signatures (uuid);

ALTER TABLE TRX_Posting ADD CONSTRAINT FK_Posting_partner
  FOREIGN KEY (partner) REFERENCES ACT_Users (uuid);

ALTER TABLE TRX_Posting ADD CONSTRAINT FK_Posting_partner_sign
  FOREIGN KEY (partner_sign) REFERENCES TRX_Signatures (uuid);
 
ALTER TABLE TRX_Signatures ADD CONSTRAINT FK_Signatures_user
  FOREIGN KEY (user) REFERENCES ACT_Users (uuid);
 
ALTER TABLE CAT_Items_i18n ADD CONSTRAINT FK_Items_i18n_item
  FOREIGN KEY (item) REFERENCES CAT_Items (uuid);
