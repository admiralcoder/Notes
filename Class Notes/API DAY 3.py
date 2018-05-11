API DAY 3

PASSING PARAMETERS
HEADERS

Json and Json Manipulation

POST METHODS GSON

================================================================



https://www.google.com/search?q=cucumber


search? = end of website
q= key 
cucumber = value


2 Types of parameters in REST SERVICES:

	1: QUERY parameters = is not part of url and passed in key+value format
	those parameters must be defined by API developer
	2: Path parameters
	is a part of url and followed by the end of the full resource url

	http://34.223.219.142:1212/ords/hr/employees

	http://34.223.219.142:1212/ords/hr/employees/100 <- its part of the url (also 
		callsed path parameters)


==============

JSONPATH -> Json path is used to navigate and Manipulate Json data

3 ways to 
		//JsonPath json = response.jsonPath();
		//JsonPath json = new JsonPath(new File(FilePath.json); option 2
		//JsonPath json = new JsonPath(response.asString()); option 3



	@Test
	public void testWithJsonPath() {
		Map<String, Integer> rParamMap = new HashMap<>();
		rParamMap.put("limit", 100);

		Response response = given().accept(ContentType.JSON).and().params(rParamMap).and().pathParam("employee_id", 177)
				.when().get(ConfigurationReader.getProperty("hrapp.baseresturl") + "/employees/{employee_id}");

		JsonPath json = response.jsonPath();
		System.out.println(json.getInt("employee_id"));
		System.out.println(json.getString("last_name"));
		System.out.println(json.getString("job_id"));
		System.out.println(json.getInt("salary"));
		System.out.println(json.getString("links[1].href"));// get specific Element from Array

		List<String> hrefs = json.getList("links.href");
		System.out.println(hrefs);
	}





HOW TO CONVERT JSONTO JAVA OBJECT?

GSON -> is a json parser that is used to convert from java OBJECT
to json and from json to java OBJECT 

--- DEPENDENCY --
		<dependency>
			<groupId>com.google.code.gson</groupId>
			<artifactId>gson</artifactId>
			<version>2.8.2</version>
		</dependency>


------------------------- DE-Serialization -------------------

JSON to java OBJECT is called DE-Serialization


------------------------- Serialization -------------------

Serialization conver java OBJECT to json 



--> Assert Items = Hasitems,hassize etc -> hamcrest matchers
	asserThat().body("items.id",hassize(10))

--> JsonPath -> to Manipulate json for more complex assertions etc

-> DE-Serialization using GSON
		
		Json to Map
		Json to List<Map>
			Map1. <-> Map2 (excel file)






































