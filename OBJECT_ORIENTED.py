Naming Packages

com.prestashop
	pages
	tests
	utilities


	Naming Packages
		Top level is always the project or the product we are working on


		Example : for a web site

		uscis.gov --> gov.uscio

		mit.edu ----> edu.mit.apply



Search test1 open the prestashop application 
search for "printed summer dress"
verify a result for "printed summer dress" is displayed


------------------------ PAGE OJECT MODEL ------------------------

=THIS IS WHAT MAKES A PAGE OBJECT CLASS OTHERWISE IT WONT BE A PAGE
OBJECT =

private WebDriver driver;
	
	public ResultsPage(WebDriver driver) {
		this.driver=driver;
		PageFactory.initElements(driver, this);
	}



 
 method that takes name of product and returns element 

 like print summer dress it should print the result



 ++++++++++++++++++ EXAMPLE FOR OBJECT MODEL TEST +++++++++++++
 ----- project name in selenium Automation Practice POM -----


package com.prestashop.tests;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.prestashop.pages.HomePage;
import com.prestashop.pages.ProductPage;
import com.prestashop.pages.ResultsPage;
import com.prestashop.utilities.Configuration1;

public class SearchTest {

WebDriver driver;
String searchQuery = "Printed Chiffon Dress";//we can declare a variable here as well and 
											//this will  be used later
	
	@BeforeClass
	public void setUp() {
		System.setProperty(Configuration1.getProperty("webdriver"), Configuration1.getProperty("driverpath"));
		driver=new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		driver.get(Configuration1.getProperty("url"));
	}
	/*
	 * open the prestashop application
	 * search for printed summer dress
	 * verify a result printed summer dress is displayed
	 */
	
	@Test(priority = 0)
	public void positiveLoginTest() {
		
		HomePage homePage = new HomePage(driver);
		homePage.search_query.sendKeys(searchQuery+Keys.ENTER);
		ResultsPage resultsPage = new ResultsPage(driver	);
		assertTrue(resultsPage.result(searchQuery).isDisplayed());
	}
	/*
	 * on the search result page click on a result for "Printed Summer Dress"
	 * is displayed
	 * verify that product name is displayed correctly in the products page
	 */
	
	@Test(priority = 1)
	public void productDetailsTest() {
		ResultsPage resultsPage = new ResultsPage(driver);
		resultsPage.result(searchQuery).click();
		ProductPage productPage = new ProductPage(driver);
		assertEquals(productPage.name.getText(), searchQuery);
		
	}
}



+++++++++++IMPORTANT++ WEBDRIVER WAIT METHOD +++++++++++++++++

WebDriverWait wait= new WebDriverWait(driver, 3);
wait.until(ExpectedConditions.visibilityOf(productPage.confirmation));

"this will give it a wait time when you cant get the confirmation on a test"

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


==== example 2 Productcheckouttest on class AutomationpracticePOM =====

package com.prestashop.tests;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import com.prestashop.pages.HomePage;
import com.prestashop.pages.ProductPage;
import com.prestashop.utilities.Configuration1;

public class ProductCheckOutTest {

	WebDriver driver;
	String ProductName = "Printed Summer Dress";//we can declare a variable here as well and 
												//this will  be used later
		@BeforeClass
		public void setUp() {
			System.setProperty(Configuration1.getProperty("webdriver"), Configuration1.getProperty("driverpath"));
			driver=new ChromeDriver();
			driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
			driver.get(Configuration1.getProperty("url"));
		}
	/*
	 * open prestashop
	 * click on product printer summer dress on home page
	 * verify product name is printed summer dress
	 */
		@Test(priority = 0)
		public void productListing() {
			HomePage homePage = new HomePage(driver);
			homePage.listing(ProductName).click();
			ProductPage productPage = new ProductPage(driver);
			assertEquals(productPage.name.getText(), ProductName);
		}
		/*
		 * open product details page, add a product to the cart
		 * verify that confirmation message is displayed
		 */
		@Test(priority = 1)
		public void checkoutTest() {
			ProductPage productPage = new ProductPage(driver);
			productPage.addToCart.click();
			//Explicit wait
			WebDriverWait wait= new WebDriverWait(driver, 3);
			wait.until(ExpectedConditions.visibilityOf(productPage.confirmation));
			
			assertTrue(productPage.confirmation.isDisplayed(),"Confirmation message was not displayed");
			String confirmation= "Product successfully added to your shopping cart";
			assertEquals(productPage.confirmation.getText(), confirmation);
		}
	
}



============== Depends ON PRODUCT LISTING =====================

@Test(priority = 0)
		public void productListing() {
			HomePage homePage = new HomePage(driver);
			homePage.listing(ProductName).click();
			ProductPage productPage = new ProductPage(driver);
			assertEquals(productPage.name.getText(), ProductName);
		}
		/*
		 * open product details page, add a product to the cart
		 * verify that confirmation message is displayed
		 */

@Test(priority = 1,dependsOnMethods="productListing")
		public void checkoutTest() {
			ProductPage productPage = new ProductPage(driver);
			productPage.addToCart.click();
			//Explicit wait so that it can pass
			WebDriverWait wait= new WebDriverWait(driver, 3);
			wait.until(ExpectedConditions.visibilityOf(productPage.confirmation));
			
			assertTrue(productPage.confirmation.isDisplayed(),"Confirmation message was not displayed");
			String confirmation= "Product successfully added to your shopping cart";
			assertEquals(productPage.confirmation.getText(), confirmation);
		}


@Test(priority = 0)

@Test(priority = 1,dependsOnMethods="productListing") --> this depends on 
														test 1 if test 1 
														fails then the SECOND
														test fails as well


@Test(priority = 0,enabled = false) --> this will not run at all its like
										un-commenting a message this test
										will be skiped same as doing // this
										







