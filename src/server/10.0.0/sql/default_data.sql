SET FOREIGN_KEY_CHECKS = 0; 

TRUNCATE TABLE ACT_Keys;
TRUNCATE TABLE ACT_Users;
TRUNCATE TABLE ACT_Company;
TRUNCATE TABLE ACT_Transporter;
TRUNCATE TABLE TRX_Signatures; 
TRUNCATE TABLE TRX_Posting; 
TRUNCATE TABLE ACT_Journals; 
TRUNCATE TABLE CAT_Items; 
TRUNCATE TABLE CAT_Catalogues;

SET FOREIGN_KEY_CHECKS = 1; 

/*
 *  SETUP: admin create default items
 */               
               
INSERT INTO CAT_Items (uuid         ,  name           , type) 
               VALUES ('item-uuid-a', 'CCONTAINER'    , 'C');                 
INSERT INTO CAT_Items (uuid         ,  name           , type) 
               VALUES ('item-uuid-b', 'SHELVES'       , 'S');           
INSERT INTO CAT_Items (uuid         ,  name           , type) 
               VALUES ('item-uuid-c', 'EXTENTIONS'    , 'E');  
              
              
/*
 *  SETUP: 
 *       company signup
 *       - informations
 *       - pubkes
 *       - catalogue
 */              
INSERT INTO ACT_Users (uuid        , display_name, type) 
                VALUES ('usr-uuid-a', 'MrGrower'  , 'C' );
INSERT INTO ACT_Keys (user         , version, pubkey_PADES   , pubkey_ESCD) 
                VALUES ('usr-uuid-a', 0  ,     'pubkey_PADES' , 'pubkey_ESCD');  
INSERT INTO ACT_Company (uuid) 
                VALUES ('usr-uuid-a');
INSERT INTO CAT_Catalogues (company       , item) 
                    VALUES ('usr-uuid-a', 'item-uuid-a');               
INSERT INTO CAT_Catalogues (company       , item) 
                    VALUES ('usr-uuid-a', 'item-uuid-b');
                                             
               
INSERT INTO ACT_Users (uuid        , display_name, type) 
                VALUES ('usr-uuid-c', 'WeSell'  , 'C' );
INSERT INTO ACT_Keys (user         , version, pubkey_PADES   , pubkey_ESCD) 
                VALUES ('usr-uuid-c', 0     , 'pubkey_PADES' , 'pubkey_ESCD');                          
INSERT INTO ACT_Company (uuid) 
                VALUES ('usr-uuid-c');
INSERT INTO CAT_Catalogues (company       , item) 
                    VALUES ('usr-uuid-c', 'item-uuid-a');               
INSERT INTO CAT_Catalogues (company       , item) 
                    VALUES ('usr-uuid-c', 'item-uuid-b');                
                  
                    
INSERT INTO ACT_Users (uuid        , display_name, type) 
                VALUES ('usr-uuid-b', 'Ciccio'  , 'T');               
               
INSERT INTO ACT_Transporter (uuid        , works_for) 
                VALUES ('usr-uuid-b','usr-uuid-a');
INSERT INTO ACT_Keys (user         , version, pubkey_PADES   , pubkey_ESCD) 
                VALUES ('usr-uuid-b', 0  ,     'pubkey_PADES' , 'pubkey_ESCD');
               
               
          
                    
                   