/*
 *  get user balance
 */

SELECT * FROM ACT_Journals
WHERE user = 'usr-uuid-a'; 


SELECT * FROM ACT_Journals
WHERE user = 'usr-uuid-b'; 


SELECT * FROM ACT_Journals
WHERE user = 'usr-uuid-c'; 

/*
 *  get all incomplete transaction 
 */

SELECT * FROM TRX_Posting
WHERE creator_sign IS NULL or partner_sign IS NULL;

/*
 *  get incomplete transation i am involved
 */

SELECT * FROM TRX_Posting
WHERE creator_sign IS NULL or partner_sign IS NULL
AND (creator = 'usr-uuid-a' OR partner =  'usr-uuid-a');


/*
 *  get company's catalogue
 */

SELECT * FROM CAT_Items 
WHERE uuid in (
	SELECT item FROM CAT_Catalogues
	WHERE company = 'usr-uuid-a'
);


/*
 *  get item details
 */

SELECT * FROM CAT_Items 
WHERE uuid = 'item-uuid-a';


/*
 *  get Keys for a user
 */

SELECT pubkey_PADES, pubkey_ESCD FROM ACT_Keys
WHERE user = 'usr-uuid-b';

/*
 *  get user with anomalous biometrics
 */

SELECT user, COUNT(user)
FROM (
	SELECT user, COUNT(user) as occ, biometrics
	FROM TRX_Signatures
	GROUP BY user, biometrics ORDER BY COUNT(*)) 
	as t
GROUP BY t.user
HAVING COUNT(t.user) > 1;

