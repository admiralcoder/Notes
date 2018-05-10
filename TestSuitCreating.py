Creating TESTNG Runner
Web page to get the syntax:

http://testng.org/doc/documentation-main.html#testng-xml


When you create a testng_runner xml we have to pass the standad header


create a new file on the project folder:
										- testng_runner.xml


	- Must always have : always on top of everything else 

		<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >


-------  TestNG HAS:  --------

@Test: smalles unit in testng it is a test method


TestClass:  contains test methods is made of test methos test class must have 
		@Test annotation


Package: contains test classes


Test: contains packages test classes @Test methods


Test suite: contains Tests

===================== Test Suite ====================== 
Project Name PrestaShop.tests.Automation
---------------------------------------------------------------
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="Presta Shop Automation Tests" verbose="2">

	<test name="Search Tests">

		<classes>

			<class name="com.prestashop.tests.search.SearchTest">

				<methods>

					<exclude name="productDetailsTest"></exclude>
					<include name="anotherTest"></include>

				</methods>

			</class>

		</classes>

	</test>

</suite>

---------------------------------------------------------------
"<include name="anotherTest"></include>" will only run the class selected


=============== CREATE SMOKE TEST ===============

You can select a specific package and a class that 
you want to do smoke test either a package and the TestClass
This is the proper way to create a Smoke Test:


<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="Presta Shop Automation Smoke Test" verbose="2">

	<test name="Checkout">

		<packages>

			<package name="com.prestashop.tests.checkout"></package>

		</packages>

	</test>

	<test name="Search">

		<classes>

			<class name="com.prestashop.tests.search.SearchTest"></class>

		</classes>

	</test>

</suite>







=============== CREATE SMOKE TEST option 2 ===============
Location: /PrestashopsTestAutomation/src/com/prestashop/tests/search/SearchTest.java

you add groups = " smoke " this belongs to regression and smoke test


@Test(priority = 1,groups= {"smoke","regression"})
	public void anotherTest() {
		ResultsPage resultsPage = new ResultsPage(driver);
		resultsPage.result(searchQuery).click();
		ProductPage productPage = new ProductPage(driver);
		assertEquals(productPage.name.getText(), searchQuery);
		
	}

================= Smoke test from 2 groups ================
locatioN: /PrestashopsTestAutomation/smoke_test_runner_using_groups.xml

Different packages for the smoke test 


<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="Presta Shop Automation Smoke Test" verbose="2">

	<test name="Search">

		<groups>

			<run>

				<include name="smoke"></include>

			</run>

		</groups>

		<classes>

			<class name="com.prestashop.tests.search.SearchTest"></class>
			
			<class name="com.prestashop.tests.search.ProductDetailsTest"></class>

		</classes>

	</test>

</suite>



























