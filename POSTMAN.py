POSTMAN

is a RESTAPI client tool that helps to test rest api urls

it is popular for both developers and testers

testers use it for manual testing


--- WILL SHOW EMPLOYEES FROM DATABASE USING API ----

http://34.223.219.142:1212/ords/hr/employees/


--- WILL SHOW departments FROM DATABASE USING API ----

http://34.223.219.142:1212/ords/hr/departments/

EXAMPLE: 

"SCENARIO"

When i send a GET request to http://34.223.219.142:1212/ords/hr/departments/
Then response status code must be 200
And I should see departments data in jason format


- WHAT IS 200? 
	this is the status code 200 means OK once you send GET on the status report you see 200 for OK

-


"SCENARIO"

When i send a GET request to http://34.223.219.142:1212/ords/hr/employees/101
Then response status code must be 200
And I should see employee Neenas information in Jason format


https://httpstatuses.com/

first thing you verify  is response status CODE 
then you verify response body .jason/xml

==================== STATUS CODE =============

2×× Success
200 --> OK

4×× Client Error
400 --> Bad Request client error

5×× Server Error
500 --> Internal Server Error



