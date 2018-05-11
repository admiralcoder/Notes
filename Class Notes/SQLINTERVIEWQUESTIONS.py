

============================== SQL ====================

Do you write SQL tables? 
	No but i know how to read it using SQL, I am familiar with backend testing


DATABASE SCHEMA -> is a chart that shows all tables and how they are related 
	to one another.


	ONE TO MANY relation -> One Department  can have many employees

	many to many relation -> One empleyee can have only one department

WHAT IS FOREIGH KEY?
	-> WHEN A COLUMN  IS USED THAT IS PRIMARY KEY IN ANOTHER TABLE 

What kind of data Types can you use on SQL? and give me example
	->Columns in SQL can accept only specific data type.

how do you sort results in SQL?

	ORDER BY ... id or name or emp id 

HOW DOES DISTICT WORK ON YOUR CURRENT SQL ?
	
	SELECTS NOT DUPLICATE NAMES OR ID OR DEPARTMENT
	EXAMPLE: IT, HR, IT, 
	RESULT:  IT, HR

What operator do you use to select if a specific letter contains 'b'on a list of names?
	we use % % percent  based on the letter we get we can use for example
	first_name LIKE %e% 

how do you see top 5 records?

	
whats difference between GROUP BY and ORDER BY?

	GROUP BY is used when ever we use multiple row functions
	and it creates sub groups from larger group.

	ORDER BY sorts the results either in ascending or descending manner.

difference between HAVING vs WHERE?

	HAVING: We use HAVING when our condition includes a GROUP function 

	WHERE: We use WHERE when our condidtion DOES NOT include GROUP function


Whats the difference between Char? and varChar2?
	Char is used for fixed length characters
	varChar2 is more flexible and it will only take space needed

how can you check if your company has a database schema?

	if you dont have database schema you can do the following
	someone gave you access to database and there is no database SCHEME

	STEP 1: display all tables

	MySQL: has a command 

	show tables;

	ORACLE: Select table_name from user_tables;
		
	STEP 2: DESCRIBE command to see Columns and relations.


What is joins in SQL?
	
	
	
Whats table Alias?

	Renaming the table name only for reporting it doesnt change the database. 

How to find second lowest salary in a QUERY?

	SELECT * FROM employees e1 
	WHERE 2 = (SELECT COUNT(DISTICT(salary))FROM employees e2
	WHERE e1.salary <= e2.salary);

Can you exaplain UNION on SQL ?

	returns combined rows from 2 independent queries and removes
	duplicates and sorts them

Whats difference between INNER JOIN and UNION?

	INNER JOIN is used to retrieve matching data from multiple tables
	UNION is used to retrieve data from multiple queries and it removes 
	duplicates and sorts the result.

UNION VS UNION ALL?
	
	UNION -> returns combined rows from 2 independent queries and removes
		duplicates and sorts them

	UNION ALL -> returns combined rows from 2 independent queries and does not
	remove duplicated and does not sort them

Do you have the experience with SQL?

Yes, I have worked with relational databases and i am very confortable
with DDL and DML commands.




===== JAVA INTERVIEW =========

whats enumaration in java?

	we can use enum type 
	it is used to store constant values
	public enum cards{
	VISA, MASTERCARD,AMEX
	}



===== Selenium =======

how many  Unit testing do you do per day?
	on " Unit test & deploy changes to server "
	Done by jenkins automatically every time developer checks in a new code
	only done by developers



====== API INTERVIEW QUESTIONS ====

*** how do you test API?
I make sure that all endpoints/urls of rest api work as expected i send GET,POST,PUT 
or d


How do you test Rest API?

	I verify if each REST API endpoint is working as expected.
	I send POST,PUT,GET,DELETE type of requests
	and verify response status code and respose body 

	i also do positive and negatice Testing of API
	when i do positive testing i send valid request parameters valid headers 
	valid request json body and verify 
	that response status code is 200 and Json response body data is as expected

	when i do negative testing i send invalid request parameters or invalid headers or
	invalid request Json body and verify that response status code is not 200 and Json 
	respose body contains error message.



===== POSTMAN interview QUESTIONS======

whats status 200?
	- means that the search for API is OK



============== JSON API ========

how to you conver json to list map from post man?

	we deserialize json to list <Map>

	List<Map> regions = json.getList("items",Map.class);//deserialize json to list<Map>


what is constrains what is it? ( API related question)
 	unique id unique url etc. 
