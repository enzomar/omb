CREATE TABLE IF NOT EXISTS ACT_Actors
(
  uuid varchar(36) NOT NULL,
  respawn_number bigint NOT NULL DEFAULT 0,
  type varchar(64) NOT NULL,
  email varchar(128),
  json varchar(4096),
  CONSTRAINT PK_Actors PRIMARY KEY (uuid)
);

CREATE TABLE IF NOT EXISTS ACT_Balance
(
  transaction varchar(36) NOT NULL,
  actor varchar(36) NOT NULL,
  other varchar(36) NOT NULL,
  item varchar(36) NOT NULL,
  amount integer NOT NULL,
  datetime timestamp NOT NULL COMMENT 'Same value then theonein the transaction',
  CONSTRAINT PK_Balance PRIMARY KEY (transaction, actor)
);

CREATE TABLE IF NOT EXISTS ACT_Keys
(
  pubkey_PADES varchar(256) NOT NULL,
  actor varchar(36) NOT NULL,
  pubkey_ESCD varchar(256) NOT NULL,
  creted_at datetime NOT NULL DEFAULT NOW(),
  active tinyint,
  CONSTRAINT PK_Keys PRIMARY KEY (actor)
);

CREATE TABLE IF NOT EXISTS CAT_Catalogues
(
  actor varchar(36),
  item varchar(36)
);

CREATE TABLE IF NOT EXISTS CAT_Items
(
  uuid varchar(36) NOT NULL,
  name varchar(512) NOT NULL,
  type varchar(256),
  description varchar(36),
  images_path varchar(512),
  json varchar(1024),
  CONSTRAINT PK_Items PRIMARY KEY (uuid)
);

CREATE TABLE IF NOT EXISTS TRX_Posting
(
  uuid varchar(36) NOT NULL,
  number bigint NOT NULL,
  creator varchar(36) NOT NULL,
  partner varchar(36) NOT NULL,
  note varchar(4096),
  document_uri varchar(512),
  creator_sign varchar(36),
  partner_sign varchar(36),
  status char(20),
  lastupdate_at timestamp NOT NULL DEFAULT NOW(),
  CONSTRAINT PK_Transactions PRIMARY KEY (uuid)
);

CREATE TABLE IF NOT EXISTS TRX_Signatures
(
  uuid varchar(36) NOT NULL,
  pubkey_PADES varchar(256),
  pubkey_ESCD varchar(256),
  biometrics varchar(2048),
  lat double DEFAULT 0,
  lng double DEFAULT 0,
  signed_at datetime NOT NULL DEFAULT NOW(),
  CONSTRAINT PK_Signatures PRIMARY KEY (uuid)
);

CREATE TABLE IF NOT EXISTS Translations
(
  uuid varchar(36) NOT NULL,
  EN varchar(2048),
  IT varchar(2048),
  CONSTRAINT PK_Translations PRIMARY KEY (uuid)
);