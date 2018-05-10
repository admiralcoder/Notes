Interview Preparation 
04/17/2018

---------- DAY 1

US COURTS  cucumber Selenium Framework courthouse


-Enviroment

Local -> Developement -> testing -> staging -> production 

-"developer"
Local Enviroment = developer write code and test it locally

-"developer"
Developement Enviroment = less stable compared to test Enviroment
						- Unit testing happens here 
						- developers do some whitebox testing 

testing Enviroment = more stable the Developement
					- manual testing is done
					- integration test is run
					- automated smoke test are run here ( every day )
					- Also knows as QA Enviroment

Staging Enviroment = final testing before release is done here
					- Outside users can test the application in this Enviroment
					- automated regression test can be run here ( its good if something
						changes on a daily basis )


on " Unit test & deploy changes to server "
Done by jenkins automatically every time developer checks in a new code
only done by developers

2023615117 - Marouf

04/18/2018
---------- DAY 2 

when do we run automated tests?

development Enviroment 			deploye changes			test Enviroment

automation engeneer starts								
working on feature


++++++  Challenges : On our current project we had a create tab already and new requirement was 
			that a delete buttom should be incorporated next to create tab in order to 
			create my feature file i had to wait for developer to be done with this requirement

================================ SMOKE TEST ===================================

SMOKE TEST: Runs against the test Enviroment
			To know wheather enviroment is up 
			Run every day
			Run every time changes are deployed to test enviroment
			Smoke test can also run against development enviroment 

			EXAMPLE: Once a day
					 1 feature file --> 3 scenario ---> 20 minutes





================================ REGRESSION TEST ===================================


REGRESSION TEST: Should be running before every release
				 To find out if new changes resulted in a bug
				 Runs less frequently than smoke test
				 Runs After major bug fixes and for every release
				 Runs against the UAT

				 Example: 350 feature files on a regression 
				 		  1000-1050 scenarios 
				 		  12 hours

				 Scenario: 
				 		GIVEN i log in to suiteCRM
				 		WHEN i search for "john"
				 		THEN link for user "john" should be display
				 		And the rest of the application should work



======================== TEAM COMPOSITION ===================================

Marouf TEAM :

			DEVELOPER 			 		6
			AUTOMATION ENGINEERS 		2
			MANUAL TEST 				4
			BA 							1
			PRODUCT OWNER				1
			SUBJECT MATTER EXPERT (SME)	1(PART TIME PERSON THAT KNOW ABOUT REGULATION RULES ETC)


 
==============================================================================

Smoke test

if smoke tests are executed once a day they can be longer for example we can have smoke tests that runs 
every morning at 6am this test have 5-10 test cases the whole run takes 20 minutes


regression:


number of features files 350
number of scenarios:  < 1100

duration of execution 12 hours

when i run regression test : 1 before release
							 2 after major bug fixes
							 3 after major new functionality


pass criteria: 90 percent pass rate with no major critical




=========================== AUTOMATION Framework ====================

TOOLS 

	eclipse
	java
	maven
	cucumber
	webdriver 3
	testNG ----> unit testing TOOL

Design

	Page Object Model - > 

Data Driven testing
	
	Cucumber outline
	excel

Back End Testing 
	
	JDBC -> 


Whats a test?

	Feature file -> step definition -> Page Objects -> hooks common Webdriver Utility Classes


Code Stored on Git -> check out from GIT -> run tests -> enviroment email


*** VERSION 1 ( BAD ARCHITECTURE ) **** Jenkins Architecture where things happen? *****

Jenkins --> installed in aws machine

code 	--> Git

jenkins checks out the code aws machine where the jenkins is installed
jenkins runs the test by passing a maven command
	The tests are executed in the same machine that means the browser 
	will open in the same machine where the code and check out 
	and running 

after the test execution, HTML cucumber reports are generated and results
are email( do not say Json report)


*** VERSION 2 ( good  ARCHITECTURE ) **** Jenkins Architecture where things happen? *****

Jenkins --> installed in aws machine

code 	--> Git

jenkins checks out the code aws machine where the jenkins is installed
jenkins runs the test by passing a maven command
	The tests are executed in the same machine that means the browser 
	will not open in the same machine where the code and check out 
	and running 

after the test execution, HTML cucumber reports are generated and results
are email( do not say Json report)

Jenkins should only run the job doesnt execute web browser ???????????????




=============================================================================================


TEAM COMPOSITION -1

7 People ( ok but preferable 9 )
		1 Scrum master
		1 Product OWNER
		1 Business Analyst
		3 developers
		1 manual 
		1 automation


TEAM COMPOSITION -2
9 People
		1 scrum master
		1 Product OWNER
		1 Business Analyst
		3 developers
		2 manual testers
		1 automation

------------------------------------------

	My Role in the TEAM


		1 automate the current spring stories
			- automate the feature files in a sprint
		2 maintain the smoke test (   )
			- check the results
			- fix code related errors
			- report bugs found
		3 Maintain the regression test
			1. once a sprint i run all the. test cases related to the 
			   current component we are working 
			2. When we actually did regression testing 
					- check the results
					- fix code related errors
					- report bugs found

Prestashop has 
ususally we work a certain component of the application for several sprints. examples for components are:
		registration
		search 
		buy 
		list

======= DESCRIBE your DAY ========

	starts with the smoke test results
		if passing ... continue

		else 
			check the results 
					read the logs what is the exception see where (Which feature file, class, method)
					was the failure look at the screenshots
					manually try to reproduce the issue

					if i find the bug report to the team if the bug has a high severity i email
					the team immediately. server enviroment application is down
					log in does not work
					can not pay while checking out
					if  the bug is not very high priority i mention it in the stand up meeting

					if the failure is not a bug but just a code issue fix the issue in my code
					issue fix the issue in my code. for example xpath that used to work before stop 
					working

					Once i am done with smoke test I work on automating sprint stories
						1: If I was working on a certain story yesterday i just continue working on that
						story i look at jira if i forget what i am working on. Jira shows which story is assigned
						to me and in progress
						2: If am not working on any story i go to Jira and start working on the next 
						available story, I pick a story and move to in progress column sometime stories are already
						assigned and I just moved to in progress


					10:30 am stand up meeting: every one in the team

THINGS THAT DONT HAPPEN EVERY DAY?

					I am sometimes pulled in to helping other tests engineers from other teams
					I also participate on all the agile ceremonies sprint related meetings
					I also particiapte the non agile /other meetings: montly all hand meetings: montly 
					all hands meetinsg training ( securiry comapny culture) we had to retake every year 
					Every now and then we have some companies demoing new products 
					microsoft came to show off their cloud solution: AZURE



CHALLENGES 



ACHIEVEMENTS




definition of done?

			story
			how do i know vertan functionality is ready?
				write code
				unit test
				review
				test manual
				auto test





Challenges
	Ajax: heavy application

		When the application is doing some operation it is always running 
		some java script. calls in backgound when i tried to 
		any selenium operation. I alaways got stalleedelement exception
		1: I had to write method which used javascript
		it waited until all javascript processes were finishes in the browser
		2: i had to use explicit waits extensively i wrote a very big library
		for explicit waits.

		overload example: i had to wait until element become clickable so i used
						a lot of 
						waitforvisible(webElement)
						waitforvisible(by)
						waitforvisible(webElement)

		3: UI block element: its a web element that sohws that the page is loading 
						it disapears after the page is done loading. BUt before it
						disappears completely it stays on the page without being
						visible(not visible because it is transparent).
						since it is on the was blocking every element on the page

							resolved by: I wrote a method that waited for it to disappears

							While(there is a count < 10)
									try
										find element
										wait time
										count ++
									catch
										not found exception 
		




























































































