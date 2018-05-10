TDD vs BDD

cucumber DBB

learn a new language

TDD --> Test Driven Development 

in TDD we write the test first, then write the code
Its done in the Development phase, devs write units tests before they write 
they actual code.
they write small test, they try to pass It
then continue with same process

TDD does not involve all the parties of the software Development, 
it only includes the developers maybe the BA who explains the functionality

New Process ------- BDD--------

we need a process which involved all artiens in the same conversation

Agile Story: Story that describes a certain behavior of an application

1)
			-As a customer 
			-I want to be able to log in 
			-To see my information

2)
			-As a renter
			-I want to be able to search apartments
			-so that i can find a palce to renter

Product Owner / BA represent the customer

Developers : write the code

Testers : test the application

Acceptance Criteria --> conditions that mark the Story Complete

Sample of a test Case:

	Given the renter is on the search page
	when the renter searches for apartments
	Then the results should display the available apartments

==================== CUCUMBER BDD ========================

tools used to facilitate the collaboration during the BDD process.
IT enables explaining the story and the Acceptance criteria in
an easy language.
-- must be created inside scr/test/resources

/first-cucumber-project/src/test/resources -->cucumber test will be written in this package 

in cucumber tests will be in feature files. feature files will have the scenarios that test a certain feature
or functionality

 example: 

 			homepage_test.feature


#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
@tag
Feature: Title of your feature
  I want to use this template for my feature file

  @tag1
  Scenario: Title of your scenario
    Given I want to write a step with precondition
    And some other precondition
    When I complete action
    And some other action
    And yet another action
    Then I validate the outcomes
    And check more outcomes

  @tag2
  Scenario Outline: Title of your scenario outline
    Given I want to write a step with <name>
    When I check for the <value> in step
    Then I verify the <status> in step

    Examples: 
      | name  | value | status  |
      | name1 |     5 | success |
      | name2 |     7 | Fail    |





Feature: the keyword is palce on top of the feature files it is used ot descrive
what functionality is being tested in this feature file.

Commenting: in a feature file is done using # 

Scenario: test case in cucumber 

Given
When
Then.   ----> feature file steps
And
But


Feature files are run using junit/testng runners


@RunWith(Cucumber.class)--> this is used to make this file run the feature
files this will execute the feature files which has the tests


@RunWith --> comes from junit
(Cucumber.class)-->teslls that jnit shuild run this class as cucumber test


Step Definitions --> for each step/line in the scenario cucumber generates
matching java method. this method is known as the step Definition for that
cucumber step. 


Run Cukes will read the feature filefor each step in teh feature file it will execute
the matching step definition in the step definition we write java
code to implement that cucumber steps we can call selenium methods and projects

========== CukesRunner.java ==============

dryRun. ---> cucumber option to turn on / off the actual execution if 
dryRun=true --> cucumber will not execute the tests it will only check if the 
cucumber steps are implemented or not if there are any unimplmented steps.

package tesla;

import org.junit.runner.RunWith;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(
		dryRun=true
		)
public class CukesRunner {}

======== homepagestepDefinitions.java =========

package tesla;

import static org.junit.Assert.assertTrue;


import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import io.github.bonigarcia.wdm.WebDriverManager;


public class HomePageStepDefinitions {
	// this is a regular expression / regex that cucumber
	// uses to match a method to a cucumber step

	WebDriver driver;

	@Given("^I am on the home page$")
	public void i_am_on_the_home_page() {
		WebDriverManager.chromedriver().setup();
		System.out.println("I am going to www.tesla.com");
		driver = new ChromeDriver();
		driver.get("https://www.tesla.com/");

	}

	@When("^I click on the model S link$")
	public void i_click_on_the_model_S_link() {
		System.out.println("clicking on the model S link");
		driver.findElement(By.linkText("MODEL S")).click();
		;

	}

	@Then("^Model S homepage should be displayed$")
	public void model_S_homepage_should_be_displayed() {
		System.out.println("Verifying the Model S home Page");
		assertTrue(driver.getTitle().contains("Model S"));
		System.out.println(driver.getTitle()+"------------------");
	}
	
	
}




======== Gherkin terms =========
Gherkin language used by the feature files

Feature, Scenario, Given, Then













