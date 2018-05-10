API 04/17/2018

FRONT END			BACK END			DATABASE
	|					|				  |
manual tester		API testing			SQL

--------------------------------------------------------------------------

REST-ASSURED -> library in java that works along with API 

--------------------------------------------------------------------------

What is API?
	- its a messanger that takes a request and sends back a response 

	- Application programing interface = also called WEB SERVICE

	- API is the middle man between DATABASE and front END (CLIENT)

	- API is an application but without UI

	- API enables communication between system

	- API enables secure way of sharing data and functionalities


How API works?

How to test Api manually?


Postman -> this is a tool



CLIENT sends request to - - - > SERVER(WHO IS THE API)

CLIENT sends response to < - - - SERVER(WHO IS THE API)

-------------------
2 Types of API:     |
		
		1: SOAP.    |

		2: REST API |

-------------------

		1: SOAP = simple object access protocol
				  - It uses XML format for request and response
				  - Its platform independent


		2: REST API - is much more popular than SOAP API
					- JASON and XML

also known as RESTFUL API / RESTFUL WEBSERVICES

===========================================================================


JASON = JAVASCRIP OBJECT NOTATION is a lightweight of XML

{
	"id":1
	"name":"KEVIN"
}

KEY + VALUE 
-----------
format



IF API communication happens throught internet we can also call it web SERVICE

REST API is enabling communication between systems

================== HOW TO WE TEST APIs? ==================================

HOW TO WE TEST APIs?

	As we know in api there is request and response communication 

	as testers we send a request to an api and verify the response

'REQUEST ---> types of request in restApi :'
				
				1: GET request 		-> 		READ data like SELECT in SQL
				2: POST request 	-> 		is to CREATE data
				3: PUT request 		-> 		UPDATE data
				4: DELETE request 	-> 		DELETE data

HOW AND WHERE ARE YOU SENDING REQUETS?
	
	A REST API will have endpoints/urls/URis

	example: www.google.com/search

	Builder of API will create public URLs and request are sent to that url




add to resume******

http://petstore.swagger.io/ <==== sample

SWAGGER is a tool for API documentation

**********

UNDERSTANDING API ENDPOINTS/URLS
	BASE URL: 
		/

*** how do you test API?
I make sure that all endpoints/urls of rest api work as expected i send GET,POST,PUT 
or delete request and validate the response

We have swagger for api documentation it gives description of api endpoints and how
to use them






















































