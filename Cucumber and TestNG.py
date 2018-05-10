Cucumber and TestNG

Gherkin Language: Keywords
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

WE HAVE LEARNED SO FAR :

1) JAVA + SELENIUM + TestNG

2) JAVA + SELENIUM + TestNG + MAVEN + GIT

3) JAVA + SELENIUM + JUNIT + CUCUMBER + MAVEN + GIT

4) JAVA + SELENIUM + TESTNG + CUCUMBER + MAVEN + GIT

- ADD CUCUMBER FEATURES FOR DUCUMENTATION

"^I logged into suiteCRM$"
^ = means begining of pattern / step
$ = means end of pattern/step

given I am on google home page

@Given("^I am on google home page$")
pubic void myMethod(){
	# // code that takes you to google page
}

=======================================
if you do it like this : 
	When I post "a","b"
it will create
	(String a, String b)



When I post "Hello From AdmiralCoder"

@When("^I post \"([^\"]*)\"$")
	public void i_post(String arg1) {
	 sysout (arg1)# it will print hello from admiralCoder
	}


what is hooks in Cucumber?

@before
@After annotations/hooks

@Before will run before each Cucumber scenario
@After will run after each Cucumber scenario








































