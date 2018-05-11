HOOKS

for cucumber a scenario is everything hooks 


@After hook always runs, it does not care weather the scenario
 pass or fail



		features="src/test/resources/features/",
		glue="com/app/step_definitions", 
		dryRun = false  // you set it to true if you wanna do dry run. // false if you want run test
		)

features: is the package name the location of the cucumber file

glue: 

tags=""; --> is used when you wanna run a single scenario when i run 
			cukes runner


tas are used to target certain scenario or feaure file to run
when we have a tag in the cuckesrunner only that tag will run everything else
will be ignored

if we dont provide any tags cucumber will run all the tests
in the shows features action

when we put tag on a secenario it applies to that scenario only

when we put the tag on top of the feature file it applies 

plugin = "pretty" --> add logs for more information about
			what is running it also tells us what passed and failed

--------------------------------------------------------------

"html:target/cucumber-report" --> This will generate HTML reports and it will be at html : and location is target/cucumber-report
If it doesn't exist it will create 1 and the reports will be there































