SQL2
Day2


127.0.0.1 ->  localhost

127.0.0.1:8899 -> Jenkins 


================= COMPARISON OPERATORS IN SQL =====================

= < > <= >= <> 

<> = is not equal in SQL operator

For -- ranges: BETWEEN ... AND ... 

IN -- operator: for sets with OR condition

LIKE -- operator: for partial searches

IS NULL 


================= LOGICAL OPERATORS IN SQL =====================

AND, OR, NOT 


====================================================================

QUERY: show all employees whose salary is more than 4000 and less than
		6000.

......."OPTION 1"

SELECT *
FROM employees
WHERE SALARY > 4000 
AND SALARY < 6000;

- result:

105	David	Austin	DAUSTIN	590.423.4569	25-JUN-05	IT_PROG	4800		103	60
106	Valli	Pataballa	VPATABAL	590.423.4560	05-FEB-06	IT_PROG	4800		103	60
107	Diana	Lorentz	DLORENTZ	590.423.5567	07-FEB-07	IT_PROG	4200		103	60
124	Kevin	Mourgos	KMOURGOS	650.123.5234	16-NOV-07	ST_MAN	5800		100	50
184	Nandita	Sarchand	NSARCHAN	650.509.1876	27-JAN-04	SH_CLERK	4200		121	50
185	Alexis	Bull	ABULL	650.509.2876	20-FEB-05	SH_CLERK	4100		121	50
200	Jennifer	Whalen	JWHALEN	515.123.4444	17-SEP-03	AD_ASST	4400		101	10



QUERY: show all employees whose salary is equal more than 4000 and less than or equal than
		6000.


......"OPTION 2"

SELECT *
FROM employees
WHERE SALARY BETWEEN 4000 AND 6000;

104	Bruce	Ernst	BERNST	590.423.4568	21-MAY-07	IT_PROG	6000		103	60
105	David	Austin	DAUSTIN	590.423.4569	25-JUN-05	IT_PROG	4800		103	60
106	Valli	Pataballa	VPATABAL	590.423.4560	05-FEB-06	IT_PROG	4800		103	60
107	Diana	Lorentz	DLORENTZ	590.423.5567	07-FEB-07	IT_PROG	4200		103	60
124	Kevin	Mourgos	KMOURGOS	650.123.5234	16-NOV-07	ST_MAN	5800		100	50
184	Nandita	Sarchand	NSARCHAN	650.509.1876	27-JAN-04	SH_CLERK	4200		121	50
185	Alexis	Bull	ABULL	650.509.2876	20-FEB-05	SH_CLERK	4100		121	50
192	Sarah	Bell	SBELL	650.501.1876	04-FEB-04	SH_CLERK	4000		123	50
200	Jennifer	Whalen	JWHALEN	515.123.4444	17-SEP-03	AD_ASST	4400		101	10
202	Pat	Fay	PFAY	603.123.6666	17-AUG-05	MK_REP	6000		201	20


-------------- :IS NOT: <> ---------------

QUERY: display all employee last name and job id who are not sales representatives


"OPTION 1"

SELECT last_name , job_id
FROM employees
WHERE job_id <> 'SA_REP';

result: 77 in total

Atkinson	ST_CLERK
Austin		IT_PROG
Baer		PR_REP
Baida		PU_CLERK
Bell		SH_CLERK
Bissot		ST_CLERK
Bull		SH_CLERK
Cabrio		SH_CLERK
Cambrault	SA_MAN


"OPTION 2" - same result different way

SELECT last_name , job_id
FROM employees
WHERE NOT job_id = 'SA_REP';


result: 77 in total

Atkinson	ST_CLERK
Austin		IT_PROG
Baer		PR_REP
Baida		PU_CLERK
Bell		SH_CLERK
Bissot		ST_CLERK
Bull		SH_CLERK
Cabrio		SH_CLERK
Cambrault	SA_MAN



====================== BETWEEN AND ===============================

BETWEEN AND -> Between 2 Values (inclusive)

QUERY: List all employees who joined the company after jan 1, 2001 and before
		jan 1, 2004


"OPTION 1"

SELECT *
FROM employees
WHERE hire_date BETWEEN '01-JAN-01'
AND '01-JAN-04';

-- result:

100	Steven	King	SKING	515.123.4567	17-JUN-03	AD_PRES	24000		
102	Lex	De Haan	LDEHAAN	515.123.4569	13-JAN-01	AD_VP	17000		100
108	Nancy	Greenberg	NGREENBE	515.124.4569	17-AUG-02	FI_MGR	12008		101
109	Daniel	Faviet	DFAVIET	515.124.4169	16-AUG-02	FI_ACCOUNT	9000		108
114	Den	Raphaely	DRAPHEAL	515.127.4561	07-DEC-02	PU_MAN	11000		100
115	Alexander	Khoo	AKHOO	515.127.4562	18-MAY-03	PU_CLERK	3100		114
122	Payam	Kaufling	PKAUFLIN	650.123.3234	01-MAY-03	ST_MAN	7900		100
137	Renske	Ladwig	RLADWIG	650.121.1234	14-JUL-03	ST_CLERK	3600		123
141	Trenna	Rajs	TRAJS	650.121.8009	17-OCT-03	ST_CLERK	3500		124
200	Jennifer	Whalen	JWHALEN	515.123.4444	17-SEP-03	AD_ASST	4400		101
203	Susan	Mavris	SMAVRIS	515.123.7777	07-JUN-02	HR_REP	6500		101
204	Hermann	Baer	HBAER	515.123.8888	07-JUN-02	PR_REP	10000		101
205	Shelley	Higgins	SHIGGINS	515.123.8080	07-JUN-02	AC_MGR	12008		101
206	William	Gietz	WGIETZ	515.123.8181	07-JUN-02	AC_ACCOUNT	8300		205



"OPTION 2 Sort"

SELECT *
FROM employees
WHERE hire_date BETWEEN '01-JAN-01'
AND '01-JAN-04'
ORDER BY hire_date;

102	Lex	De Haan	LDEHAAN	515.123.4569	13-JAN-01	AD_VP	17000	
205	Shelley	Higgins	SHIGGINS	515.123.8080	07-JUN-02	AC_MGR	12008	
204	Hermann	Baer	HBAER	515.123.8888	07-JUN-02	PR_REP	10000	
206	William	Gietz	WGIETZ	515.123.8181	07-JUN-02	AC_ACCOUNT	8300	
203	Susan	Mavris	SMAVRIS	515.123.7777	07-JUN-02	HR_REP	6500	
109	Daniel	Faviet	DFAVIET	515.124.4169	16-AUG-02	FI_ACCOUNT	9000	
108	Nancy	Greenberg	NGREENBE	515.124.4569	17-AUG-02	FI_MGR	12008	
114	Den	Raphaely	DRAPHEAL	515.127.4561	07-DEC-02	PU_MAN	11000	
122	Payam	Kaufling	PKAUFLIN	650.123.3234	01-MAY-03	ST_MAN	7900	
115	Alexander	Khoo	AKHOO	515.127.4562	18-MAY-03	PU_CLERK	3100	
100	Steven	King	SKING	515.123.4567	17-JUN-03	AD_PRES	24000	
137	Renske	Ladwig	RLADWIG	650.121.1234	14-JUL-03	ST_CLERK	3600	



====================== IN operator ===============================


IN operator

QUERY: show all employes who works in any one of these departmens id
		90, 60,100,130,120

------- "OPTION 1"

SELECT *
FROM employees
WHERE DEPARTMENT_ID = 90 
OR DEPARTMENT_ID = 60
OR DEPARTMENT_ID = 100 
OR DEPARTMENT_ID = 130
OR DEPARTMENT_ID = 120;

result:

103	Alexander	Hunold	AHUNOLD	590.423.4567	03-JAN-06	IT_PROG	9000		102
104	Bruce	Ernst	BERNST	590.423.4568	21-MAY-07	IT_PROG	6000		103
105	David	Austin	DAUSTIN	590.423.4569	25-JUN-05	IT_PROG	4800		103
106	Valli	Pataballa	VPATABAL	590.423.4560	05-FEB-06	IT_PROG	4800		103
107	Diana	Lorentz	DLORENTZ	590.423.5567	07-FEB-07	IT_PROG	4200		103
100	Steven	King	SKING	515.123.4567	17-JUN-03	AD_PRES	24000		
101	Neena	Kochhar	NKOCHHAR	515.123.4568	21-SEP-05	AD_VP	17000		100
102	Lex	De Haan	LDEHAAN	515.123.4569	13-JAN-01	AD_VP	17000		100
108	Nancy	Greenberg	NGREENBE	515.124.4569	17-AUG-02	FI_MGR	12008		101
109	Daniel	Faviet	DFAVIET	515.124.4169	16-AUG-02	FI_ACCOUNT	9000		108
110	John	Chen	JCHEN	515.124.4269	28-SEP-05	FI_ACCOUNT	8200		108
111	Ismael	Sciarra	ISCIARRA	515.124.4369	30-SEP-05	FI_ACCOUNT	7700		108
112	Jose Manuel	Urman	JMURMAN	515.124.4469	07-MAR-06	FI_ACCOUNT	7800		108
113	Luis	Popp	LPOPP	515.124.4567	07-DEC-07	FI_ACCOUNT	6900		108

------- "OPTION 2"

SELECT *
FROM employees
WHERE DEPARTMENT_ID IN (90,60,100,130,120);

result:

103	Alexander	Hunold	AHUNOLD	590.423.4567	03-JAN-06	IT_PROG	9000		102
104	Bruce	Ernst	BERNST	590.423.4568	21-MAY-07	IT_PROG	6000		103
105	David	Austin	DAUSTIN	590.423.4569	25-JUN-05	IT_PROG	4800		103
106	Valli	Pataballa	VPATABAL	590.423.4560	05-FEB-06	IT_PROG	4800		103
107	Diana	Lorentz	DLORENTZ	590.423.5567	07-FEB-07	IT_PROG	4200		103
100	Steven	King	SKING	515.123.4567	17-JUN-03	AD_PRES	24000		
101	Neena	Kochhar	NKOCHHAR	515.123.4568	21-SEP-05	AD_VP	17000		100
102	Lex	De Haan	LDEHAAN	515.123.4569	13-JAN-01	AD_VP	17000		100
108	Nancy	Greenberg	NGREENBE	515.124.4569	17-AUG-02	FI_MGR	12008		101
109	Daniel	Faviet	DFAVIET	515.124.4169	16-AUG-02	FI_ACCOUNT	9000		108
110	John	Chen	JCHEN	515.124.4269	28-SEP-05	FI_ACCOUNT	8200		108
111	Ismael	Sciarra	ISCIARRA	515.124.4369	30-SEP-05	FI_ACCOUNT	7700		108
112	Jose Manuel	Urman	JMURMAN	515.124.4469	07-MAR-06	FI_ACCOUNT	7800		108
113	Luis	Popp	LPOPP	515.124.4567	07-DEC-07	FI_ACCOUNT	6900		108



TASK: show all employees who work as any of these jobs:
		IT_PROG, SA_REP, FI_ACCOUNT, AD_VP
		sort by job IDS

-------- "OPTION 1"

SELECT *
FROM employees
WHERE job_id IN ('IT_PROG','SA_REP','FI_ACCOUNT','AD_VP')
ORDER BY job_id;

result: 42 results

101	Neena	Kochhar	NKOCHHAR	515.123.4568	21-SEP-05	AD_VP	17000		100
102	Lex	De Haan	LDEHAAN	515.123.4569	13-JAN-01	AD_VP	17000		100
113	Luis	Popp	LPOPP	515.124.4567	07-DEC-07	FI_ACCOUNT	6900		108
109	Daniel	Faviet	DFAVIET	515.124.4169	16-AUG-02	FI_ACCOUNT	9000		108
110	John	Chen	JCHEN	515.124.4269	28-SEP-05	FI_ACCOUNT	8200		108



=========================== LIKE OPERATOR IN SQL % =============================

'e%' = starts with e
'%e' = ends with e
'%e%'= contains e 


 LIKE OPERATOR IN SQL

 LIKE is used to do partial searches 

 '%' means any or no characters 

 QUERY: List all employees whose first name starts with N

"OPTION 1"

SELECT *
FROM employees
WHERE first_name LIKE 'N%';

result 

154	Nanette	Cambrault	NCAMBRAU	011.44.1344.987668	09-DEC-06	SA_REP	7500	0.2	145
108	Nancy	Greenberg	NGREENBE	515.124.4569	17-AUG-02	FI_MGR	12008		101
101	Neena	Kochhar	NKOCHHAR	515.123.4568	21-SEP-05	AD_VP	17000		100
184	Nandita	Sarchand	NSARCHAN	650.509.1876	27-JAN-04	SH_CLERK	4200		121


++++ TASK: show all employees whose last name ends with 'a'

"OPTION 2"

SELECT *
FROM employees
WHERE last_name LIKE '%a';

result:

106	Valli	Pataballa	VPATABAL	590.423.4560	05-FEB-06
111	Ismael	Sciarra	ISCIARRA	515.124.4369	30-SEP-05
116	Shelli	Baida	SBAIDA	515.127.4563	24-DEC-05
167	Amit	Banda	ABANDA	011.44.1346.729268	21-APR-08


++++ TASK: list all employees who started working on month of february


SELECT *
FROM employees
WHERE hire_date LIKE '%FEB%';

result: 13 people 

106	Valli	Pataballa	VPATABAL	590.423.4560	05-FEB-06	IT_PROG
107	Diana	Lorentz	DLORENTZ	590.423.5567	07-FEB-07	IT_PROG
131	James	Marlow	JAMRLOW	650.124.7234	16-FEB-05	ST_CLERK
136	Hazel	Philtanker	HPHILTAN	650.127.1634	06-FEB-08	ST_CLERK
139	John	Seo	JSEO	650.121.2019	12-FEB-06	ST_CLERK
165	David	Lee	DLEE	011.44.1346.529268	23-FEB-08	SA_REP
171	William	Smith	WSMITH	011.44.1343.629268	23-FEB-07	SA_REP
181	Jean	Fleaur	JFLEAUR	650.507.9877	23-FEB-06	SH_CLERK
183	Girard	Geoni	GGEONI	650.507.9879	03-FEB-08	SH_CLERK
185	Alexis	Bull	ABULL	650.509.2876	20-FEB-05	SH_CLERK
187	Anthony	Cabrio	ACABRIO	650.509.4876	07-FEB-07	SH_CLERK
192	Sarah	Bell	SBELL	650.501.1876	04-FEB-04	SH_CLERK
201	Michael	Hartstein	MHARTSTE	515.123.5555	17-FEB-04	MK_MAN



++++ TASK: list all employees who started working on month of february or in 
			MARCH or in APRIL

"OPTION 1"

SELECT *
FROM employees
WHERE hire_date LIKE '%FEB%'
OR  hire_date LIKE '%MAR%'
OR  hire_date LIKE '%APR%';

result: 27 total

107	Diana	Lorentz
112	Jose Manuel	Urman
121	Adam	Fripp
128	Steven	Markle
131	James	Marlow
132	TJ	Olson
136	Hazel	Philtanker


++++ TASK: list all employees whos last name second letter is 'a'

"OPTION 1"

SELECT *
FROM employees
WHERE last_name LIKE '_a%'; -- second letter on last name only 

Result: 33 people

106	Valli	Pataballa
109	Daniel	Faviet
114	Den	Raphaely
116	Shelli	Baida
122	Payam	Kaufling
125	Julia	Nayer


++++ TASK: list all employees whose first name contains either 'a' or 'e' or 'b'

"OPTION 1"
SELECT *
FROM employees
WHERE first_name LIKE '%a%'
OR first_name LIKE '%e%'
OR first_name LIKE '%b%';

result: 95 people 

100	Steven	King
101	Neena	Kochhar
102	Lex	De Haan
103	Alexander	Hunold
104	Bruce	Ernst

++++ TASK: list all employees whose whose last name contains 2 lowercase 'a'

"OPTION 1"

SELECT *
FROM employees
WHERE last_name LIKE '%a%a%'; -- contains 2 lowercase a

results: 10

Lex	De Haan
Valli	Pataballa
Ismael	Sciarra
Den	Raphaely
Shelli	Baida
Peter	Vargas
Gerald	Cambrault
Nanette	Cambrault
Amit	Banda
Nandita	Sarchand


==================== rownum <= 5 =============================

MYSQL: limit numberOfrows

++++ QUERY: show first 5 employees in company.

SELECT * 
FROM employees
WHERE rownum <= 5;

result:

Steven	King
Neena	Kochhar
Lex	De Haan
Alexander	Hunold
Bruce	Ernst


++++ TASK: show 7 top highest salary employees

"OPTION 1"

==================== NULL in SQL =============================

NULL in SQL

QUERY: show all lastnames, salaries, and commissions

"OPTION 1"
SELECT last_name, SALARY , commission_pct
FROM employees;

King	24000	NULL
Kochhar	17000	NULL
De Haan	17000	NULL
Hunold	9000	NULL


"OPTION 2" -- IS NOT NULL

SELECT last_name, SALARY , commission_pct
FROM employees
WHERE commission_pct IS NOT NULL;

Russell	14000	0.4
Partners	13500	0.3
Errazuriz	12000	0.3
Cambrault	11000	0.3
Zlotkey	10500	0.2


"OPTION 3" -- IS NULL

SELECT last_name, SALARY , commission_pct
FROM employees
WHERE commission_pct IS NULL;

King	24000	
Kochhar	17000	
De Haan	17000	
Hunold	9000	
Ernst	6000	


==================== FUNCTIONS in SQL =============================
ALso known as methods in SQL


IN SQL all functions return a Values 
there is no void functions

2 types of functions in Sql:
	1: single row functions
	2: multiple row functions
		aggregate functions
		group functions

SINGLE ROW FUNCTIONS: function will run for each row and 
					return a value for each row. 

MULTIPLE ROW FUNCTIONS: function will run for many rows
					and return a single value


------------- SINGLE ROW FUNCTIONS ------------------

LOWER, UPPER, INITCAP

'++++ UPPER CASE ++++'

++++ QUERY: show all first and last names all in uppercase

"METHOD"

SELECT UPPER(first_name), UPPER(last_name)
FROM employees;

result:

ELLEN	ABEL
SUNDAR	ANDE
MOZHE	ATKINSON
DAVID	AUSTIN
HERMANN	BAER


'++++ LOWER CASE, UPPER CASE, INITIAL CAPITAL ++++'

++++ QUERY: show all emails lowercase uppercase and initial capital

"METHOD"

SELECT LOWER(EMAIL), UPPER(EMAIL),INITCAP(EMAIL)
FROM employees;

results:

abanda	ABANDA	Abanda
abull	ABULL	Abull
acabrio	ACABRIO	Acabrio


'++++ Length function ++++'

++++ QUERY: show all employees whos last name is 6 characters

"METHOD"

SELECT *
FROM employees
WHERE LENGTH(last_name) = 6;

results:

Alexander	Hunold
David	Austin
Daniel	Faviet
Sigal	Tobias
Guy		Himuro




==================== CONCAT SUBSTR LENGTH INSTR =====================

CONCAT, SUBSTR,  LENGTH, INSTR
TRIM, REPLACE

++++ QUERY: create a password for each employee that consists
			of first 3 letters of firstname and first 3 letters of last name.

"METHOD"

SELECT SUBSTR(first_name,0,3) || SUBSTR(last_name,0,3)
FROM employees;

result

EllAbe
SunAnd
MozAtk

"RENAME PASSWORD" -- as password

SELECT SUBSTR(first_name,0,3) || SUBSTR(last_name,0,3) AS "Employee passwords"
FROM employees;

result

EllAbe
SunAnd
MozAtk

------ CONVERT PASSWORD TO LOWERCASE ------

"METHOD"

SELECT LOWER(SUBSTR(first_name,0,3) || SUBSTR(last_name,0,3)) AS "Employee passwords"
FROM employees;

result:

ellabe
sunand
mozatk

==================== ROUND, TRUNC NUMBER RELATED =====================

NUMBER Related single row functions

ROUND. = rounds number
TRUNC  = 
MOD    =


-- QUERY: show all salaries and commision amount for employees who earn commissions.

SELECT salary, salary + salary * commission_pct / 4
FROM employees
WHERE commission_pct IS NOT null;


SELECT ROUND(23.43)
FROM dual;

23

SELECT ROUND(23.43,1) <- it will take the 1 decimal  ,1
FROM dual;

23.4

--- QUERY: show all employees whos employee ID is even 

"METHOD"

SELECT *
FROM employees
WHERE MOD(employee_id,2) = 0;

result:

100	Steven	King
102	Lex	De Haan
104	Bruce	Ernst
106	Valli	Pataballa

"METHOD 2"

SELECT *
FROM employees
WHERE NOT MOD(employee_id,2) = 0;

result

101	Neena	Kochhar
103	Alexander	Hunold
105	David	Austin
107	Diana	Lorentz

"METHOD 3"

SELECT *
FROM employees
WHERE  MOD(employee_id,2) <> 0;

result:

101	Neena	Kochhar
103	Alexander	Hunold
105	David	Austin


================ COUNT, MAX, MIN, AVG ===================

------------- MULTIPLE ROW FUNCTIONS ----------------

MULTIPLE row functions
group functions
aggregate functions


---- "PROCESSES MULTIPLE ROWS AND RETURN SINGLE RESULT / ROW"

COUNT, MAX, MIN, AVG

+++++ QUERY: show number of employees in the company

"METHOD"
SELECT COUNT(employee_id)
FROM employees;

resul:

107

+++++ QUERY: show number of employee who are IT_PROGs

"METHOD"

SELECT COUNT(employee_id)
FROM employees
WHERE job_id = 'IT_PROG';5

result:

5

+++++ QUERY: show number of unique job IDS

"METHOD"

SELECT COUNT (DISTINCT job_id)
FROM employees;

result:

19



------------  MAX shows highest number. -----------

++++ QUERY: SHOW the maximum salary in company

"METHOD"
SELECT MAX(salary)
FROM employees;

SELECT MAX(salary)
FROM employees;

++++ QUERY: show the highest employee id.

"METHOD"
SELECT MAX(employee_id)
FROM employees;

206

++++ QUERY: show max salary min salary round average salary


SELECT MAX(salary), MIN(salary), ROUND(AVG(salary),1)
FROM employees;

24000	2100	6461.8


------------ SUM = sums the values for each record -------

++++ QUERY: show the companies montly payroll amount

"METHOD"
SELECT SUm(salary) AS payroll
FROM employees;

result:
691416


----------- GROUP BY KEYWORD / CLAUSE --------------

IT creates sub groups and is used with groups functions

++++ QUERY: Display department id and count of people who work for 
			department 

"METHOD"

SELECT department_id, count(*)
FROM employees
Group BY department_id;

results:

100	6
30	6
	1
90	3
20	2
70	1
110	2


++++ QUERY: Display job ids and count of people who work for those jobs

"METHOD"

SELECT job_id, count(*)
FROM employees
GROUP BY job_id;

RESULT:

AC_ACCOUNT	1
AC_MGR		1
AD_ASST		1
AD_PRES		1
AD_VP		2

+++++++++++++++ MUST KNOW ABOUT GROUP BY ++++++++++++++++++++++

When ever you use a group function in SELECT statement and
you include also columns that are not with GROUP functions
those columns must be in GROUP BY clause/keyboard

example 1: 'one group job_id'
	SELECT job_id, count(employee_id)
	FROM employees
	GROUP BY job_id; <- it must be the same as job_id and must 
						have GROUP BY method

example 2:'2 groups job and department'
	SELECT job_id, count(employee_id), department_id
	FROM employees
	GROUP BY job_id, department_id;

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

================= HAVING keyboard ====================

IT is used when ever we need to filter or put condition
that involves a group function like ( MIN, MAX, etc)

+++ QUERY: Display department id and min salary for the departments that have
		min salary less than 3500


"METHOD"

SELECT department_id, MIN(salary)
FROM employees
GROUP BY department_id
HAVING MIN (salary) < 3500;

result:

30	2500
50	2100

+++ QUERY: Display job ids and count of ppl for those jobs that are 
			more than 4 people

"METHOD"

SELECT job_id, count(*)
FROM employees
GROUP BY job_id
HAVING count(*) > 4;

RESULT:

FI_ACCOUNT	5
IT_PROG		5
PU_CLERK	5
SA_MAN		5
SA_REP		30
SH_CLERK	20
ST_CLERK	20
ST_MAN		5



~~~~~~~~~~~~~~ SUMARY ~~~~~~~~~~~~~~

	comaprison OPERATORS
	between AND
	IN 
	LIKE
	ROWNUM
	FUNCTIONS
		SINGLE ROW
		aggregate
			GROUP BY
			HAVING









