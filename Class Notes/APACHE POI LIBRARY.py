APACHE POI LIBRARY

For data driven testing sometimes data will be stored in excel files
and we need to programatically read data form excel and input to out
application


good example for data driven testing
	google translate
		- you enter Hello and you should be able to verify that
		it translates in many languages. 



how to compare 2 excel sheets

store all excel file1 into a java data structure

store all excel file2 into a java data structure

then compare data structure


Friday: launch a person Amazon AWS EC2 Machine
		Install Oracle 11G Express to it
		install sql developer into local Machine
		connect to Database in Amazon EC2 Could server

Windows Server 2012 AWS Cloud EC2 Machine

1: Deployed oracle database
		-> sql programaming 
2: then we will use it for API Deployment 
		api testing and automation

3: Selenium Grid 


------------------------------------------------------------------

++ Interview Questions?

-"when do you do Data Driven Testing"

when a module in my application requires testing with multiple sets of 
data then we need to do data driven testing

while doing data driven testing code and test data will be separated
test data will be stored and fed to code form excel files or any 
other external source. 

Data Drives the test code must be smart enough to find out how many
sets of data we need to test with . and pass those to application

We write code once and afterwards keep working with data depending
on what we want to test.

-"where else i need to use excel read/write"
1: Data Driven testing where we store our test data into excel
2: excel reports testing
	Application had a page where all current market prices are loading
	and there was a download ICON on top
	When you click that download icon it downloads excel report contatining
	data on the page

	- how to test?
	you read all the data on the webtable into a data structure then read all the data in excel
	report into similar data structure

	- Compare them.


-"Reports comparison"?
	
	Data Migration:
				Data application was being updated along with database
				old application database had sybase
				new application database had oracle

	Developers wrote code to generate excel files from both databases

	our code would take excelfile with old database data
	and compare with new excelfile with new database data

	--- end result was comparing excel vs excel files ---
































































