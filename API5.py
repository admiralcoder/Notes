API day 2

04/24/2018

==================== Scenario ===================================

Scenario Automation
Cucumber + RestAssured

Given Content Type and Accept Type is Json
When I post a new Employee with "1234" ID 
Then Status code is 201
And Response Json should contain Employee info
When I send a GET request with "1234" id 
Then Status code is 200
And employee JSON response data should match the posted JSON data


TEST DATA URL:
http://34.223.219.142:1212/ords/hr/employees/

Json of Request body / payload:
	Example: 
	{		
			"employee_id": 669,
            "first_name": "Lion",
            "last_name": "King",
            "email": "Lking",
            "phone_number": "515.123.2312",
            "hire_date": "2018-24-17T07:30:00Z",
            "job_id": "AD_PRES",
            "salary": 24000,
            "commission_pct": null,
            "manager_id": null,
            "department_id": 90,
    }

// to create in post man click on

new tab -> Post -> Headers -> select for key 		Value
										Accept = Application/JSON
										Content-type=Application/Json

-> Body -> click raw and paste your Example then -> click SEND -> 201 code

// to check if it was process then go to url again
http://34.223.219.142:1212/ords/hr/employees/669/


==================================================================
 <---------- sending request --------->
import static io.restassured.RestAssured.given;
import static org.testng.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

import org.testng.annotations.Test;

import com.app.utilities.ConfigurationReader;

import io.restassured.http.ContentType;
import io.restassured.response.Response;

public class APIDay5_POSTthenGET {

	/*
	 * Given Content type and Accept type is Json
		When I post a new Region with "AB" id
		Then Status code is 201
		And Respons Json should contain Region info
		When i send a get Request with "AB" id 
		Then status code is 200
		And employees JSON Response Data should match the posted JSON data  
	 */
	
	@Test
	public void PostEmployeeThenGetEmployee() {
		
		int randomID = new Random().nextInt(9999);
		
		Map reqEmployee = new HashMap();
		String url=ConfigurationReader.getProperty("hrapp.baseresturl") + "/employees/";
		
		reqEmployee.put("employee_id", randomID);
		reqEmployee.put("first_name", "BOBIR");
		reqEmployee.put("last_name", "UMARKULOV");
		reqEmployee.put("email", "BO"+randomID);
		reqEmployee.put("phone_number", "412.777.2277");
		reqEmployee.put("hire_date", "2016-01-17T04:00:00Z");
		reqEmployee.put("job_id", "IT_PROG");
		reqEmployee.put("salary", 7700);
		reqEmployee.put("commission_pct", null);
		reqEmployee.put("manager_id", null);
		reqEmployee.put("department_id", 90);
		
	Response response =	given().accept(ContentType.JSON)
		.and().contentType(ContentType.JSON)
		.and().body(reqEmployee)
		.when().post(url);
	
	assertEquals(response.statusCode(),201);
		
	Map postResEmployee = response.body().as(Map.class);
	
	for (Object key : reqEmployee.keySet()) {
		System.out.println(postResEmployee.get(key)+"<>"+ reqEmployee.get(key));
		assertEquals(postResEmployee.get(key), reqEmployee.get(key));
	}
		
		response = given().accept(ContentType.JSON)
					.when().get(url+randomID);
		
		assertEquals(response.statusCode(),200);
		
		Map getResMap = response.body().as(Map.class);
		
		for (Object key : reqEmployee.keySet()) {
			System.out.println(key + ": "+reqEmployee.get(key)+"<>");
			assertEquals(postResEmployee.get(key), getResMap.get(key));
			assertEquals(getResMap.get(key), reqEmployee.get(key));
	}
	
//		
//		Employees employees = new Employees();
//		employees.setEmployee_id(7887);
//		employees.setFirst_name("Bobir");
//		employees.setLast_name("Umarkulov");
//		employees.setEmail("UMARKULOV");
//		employees.setPhone_number("715.123.4563");
//		employees.setHire_date("2016-01-17T04:00:00Z");
//		employees.setJob_id("IT_PROG");
//		employees.setSalary(12000);
//		employees.setDepartment_id(90);
		
		
				
				
	}
}



























