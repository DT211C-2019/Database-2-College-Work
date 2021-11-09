--Minus demo
SELECT * FROM CLAIM
MINUS
SELECT * FROM CLAIM WHERE CLAIM_NATURE = 'Medical';

--Intersection demo
SELECT * FROM CLAIM WHERE CLAIM_STATE = 'S'
INTERSECT 
SELECT * FROM CLAIM WHERE CLAIM_NATURE = 'Medical';

--Union demo
SELECT * FROM CLAIM WHERE CLAIM_NATURE = 'Civil'
UNION
SELECT * FROM CLAIM WHERE CLAIM_NATURE = 'Medical';

--XOR demo
SELECT * FROM CLAIM TA
LEFT JOIN (SELECT * FROM CLAIM) TB ON TA.CLAIM_ID = TB.CLAIM_ID 
UNION 
SELECT * FROM CLAIM TA
RIGHT JOIN (SELECT * FROM CLAIM) TB ON TA.CLAIM_ID = TB.CLAIM_ID
WHERE (TA.CLAIM_ID IS NULL) OR (TB.CLAIM_ID IS NULL);

--Relational division demo
SELECT * FROM CLAIM
WHERE CLAIM_NATURE = 'Medical' AND CLAIM_STATE = 'S';

--Inner join demo
SELECT * FROM CLAIM
INNER JOIN (SELECT * FROM CLAIM) USING (CLAIM_ID);

--Left Join demo
SELECT CLAIM.CLAIM_STATE, PAYMENT.PAYMENT_AMOUNT FROM CLAIM
LEFT JOIN PAYMENT USING (PAYMENT_ID);

--Full join demo
SELECT CLAIM.CLAIM_NATURE, REPORT.REPORT_CONTENT FROM CLAIM
FULL OUTER JOIN REPORT USING (REPORT_ID);

--Aggregate Functions demo
SELECT PAYMENT_ID, MIN(PAYMENT_AMOUNT), MAX(PAYMENT_AMOUNT) FROM PAYMENT
GROUP BY PAYMENT_ID
HAVING MIN(PAYMENT_AMOUNT) > 300
ORDER BY PAYMENT_ID;

--Correlated Sub-Query demo
SELECT ACCIDENT.ACCIDENT_DESCRIPTION, PAYMENT.PAYMENT_AMOUNT FROM ACCIDENT
INNER JOIN CLAIM USING (ACCIDENT_ID)
INNER JOIN PAYMENT USING (PAYMENT_ID)
WHERE PAYMENT.PAYMENT_AMOUNT = (SELECT MIN (PAYMENT_AMOUNT) FROM PAYMENT);