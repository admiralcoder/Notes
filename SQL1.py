SQL from terminal 
connect hr/hr

SELECT * FROM employees;

SELECT * FROM countries;

Interview questions As Tester we dont write tables.


====================================================================

DATA TYPES ON SQL

	Columns in SQL can accept only specific data type.
	like in JAVA.

Can Store data type

	Number -> whole numbers
	number(9) -> can accept numbers up to 9 digits
	number(5,3) ->

	char -> characters/strings
	varchar2 -> also characters used for varying length data.

		Firstname
		1) char(7) -> mark -> 4 = It will charge you for 7 spaces

		State
		char(2) -> VA,WA,FL

		City
		varchar2(20) -> Mclean -> 6 = It will charge you only for 6 spaces

		DATE -> full DATE
		Currency -> used for prices etc


====================================================================

How do I know what data types are in my table?

Commands: to uncomment type  -- (sample )

'-------------------------------------------------------------------'
	describe countries;

Name         Null?    Type         
------------ -------- ------------ 
COUNTRY_ID   NOT NULL CHAR(2)      
COUNTRY_NAME          VARCHAR2(40) 
REGION_ID             NUMBER       

'-------------------------------------------------------------------'

	describe employees;
-------------- -------- ------------ 
EMPLOYEE_ID    NOT NULL NUMBER(6)    
FIRST_NAME              VARCHAR2(20) 
LAST_NAME      NOT NULL VARCHAR2(25) 
EMAIL          NOT NULL VARCHAR2(25) 
PHONE_NUMBER            VARCHAR2(20) 
HIRE_DATE      NOT NULL DATE         
JOB_ID         NOT NULL VARCHAR2(10) 
SALARY                  NUMBER(8,2)  
COMMISSION_PCT          NUMBER(2,2)  
MANAGER_ID              NUMBER(6)    
DEPARTMENT_ID           NUMBER(4)  

'-------------------------------------------------------------------'

	Describe departments;
-------------- -------- ------------ 
COUNTRY_ID   NOT NULL CHAR(2)      
COUNTRY_NAME          VARCHAR2(40) 
REGION_ID             NUMBER       
Name           Null?    Type    

'-------------------------------------------------------------------'


	Describe locations;
-------------- -------- ------------ 
LOCATION_ID    NOT NULL NUMBER(4)    
STREET_ADDRESS          VARCHAR2(40) 
POSTAL_CODE             VARCHAR2(12) 
CITY           NOT NULL VARCHAR2(30) 
STATE_PROVINCE          VARCHAR2(25) 
COUNTRY_ID              CHAR(2)      
Name           Null?    Type  

"____________________________________________________________________"

* PRIMARY KEY

	-> EVERY TABLE HAS A PRIMARY KEY, UNIQUE

* FOREIGH KEY

	-> WHEN A COLUMN  IS USED THAT IS PRIMARY KEY IN ANOTHER TABLE 

	STUDENTS	  ->FOREIGH KEY			STUDENTS	
STUDENTID	NAME	CLASSID			CLASSID	CLASS NAME
100			SARA	122				122				SQL
101			ALEX	123				123				JAVA
102			MICK	125				124				SELENIUM


CLASS ID FOR MICK IS 125 WHICH IS NOT ON THE LIST THAT LINE OF ID IS
CALLED FOREIGH KEY

- When a Column is a FOREIGH key only data from primary key table
can be used.

"____________________________________________________________________"


*******************
Char vs varchar2

char is used for fixed length characters
gender, M,F

email -> char (50)
	even if you do not insert 50 characters, databae will still take space 
	for 50 character from memory

email -> varchar2(50)
	if you put less than 50 characters database will only take that 
	length of memory

******************


====================================================================
 if there is an empty space  on the document 

NULL,
NULL -> MANDATORY TO ENTER DATA TO THIS Columns
NOT NULL -> MANDATORY TO ENTER DATA TO THIS Columns

====================================================================

RDBMS:	'RELATIONAL DATABASE MANAGEMENT SYSTEM'

we call them relational because tables in that database are
related using primary and foreigh key relationship.

ORACLE, MYSQL

Oracle is a database system and is used by big companies because 
its very expensive


====================================================================

AMAZON EC2 SERVER AND INSTALLED ORACLE RDBMS

	- We are connecting to that database using. SQL developer
	SQL DEVELOPER IS A TOOL 

	DATABASE SYSTEMS 
	MY SQL ORACLE 

======================= DATABASE SCHEMA ===========================

	DATABASE SCHEMA -> is a chart that shows all tables and how they are related 
	to one another.


ONE TO MANY relation -> One Department  can have many employees

many to many relation -> One empleyee can have only one department


====================================================================
if you dont have database schema you can do the following
someone gave you access to database and there is no database SCHEME

STEP 1: display all tables

MySQL: has a command 

	show tables;

ORACLE: Select table_name from user_tables;
		EXAMPLE:

Sybase
IBM
DB2
MS SQL SERVER

			REGIONS
1 LOCATIONS
2 DEPARTMENTS
3 JOBS
4 EMPLOYEES
5 JOB_HISTORY
6 COUNTRIES


STEP 2: DESCRIBE command to see Columns and relations.

=========================================================

DISPLAY DATA FROM SEPCIFIC COLUMN

SELECT col1, col2, col3
FROM table;

Query to see emp first name, lastname 

SELECT first_name, last_name
FROM employees;

Ellen	Abel
Sundar	Ande
Mozhe	Atkinson
David	Austin
Hermann	Baer
Shelli	Baida
Amit	Banda
Elizabeth	Bates


Task: write a query last name first name salary job id

Select first_name, salary, job_id
from employees;

Steven	King			24000	AD_PRES
Neena	Kochhar			17000	AD_VP
Lex	De Haan				17000	AD_VP
Alexander	Hunold		9000	IT_PROG
Bruce	Ernst			6000	IT_PROG
David	Austin			4800	IT_PROG
Valli	Pataballa		4800	IT_PROG
Diana	Lorentz			4200	IT_PROG
Nancy	Greenberg		12008	FI_MGR
Daniel	Faviet			9000	FI_ACCOUNT

====================== SortQuery ascending ========================

SORTING QUERY RESULTS:
	ORDER BY is used to sort results. by default is ascending

		Display all last names, emp id, emails. sort by lastname

SELECT last_name, employee_id, email
FROM employees
ORDER BY employee_id;

Abel			174	EABEL
Ande			166	SANDE
Atkinson		130	MATKINSO
Austin			105	DAUSTIN
Baer			204	HBAER
Baida			116	SBAIDA
Banda			167	ABANDA

====================== SortQuery Descending ========================

SELECT last_name, employee_id, email
FROM employees
ORDER BY employee_id desc;

Gietz			206	WGIETZ
Higgins			205	SHIGGINS
Baer			204	HBAER
Mavris			203	SMAVRIS
Fay				202	PFAY
Hartstein		201	MHARTSTE
Whalen			200	JWHALEN


Task: Display employee id, last name, job id, salaries
with descending order of salary

'sample 1'
SELECT employee_id,last_name, JOB_ID, SALARY
FROM employees
ORDER BY SALARY desc;

-- order by position 4 is SALARY --
'sample 2'
SELECT employee_id,last_name, JOB_ID, SALARY
FROM employees
ORDER BY 4 desc;

100	King	AD_PRES			24000
101	Kochhar	AD_VP			17000
102	De Haan	AD_VP			17000
145	Russell	SA_MAN			14000
146	Partners	SA_MAN		13500
201	Hartstein	MK_MAN		13000
108	Greenberg	FI_MGR		12008
205	Higgins	AC_MGR			12008

=============== ARITHMETIC EXPRESSIONS  ==============

SELECT 10 * 10 + 2000
FROM employees;

Query: DIsplay emp last name and anual salary 

SELECT last_name, SALARY*12
FROM employees
ORDER BY 2;

Olson		25200
Markle		26400
Philtanker	26400
Gee			28800
Landry		28800

=============== RENAME COLUM IN RESULT ==============

REname colums in resul by :

AS keyboard or just space

SELECT last_name, SALARY*12 AS Annual
FROM employees
ORDER BY 2;

Task: DIsplay empl last name, salary daily hourly weekly montly anually 
sort by lastname

SELECT Last_name, job_id, salary/160 AS hourly, 
salary/20 AS daily,salary/4 AS weekly,
salary AS montly,salary*12 AS hourly
FROM employees
ORDER BY 1;

=============== DISTINCT keyword ==============
IT WILL SELECT AND PRINT THE ONES THAT ARE NOT DUPLICATE

SELECT DISTINCT job_id
FROM employees;


=============== CONCATENANTION keyword ==============

CONCATENATION OPERATOR IN SQL:
JAVA : +
SQL:   ||

		SELECT first_name || last_name || '@gmail.com' AS emails
		FROM employees;
'resul'		
EllenAbel@gmail.com
SundarAnde@gmail.com
MozheAtkinson@gmail.com
DavidAustin@gmail.com

		SELECT first_name ||'_'|| last_name || '@gmail.com' AS emails
		FROM employees;

'sample'
Ellen_Abel@gmail.com

||'_'||

====================== FILTERING RESULTS =======================

Filtering Results in SQL
Where keyboard 

QUery: display lastname salary only for people who earn less than 5000
montly

SELECT last_name, salary
FROM employees
WHERE salary < 5000;

Austin		4800
Pataballa	4800
Lorentz		4200
Khoo		3100
Baida		2900
Tobias		2800
Himuro		2600

====================== SHOW ALL IT PROGRAMERS =======================

show all IT programer
task:
	SELECT * 				-> SELECTS * MEANS ALL
	FROM employees. 		-> FROM THE LIST OF EMPLOYEES
	WHERE JOB_ID = 'IT_PROG'; -> BY JOB TITLE IT PROGRAMERS

103	Alexander	Hunold	AHUNOLD	590.423.4567	03-JAN-06	IT_PROG	9000		102	60
104	Bruce		Ernst	BERNST	590.423.4568	21-MAY-07	IT_PROG	6000		103	60
105	David		Austin	DAUSTIN	590.423.4569	25-JUN-05	IT_PROG	4800		103	60
106	Valli		Pataballa	VPATABAL	590.423.4560	05-FEB-06	IT_PROG	4800		103	60
107	Diana		Lorentz	DLORENTZ	590.423.5567	07-FEB-07	IT_PROG	4200		103	60



====================== JOB ID AND DEPARTMENT ID OF DAVIG ==============

TASK: TELL ME JOB ID AND DEPARTMENT ID OF David Austin

	SELECT job_id, department_id
	FROM employees
	WHERE first_name || last_name = 'DavidAustin';
	
'Result'

	IT_PROG	60


====================== SUMMARY =======================

Database is a store for data in database we have tables, tables have
cllums and rows, tables are related to one another using primary
and foreigh keys

each table columm can accept only pre-defined data types


AWS

AWS: EC2-> cloud machine

service called Amazon RDS -> for databases 

SELECT, FROM , ORDER BY, AS, DISTINCT || DESCRIBE 
















