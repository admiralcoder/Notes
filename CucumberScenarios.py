Data Driven Testing

Executing same test case against different sets of data

We run the same test case following the same steps using different input

Scenario 1:
	Scenario: Create contact using CREATE page
    Given I logged into suiteCRM
    And I open the create contact page
    And I enter the first name "Bruce" and the last name "Lee"
    And I enter the phone number "1800-889-8829"
    And I enter the department "Actor"
    When click on the save button
    Then I should see contact information for "Bruce Lee"

Scenario 2: 
 	 Scenario: Create contact using CREATE page
    Given I logged into suiteCRM
    And I open the create contact page
    And I enter the first name "El" and the last name "kiko"
    And I enter the phone number "1800-889-8829"
    And I enter the department "Actor"
    When click on the save button
    Then I should see contact information for "El Kiko"


flow should not change based on data. we do the same test over and over



Scenario Outline: is just liek a secenario but used for data Driventesting


with scenario Outline we have the same cucumber steps, but we have a data after 
the scenario as a table key word Example.

















