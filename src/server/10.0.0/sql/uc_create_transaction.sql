SET FOREIGN_KEY_CHECKS = 0; 

TRUNCATE TABLE TRX_Signatures; 
TRUNCATE TABLE TRX_Posting; 
TRUNCATE TABLE ACT_Journals; 


SET FOREIGN_KEY_CHECKS = 1;                         


/* ==============================================
 *  creator post the posting with its sign
 */

INSERT INTO TRX_Signatures (uuid    , pubkey_PADES  , pubkey_ESCD  , biometrics, user) 
                    VALUES ('sign-a', 'pubkey_PADES', 'pubkey_ESCD', 'biometrics', 'usr-uuid-a'); 

INSERT INTO TRX_Posting (uuid         , number, creator     , partner     , document_uri                   , creator_sign) 
                 VALUES ('post-uuid-a', 1     , 'usr-uuid-a', 'usr-uuid-b', '/var/post-uuid-a/document.pdf', 'sign-a'    );          
                                
INSERT INTO ACT_Journals (posting , user        , other_user  , type , item         , amount, datetime) 
                 VALUES ('post-uuid-a', 'usr-uuid-a' , 'usr-uuid-b' , 'R'  , 'item-uuid-a', 10    , NOW());
                
INSERT INTO ACT_Journals (posting , user        , other_user  , type , item         , amount, datetime) 
                 VALUES ('post-uuid-a', 'usr-uuid-b' , 'usr-uuid-a' , 'D'  , 'item-uuid-a', 10    , NOW());                
                
 /*
 *  partenrs patch the posting with its sign
 */           
           
INSERT INTO TRX_Signatures (uuid    , pubkey_PADES  , pubkey_ESCD  , biometrics, user) 
                    VALUES ('sign-b', 'pubkey_PADES', 'pubkey_ESCDx', 'biometrics', 'usr-uuid-b');  
                   
UPDATE TRX_Posting SET 
                   partner_sign = 'sign-b'
WHERE uuid='post-uuid-a';
               

/*
 *  creator manual double check the signature
 */  

UPDATE TRX_Posting SET 
                   status = 'VALIDATED'
WHERE uuid='post-uuid-a';




/* ==============================================
 *  creator post the posting with its sign
 */

INSERT INTO TRX_Signatures (uuid    , pubkey_PADES  , pubkey_ESCD  , biometrics, user) 
                    VALUES ('sign-c', 'pubkey_PADES', 'pubkey_ESCD', 'biometricsx', 'usr-uuid-b'); 

INSERT INTO TRX_Posting (uuid         , number, creator     , partner     , document_uri                   , creator_sign) 
                 VALUES ('post-uuid-b', 1     , 'usr-uuid-a', 'usr-uuid-b', '/var/post-uuid-a/document.pdf', 'sign-c'    );
                
                                          
INSERT INTO ACT_Journals (posting , user        , other_user  , type , item         , amount, datetime) 
                 VALUES ('post-uuid-b', 'usr-uuid-a' , 'usr-uuid-b' , 'D'  , 'item-uuid-a', 10    , NOW());
                
INSERT INTO ACT_Journals (posting , user        , other_user  , type , item         , amount, datetime) 
                 VALUES ('post-uuid-b', 'usr-uuid-b' , 'usr-uuid-a' , 'R'  , 'item-uuid-a', 10    , NOW()); 
                
INSERT INTO ACT_Journals (posting , user        , other_user  , type , item         , amount, datetime) 
                 VALUES ('post-uuid-b', 'usr-uuid-a' , 'usr-uuid-b' , 'D'  , 'item-uuid-b', 5    , NOW()); 
                
INSERT INTO ACT_Journals (posting , user        , other_user  , type , item         , amount, datetime) 
                 VALUES ('post-uuid-b', 'usr-uuid-b' , 'usr-uuid-a' , 'R'  , 'item-uuid-b', 5    , NOW());                 
                
 /*
 *  partenrs patch the posting with its sign
 */           
           
INSERT INTO TRX_Signatures (uuid    , pubkey_PADES  , pubkey_ESCD  , biometrics, user) 
                    VALUES ('sign-d', 'pubkey_PADESx', 'pubkey_ESCD', 'biometrics', 'usr-uuid-b');
                   
UPDATE TRX_Posting SET 
                   partner_sign = 'sign-c'
WHERE uuid='post-uuid-c';
               

/*
 *  creator manual double check the signature
 */  

UPDATE TRX_Posting SET 
                   status = 'VALIDATED'
WHERE uuid='post-uuid-c';