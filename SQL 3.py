SQL 3
04/10/2018


example: AUTOZONE - customer bob goes there and he wants alternator for honda 2015 civic
				    
				    sales person checks on system: part id - 12345 

				    looks inside for item by part id - 12345

				    when he finds it he exactly knows how the product looks like

======================= JOIN in SQL ===========================

DISPLAYING DATA FROM MULTIPLE TABLES

'SCENARIO:' 
		can you create a report that includes :
		Employee ID last name and department id and department
		names for all employees.

'search 1'
SELECT employee_id, last_name, department_id
FROM employees;

'resuls'
100	King	90

'search 2'
SELECT department_name
FROM departments
WHERE DEPARTMENT_ID = 90;

'result'
Executive





types of joins in sql: 

1: inner joins
2: outer joins


================= INNER JOIN ===================

What is inner join ?
	Inner join is used to display data from multiple tables 
	and it returns only matching records. according to joining condition

'QUERY'
		SELECT employee_id, last_name, department_id, department_name
		FROM employees join departments
		ON employees department_id = departments.department_id;

'RESULT'
200	Whalen	10	Administration
201	Hartstein	20	Marketing
202	Fay	20	Marketing

'TASK'
		Display department id and department name city name for all departments

- Example: 

SELECT department_id,department_name,city
FROM departments JOIN locations
ON departments.location_id = locations.location_id;

- Result:

60	IT	Southlake
50	Shipping	South San Francisco
10	Administration	Seattle
30	Purchasing	Seattle
90	Executive	Seattle
100	Finance	Seattle



-------= MORE CONDITIONS same example from top

SELECT department_id,department_name,city
FROM departments JOIN locations
ON departments.location_id = locations.location_id
WHERE department_id = 100;

100	Finance	Seattle


'TASK 2'
		DIsplay all cities country names

SELECT city, country_name
FROM locations inner join countries
on locations.country_id = countries.country_id;


Sydney		Australia
Sao Paulo	Brazil
Toronto		Canada
Whitehorse	Canada
Geneva		Switzerland


'QUERY':
		Display country id country name region id and region name

'sample'
SELECT country_id, country_name, counties.region_id,region_name
FROM countries INNER JOIN regions
ON counties.region_id = regions.region_id;

'result'
NL	Netherlands	1	Europe
FR	France	1	Europe
UK	United Kingdom	1	Europe
DK	Denmark	1	Europe

----------- nickname  TABLE ALIAS ---------------

countries c = c stands for countries its table alias renaming the table
regions r = r stand for regions its table alias renaminig table.

'sample'
SELECT country_id, country_name, counties.region_id,region_name
FROM countries c INNER JOIN regions r
ON counties.region_id = regions.region_id;

'result'
NL	Netherlands	1	Europe
FR	France	1	Europe
UK	United Kingdom	1	Europe
DK	Denmark	1	Europe




"QUERY"
		Employee id, last name, department id, department name, 
		location id, city, country name.

'sample'

FROM employees e JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
JOIN countries c
ON l.country_id = c.country_id;

'result'
100	King	90	Executive
101	Kochhar	90	Executive
102	De Haan	90	Executive
103	Hunold	60	IT
104	Ernst	60	IT

=================== OUTER JOINS =====================


3 Types of outer joins:

	1: Right outer join
	2: left outer join
	3: full outer join

1: Right outer join = is used to display data from multiple tables
	and it returns matching record as well as non matching records from 
	right hand side table.

2: left outer join = is used to display data from multiple tables
	and it returns matching record as well as non matching records from 
	left hand side table.

3: full outer join = is used to display data from multiple tables
	and it returns matching record as well as non matching records from 
	full table.

'QUERY'
		display employee last_name, department_id, department_name
		for departments that have employees and that does not have.

'sample 1 right outer join'

SELECT last_name, d.department_id, department_name
FROM employees e RIGHT OUTER JOIN departments d
ON e.department_id = d.department_id;

'result'

Greenberg	100	Finance
Gietz	110	Accounting
Higgins	110	Accounting
null	120	Treasury
null 	130	Corporate Tax
null 	140	Control And Credit


'sample 2 left outer join'

SELECT last_name, d.department_id, department_name
FROM employees e LEFT OUTER JOIN departments d
ON e.department_id = d.department_id;

'result'
Gietz	110	Accounting
Higgins	110	Accounting
Grant	null	null


'sample 3 Full outer join'

SELECT last_name, d.department_id, department_name
FROM employees e FULL OUTER JOIN departments d
ON e.department_id = d.department_id;

'result'

Livingston	80	Sales
Grant		null
Johnson	80	Sales
Taylor	50	Shipping

Higgins	110	Accounting
Gietz	110	Accounting
null	220	NOC
null	170	Manufacturing

----------- Prints only null ---------

'example to print null noly on table'

SELECT last_name, d.department_id, department_name
FROM employees e FULL OUTER JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id is null;

Grant		
null	220	NOC
null	170	Manufacturing
null	240	Government Sales
null	210	IT Support
null	160	Benefits



SELF JOIN -> when you join 


