CREATE OR REPLACE PROCEDURE generate_report (
	claim_idL IN NUMBER(1),
	report_request_dateL IN DATE,
	report_submit_dateL IN DATE,
	report_contentL IN VARCHAR2(255),
	expert_idL IN NUMBER(1),
	reportID OUT NUMBER(1)
)
IS
	report_idL NUMBER(1) 
BEGIN
	
	IF expert_idL <= 0 THEN
		RAISE expert_invalid_low;
	ELSE 
		--Starts our transaction
		SET TRANSACTION READ WRITE;
	
		--Gets a new ID
		SELECT MAX(REPORT_ID) INTO report_idL FROM REPORT;
		report_idL := report_idL+1;

		--Creates a new table based on inputs
		INSERT INTO REPORT VALUES (report_idL, report_request_dateL, report_submit_dateL, report_contentL, expert_idL);

		--Passes ID to our output register
		reportID := reportIDL;

		--Commits our changes
		COMMIT;
	END IF;

EXCEPTION
	WHEN expert_invalid_low;
	dbms_output.put_line('Error! Expert ID must be greater then zero');
	ROLLBACK;

	WHEN OTHERS THEN
	dbms_output.put_line('Error! Generic'); 
	ROLLBACK;
	
END;

--Updates our table with above procedure
UPDATE CLAIM
SET REPORT_ID = EXEC generate_report(3, DATE '2020-11-01', DATE '2020-11-07', 'Driver did not assault patron', 1)
WHERE REPORT_ID = 5;