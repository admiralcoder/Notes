Selenium WebDriver Class: PAGE OBJECT MODEL

Tools that are used around Selenium: Maven, Cucumber, Git, Jenkins..

Java part --> Collections Framework, Excel Automation, JDBC, RestAssure

AUT => Application Under Test



FrontEnd => Graphic User Interphase what ever user sees	in browser

		-> can manually be tested
		-> Automation test -> Selenium WebDriver with Java
		-> UFT + VBScript (other tools)
		-> 	Watir + Ruby etc. (Other Tools)


BackEnd -> DataBase -> JDBC in JAVA
		-> API level -> RestAssure library in Java


		-> Manual Test
		-> DataBase -> sql developer
		-> API level -> PostMan

++++= Full Stack Automation. <- name of the title of this FrontEnd BackEnd

=================== PAGE OBJECT MODEL =============================

The way you write selenium code will change 

- POM = PAGE OBJECT MODEL
		-> most populat framework designs


EPIC > User Stories > Test Cases


What kind of Test cases?
	When you write test cases you cover different scenarios
	Scenarios.

	Positive
	Negative
	Boundary value analysis




User Stories = can have multiple user Stories

Test Cases = can have multiple test Cases




RTM: requirement tracebility matrix

Mapping Test cases with user story


==========================================================

Steps to automate it?

1: Learn the functionality
	-> Read Documents
	-> have a KT knowledge transfer session with BA 
	-> Ask team mates developer etc

2: Manually Test it.
	-> Go over each Step and test it manually and make sure you understand
	and test each step properly understand expect expect results.
	-> Make sure everything looks good / when expected behavior is matching 
	actual behavior

3: Automate it:  




================== PAGE OBJECT MODEL POM ==================


Page Object Model in selenium:

	- its a design pattern
		-> when you write code you follow certain pattern so that it is easier to maintain 
		and write / reuse code many design pattern in JAVA
			-> 1: Singleton pattern
			-> 2: Factory pattern etc

Selenium Web Driver supports POM Design pattern
-----------------------------------------------------------------------------------------
		-> we Create a separate java class for each page in AUT(application Under Test).

			-> home page in AUT -> public class Homepage{}
			-> Login PAge in AUT -> public class LoginPage{}
			-> Account page in AUT-> public clasa Accountpage{}
-----------------------------------------------------------------------------------------
		-> Each htmlelement on the page of AUT will be variable in page java class

			-> public class Homepage{
					public WebElement Signin{}
					Public WebElement Logo{}

			}
------------------------------------PAGE CLASS will contain element ----------------------

			-> Each Action to be performed on that page of AUT will be a 
			method in java page class 

			public class LoginPage{
					@findBy(id="email")
					public WebElement email{}
					Public WebElement password{}
					public webelement signinbutton{}

					public void SetEmail(String email){
					email.sendKeys(email);
					}

					public void enterCredentials(String email, String password){
					email.sendkeys(email);
					password.sendkeys(password);
					}
			}

-----------------------------------------------------------------------------------------
Example 1: of a test for AUT 

			@Test
			public void loginPAge(){
				loginpage loginpage = new loginpage();
				loginpage.entercredentials("djale2008@gmail.com","abcde");

			}

-----------------------------------------------------------------------------------------
Example 2: this 2 options do the same thing

		1:	WebElement email = driver.findelement(By.id"email");
			email.sendkeys("djale2008@gmail.com");

		2:	@FindBy (id="email");						--
			public WebElement email;					  | from today we will use 

			email.sendKeys("djale2008@gmail.com");		__| this method 


This code will not work by it self we need to ask selenium to load coade and 
initialize elements in the page and make it available for use


1: we need to add a constructor that accepts a webdriver
2: use pagefactory class




-----------------------------------------------------------------------------------------

PageFactory.initElements(driver, this);  ==> will initialize and load WebElements defined on 
										the page class and make it visible for our driver.

LOGO in a webSite:

<img class="logo img-responsive" 
src="http://automationpractice.com/img/logo.jpg" 
alt="My Store" width="350" height="99">

http://automationpractice.com/index.php

search by xpath for logo in website  name

@FindBy(xpath= //img[@class='logo img-responsive'])


===================== we dont put assert @test cases here only paths ======================


public class HomePage {
	private WebDriver driver;
	
	public HomePage(WebDriver driver) {
		this.driver=driver;
		PageFactory.initElements(driver, this);
	}
	
	@FindBy(linkText="Sign in")   //finds the element replaces driver.findelement(By.path)
	public WebElement signInLink;
	
	@FindBy(xpath= "//img[@class='logo img-responsive']")
	public WebElement logo;
	
	public boolean isAt() {
		return driver.getTitle().equals("My Store");
	}
	
	public void gotologinPage() {
		signInLink.click();
	}
	
}


public class LogInPage {

	private WebDriver driver;
	
	public LogInPage(WebDriver driver) {
		this.driver=driver;
		PageFactory.initElements(driver, this);
	}
	@FindBy(xpath="//h3[.='Create an account']")
	public WebElement CreateAccountLabel;
	
	@FindBy(xpath="//h3[.='Already registered?']")
	public WebElement alreadyRegisterLabel;

	public boolean isat() {
		return driver.getTitle().equals("Login - My Store");
	}

}




===================== We @test in a different class   ======================





public class LogInTests {
	WebDriver driver;
	
	
	@BeforeClass
	public void setUp() {
		System.setProperty(Configuration1.getProperty("webdriver"), Configuration1.getProperty("driverpath"));
		driver=new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		driver.get(Configuration1.getProperty("url"));
	}
	
	@Test
	public void positiveLoginTest() {
		HomePage homepage= new HomePage(driver);
		// verify home page
		assertTrue(homepage.isAt());
		// verify logo is displayed
		assertTrue(homepage.logo.isDisplayed());
		
		homepage.gotologinPage();
		
		LogInPage loginpage = new LogInPage(driver);
		//verify if login is there
		assertTrue(loginpage.isat());
		//verify if log is displayed
		assertTrue(loginpage.CreateAccountLabel.isDisplayed());
		assertTrue(loginpage.alreadyRegisterLabel.isDisplayed());
		
		//enter valid email and password then click sign in 
		loginpage.EmailField.sendKeys(Configuration1.getProperty("username"));
		loginpage.PasswordField.sendKeys(Configuration1.getProperty("password"));
		loginpage.submitSignIn.click();
		
		
	}

}




===================== Configuration Text file created  ======================

url=http://automationpractice.com/index.php
username=djale2008@gmail.com
password=abcdef
driverpath=/Users/arod/Documents/selenium dependencies/drivers/chromedriver
webdriver=webdriver.chrome.driver




============ Configuration1 class created inside package  ================



public class Configuration1 {
		
		private static Properties properties;
		public static final String CHROMEDRIVER="webdriver.chrome.driver";
		
		static{
			try {
				properties = new Properties();
				FileInputStream inputStream = new FileInputStream("./configuration.properties");
				properties.load(inputStream);
				
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		public static String getProperty(String key){
			return properties.getProperty(key);
		}
	}








1: learn the functionality
2: 
3: automate it: 
	1: create classes for each page that is involved in the test if not already created
	2: add elements
	3: add necessary methods 
	4: create testNG test and user my page objects along with all assertions

=============================================================================================


Next Class

@FindBys
AND logic
@FindAll
OR logic











