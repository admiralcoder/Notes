Creating Contacts Feature
cucumber-testng-automation project
-------------------------------------------------------
Feature: Creating contacts

  Scenario: Create contact using a map
    Given I logged into suiteCRM
    When I create a new contact
      | first_name | John  |
      | last_name  | Smith |
Then I should see contact information for "John Smith"


-----

	@When("^I create a new contact$")
	public void i_create_a_new_contact(Map<String, String> contacts) {
		// open the create contact dialog
		BrowserUtils.hover(dashboard.createLink);
		dashboard.createContact.click();
		// enter information
		createContact.firsName.sendKeys(contact.get("first_name"));
		createContact.lastName.sendKeys(contact.get("last_name"));
	}

-----

beans == pojo

pojo = plain old java object

te roles, objects products that we have in our application can be 
represented by a bean class 

-------------------------------------------------------------
Contactbean Class 
Student{
	firstName 
	lastName

	getFirstName()
	getLastName()

	setFirstName()
	setLastName()
}





++++ Interview Questions


beans are called pojo and model as well depending on the company you work

- Whats the difference between key and Value in cucumber 





















