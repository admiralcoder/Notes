API DAY 2

RESTful API Testing


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

============================== ORACLE ORDS REST API =========================

ORDS = oracle Rest Data Services

ORDS is a tool/ technology that orcle built to make easy for creating RESTful APIs 
on Oracle Database


------------------ GET positive Scenario using Postman ---------------------

Scenario 1
GET - positive scenario: 

		When i send a GET request to REST url http://34.223.219.142:1212/ords/hr/employees

		Then response status should be 200

		And response Json body should contain employees data


Scenario 2
GET - positive scenario: 

		When i send a GET request to REST url http://34.223.219.142:1212/ords/hr/countries/US

		And accept Type is "Application/json"

		Then response status should be 200

		And Country name should be "UNITED STATES" for country id "US" in Json response body



====================== GET REQUEST WITH HEADERS  =============================


GET REQUEST WITH HEADERS 

Content Type Accept

Header are also in key+value format they are used to provide additional information 
about request / response


Accept --> Application / Json
		-> APplication / xml

I am expecting Json/xml data back. And API needs to Support it otherwise it will send back
default one. 




---------------------------- REST ASSURED LIBRARY -----------------

We are using rest-assured library in java 


It is a BDD Style library = BEHAVIOR DRIVER 
							style is WHEN i do this 
							AND i get this
							THEN am still doin...


<!-- https://mvnrepository.com/artifact/io.rest-assured/rest-assured -->
<dependency>
    <groupId>io.rest-assured</groupId>
    <artifactId>rest-assured</artifactId>
    <version>3.0.7</version>
    <scope>test</scope>
</dependency>


"OPTION 2"
https://github.com/rest-assured/rest-assured/wiki/GettingStarted#maven--gradle-users

<dependency>
      <groupId>io.rest-assured</groupId>
      <artifactId>rest-assured</artifactId>
      <version>3.0.7</version>
      <scope>test</scope>
</dependency>


APACHE CLIENT is another library for JAVA for REST APIs/Services testing

https://hc.apache.org/

----------------------------------------------------------------------------

We are using rest-assured library in java 

































