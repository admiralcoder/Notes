How to configure variables



"Project"
	|
	-->Package
			|
			-->Class
			|
			-->Class


"Project" home folder --> the folder where the Projectis created
top level of the Project

---- FULL PATH LOCATION ==> /Users/arod/eclipse-workspace/UI-Functional-Tests

Create file in the Project home folder

Naming the file =>		Configuration.properties





properties file 
--> A file whos extensionis properties 
	this file is used to store the project level configurationsettings
	very important information is saved in properties file.
	example:
			Log in information certain path can be stored in configuration file.
			(in addition to other information)


All values in te config file are saved in key and value format

Example:

Username = Tester

Username -> key

Tester   -> Value of the key Username

-------------------   configuration vs constants -------------------

constants = we put values that we dont change, whetever in constants is usually related to
			the code

			Example: located in UI-Functional-Tests com.utilities

			public static final String CHROME_PATH="/Users/arod/Documents/selenium dependencies/drivers/chromedriver";
	
			public static final String WO_ORDERS_URL = "http://secure.smartbearsoftware.com/samples/testcomplete12/WebOrders/login.aspx";
	

Values that are project level and we want to change easily are saved in configuration file.

confi
