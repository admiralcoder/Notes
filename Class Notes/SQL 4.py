SQL 4

SUBQUERIES
SET OPERATORS

==================== SUBQUERIES ( query inside query) ==========================

SUBQUERIES

what is a subquery: 
					subquery is a nested query. QUery within another query
					like nested method calls

"SCENARIO 1 - Minimum Salary"
		 : first name, last name, salary, job id of the lowest salaried employees

'example 1'
SELECT first_name, last_name, salary, job_id
FROM employees
WHERE salary = (SELECT MIN (salary) FROM employees);

'result 1'
TJ	Olson	2100	ST_CLERK



"SCENARIO 2 MAXIMUM Salary"
		:: first name, last name, salary, job id of the highest salaried employees

'example 2'
SELECT first_name, last_name, salary, job_id
FROM employees
WHERE salary = (SELECT MAX (salary) FROM employees);

'result 2'
Steven	King	24000	AD_PRES



""QUERY""
		: list emp ids, job id, dep id for employee who are not managers.

1) Find unique manager Ids 
2) Find employees who do not have those Ids as employee Ids

'example'
SELECT employee_id,last_name, job_id,department_id
FROM employees
WHERE NOT employee_id IN (SELECT DISTINCT manager_id FROM employees WHERE manager_id is not null);

'result'
106	Pataballa	IT_PROG	60
107	Lorentz	IT_PROG	60
109	Faviet	FI_ACCOUNT	100


================== SET OPERATORS =====================

UNION , UNION ALL, MINUS, INTERSECT

SET OPERATORS work with INDEPENDENT queries. 

UNION -> returns combined rows from 2 independent queries and removes
		duplicates and sorts them

'EXAMPLE'

	(query 1)
	UNION
	(query 2)

=================== UNION SAMPLE ===========================
UNION -> returns combined rows from 2 independent queries and removes
		duplicates and sorts them


'sample '
(SELECT employee_id, last_name, salary,department_id
FROM employees
WHERE department_id = 100)
UNION
(SELECT employee_id, last_name, salary,department_id
FROM employees
WHERE department_id = 10);

'result'

108	Greenberg	12008	100
109	Faviet	9000	100
110	Chen	8200	100
111	Sciarra	7700	100
112	Urman	7800	100
113	Popp	6900	100
200	Whalen	4400	10


------ FOR SET operators to work:

	-> Same number of columns in select statement
		-> same numbers of column in select statement

'example'
	(SELECT employee_id, last_name, salary
	FROM employees
	WHERE department_id = 100)
	UNION
	(SELECT employee_id, last_name, salary,department_id
	FROM employees
	WHERE department_id = 10);
'result'
	ORA-00936: missing expression
	00936. 00000 -  "missing expression"
	*Cause:    
	*Action:
	Error at Line: 356 Column: 1


	-> Same Data type in same order
'example'
	(SELECT employee_id, last_name, salary,department_id
	FROM employees
	WHERE department_id = 100)
	UNION
	(SELECT employee_id, last_name,department_id,salary
	FROM employees
	WHERE department_id = 10);

'resul'
	ORA-01790: expression must have same datatype as corresponding expression
	01790. 00000 -  "expression must have same datatype as corresponding expression"
	*Cause:    
	*Action:
	Error at Line: 355 Column: 22

============================ UNION ALL ==========================

UNION ALL -> returns combined rows from 2 independent queries and does not
	remove duplicated and does not sort them

"query using UNION"
		(select employee_id, last_name,job_id
			from employees)
		UNION
		(select employee_id, last_name,job_id
			from employees)

"query using UNION ALL"
		(select employee_id, last_name,job_id
			from employees)
		UNION ALL
		(select employee_id, last_name,job_id
			from employees)


============================ MINUS ==========================

MINUS: returns records from first query that is not present in
		Second query.

-> it will only return values (from 1st query) that are not common 
	in 2 queries.

-> it will take results of 1st query and compare with 2nd query
	and show only records that do not apprear in 2nd query. 
	it will help you find difference between queries

sample:
1) woodenspoon, apples, banana, cucumber, charger
2) plastic spoon, apple, bananas,charger

result:
woodensppon, cucumber

--- printing 105 and 106 using MINUS first query decides what will print

'example'
(SELECT employee_id, last_name
FROM employees
WHERE employee_id IN (100,104,105,106)) <- first query will decide what to print
MINUS
(SELECT employee_id, last_name
FROM employees
WHERE employee_id IN (100,104,110,120));

'resul'

105	Austin
106	Pataballa

"QUERY"
		1- display emp ids, dept ids, dep names
		for all employees and departments

		2- display emp ids, dept ids, dep names
		for all employees and departments
		only for departments that have employees

'sample'
(SELECT employee_id,e.department_id,department_name
FROM employees e FULL OUTER JOIN departments d
ON e.department_id = d.department_id)
MINUS
(SELECT employee_id,e.department_id,department_name
FROM employees e INNER JOIN departments d
ON e.department_id = d.department_id);

'result'
178		null	null
null	null	Benefits
null	null	Construction
null	null 	Contracting



INTERSECT ->  DATA migration from database (MYSQL)
to DATABSE2(ORACLE)

same database schema in both.


	how to collect data from 2 tables from different companies:
	'example'
			tableA in MYSQL
			tableA in ORACLE

	SELECT * from tableA
	MINUS
	SELECT * from tableA

if its same data nothing should show up 
if there is difference those records will show


	'example'
			tableA in MYSQL
			tableA in ORACLE

	SELECT * from tableA
	MINUS
	SELECT * from tableB



	'example'
			tableA in MYSQL
			tableA in ORACLE

	SELECT * from tableB
	MINUS
	SELECT * from tableA



=========================== INTERSECT =======================

INTERSECT -> returns  records that are present /common/appear in both


'example'
(SELECT employee_id, last_name
FROM employees
WHERE employee_id IN (100,104,105,106)) <- first query will decide what to print

INTERSECT

(SELECT employee_id, last_name
FROM employees
WHERE employee_id IN (100,104,110,120));

'resul'
100
104

======================= SUMMARY ====================

SUBQUERY: nested query summary of set operators

UNION - combines, removes duplicates sorts
UNION ALL - combines, doesnt remove duplicates, does not sorts
MINUS - show records from query1 that are not present in query2
INTERSECT- show common records from 2 queries


DDL: 
	create
	drop
	truncate
	alter

DML:
	select
	insert
	update
	delete

DROP vs truncate

both are data definition language commands
drop removes data and table as well 
truncate will remove all data but keeps the empty table

neither of them can be rolled back







============ EXTRA =================


--create table
create table Students 
(
Student_id number(4) primary key,
last_name varchar2(30) not null,
couse_id number(4) null

);

describe Students;


































