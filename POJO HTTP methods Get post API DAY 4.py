
WARM UP

	given content type is Json
	and Limit is 10
	When I send request to Rest API url:
	http://34.223.219.142:1212/ords/hr/regions
	Then I should see following data
		1 Europe
		2 Americas
		3 Asia
		4 Middle East and Africa

=================== HTTP METHODS =================

	HTTP METHODS:

	GET 		-> 

	POST		-> CREATE

	PUT			->

	DELETE		-> REMOVE


EXAMPLE : 
{
	"region_id" : 586,
	"regrion_name" : "AlexBoliviano region"
}

/ Post Scenario:

given content type is Json
And Accept type is json
When I send POST request to 
http://34.223.219.142:1212/ords/hr/regions
with request body:
{
	"region_id" : 586,
	"regrion_name" : "AlexBoliviano region"
}
Then Status code should be 200
And response body should match request body


======== Generic Meanings of HTTP Response Status Codes =======

The following table lists HTTP response status codes and their meanings:

Response Status Code			Meaning
200			 	Ok				Successful requests other than creations and deletions.

201 			Created			Successful creation of a queue, topic, temporary queue, temporary topic, session, producer, consumer, listener, queue browser, or message.

204 			No content 		Successful deletion of a queue, topic, session, producer, 
								or listener.

400 			Bad request 	The path info doesnt have the right format, 	
								or a parameter or request body value doesnt have the 
								right format, or a required parameter is missing, 
								or values have the right format but are invalid in
								some way (for example, destination parameter does not exist,
								content is too big, or client ID is in use).

403 			Forbidden 		The invoker is not authorized to invoke the operation.

404 			Not Found		The object referenced by the path does not exist.

405 		Method Not allowed 	The method is not one of those allowed for the path.

409 			Conflict 		An attempt was made to create an object that already exists.

500 	Internal Server Error 	The execution of the service failed in some way.


===================




JSON request body

JAVA OBJECT --> JSON


HASHMAP --> JASON   = SEREALIZATION



During Regressin or Smoke test we post everytime

if ID is already used how to re-run our test?

=========================== POJO ===========================

http://www.jsonschema2pojo.org/
Convert JSON schema to POJO by entering

{
	"region_id" : 586,
	"regrion_name" : "AlexBoliviano region"
}
Settings
-JAVA
-JSON
-Gson
= Preview



 CUSTOM CLASSES TO MATCH OUR JSON REQUEST AND RESPONSE 

POJO -> Plain old java Object 

(also knows as BEANS)

{
	"region_id" : 586,
	"regrion_name" : "AlexBoliviano region"
}

public class Region {
	private int region_id;
	private String regrion_name;

	public void setRegion_id(int region_id){
	this.region_id = region_id;
	}

	public void setRegion_name(String region_name){
	this.region_name = region_name;
	}

	public int getRegion_id(){
	return region_id;
	}

		public String getRegion_name(){
	return region_name;
	}

}





==== EXAMPLE 2

EXAMPLE : 

/ Post Scenario:

given content type is Json
And Accept type is json
When I send POST request to 
http://34.223.219.142:1212/ords/hr/countries/
with request body:
{
	"country_id" : "AR",
	"regrion_name" : "Argentina"
	"region_id" : 2
}
Then Status code should be 200
And response body should match request body







============= SERIALIZATION ========


Country reqCountry = new Country();
reqCountry.setCountry_id("bit");
reqCountry.setCountry_name("BOLIVIA");
reqCountry.setRegion_id(new Random().nextInt(99999));


convert to JSON   its called SERIALIZATION


=========== deserialization =============

from JSON 

to 

		CountryResponse resCountry = 
		response.body().as(CountryResponse.class);













