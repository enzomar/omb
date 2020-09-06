CREATE USER 'webserver'@'%';
ALTER USER 'webserver'@'%'
IDENTIFIED BY 'webserver' ;

GRANT Update ON easycontainer.* TO 'webserver'@'%';
GRANT Select ON easycontainer.* TO 'webserver'@'%';
GRANT Insert ON easycontainer.* TO 'webserver'@'%';
GRANT Delete ON easycontainer.* TO 'webserver'@'%';
