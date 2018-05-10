WEB DRIVER API SYNCHRONIZATION


++++++++++++++++++++++ Thread.sleep +++++++++++++++++++++++++++++
Thread.sleep ( dont use this) ==> 

SYNCHRONIZATION:

synching the execution of the code with the speed of the browser

	1. thread.sleep

Pauses the execution of the java code does not affect the browser at all


Selenium official documentation discourages of the user of 
thread.sleep

It is not flexible : sometimes we need to wait more or less time. 
Thread.sleep only waits for given amount time.

It makes the execution heavy and slow

@Test
	public void sleep() throws InterruptedException {
		driver.get("http://the-internet.herokuapp.com/dynamic_loading/1");
		driver.findElement(By.tagName("button")).click();
		// pauses the execution of the code
		// it does have nothing to do with the browser
		Thread.sleep(5000);
		String actual = driver.findElement(By.cssSelector("#finish h4")).getText();
		Assert.assertEquals(actual, "Hello World!"); // we are looking for Hello World message
	}



++++++++++++++++++++++ IMPLICITLY WAIT +++++++++++++++++++++++++++++


2. IMPLICITLY WAIT ==> only works with find element method
						By default it is 0 

	driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);


Only applies to findElement/findelements method

if you do it implictly way driver will reatedly try to find the element driver
will stop looking it finds the element before the time given

given returns the element immediately 
driver throw exeption only after the given time runs out

Applies to that instance of the WebDriver object only


it is called twise it will override the previous value 

	driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
	driver.manage().timeouts().implicitlyWait(2, TimeUnit.SECONDS);

Best practice is if you put it on the @BEFOREMETHOD 

@BeforeMethod
	public void setup() {
		System.setProperty("webdriver.chrome.driver", TestConstants.CHROME_PATH);
		driver = new ChromeDriver();
		//waits certain time while finding the element
		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		//
		driver.manage().timeouts().pageLoadTimeout(60, TimeUnit.SECONDS);
	}

@Test
	public void implicitWait() {
		driver.get("http://the-internet.herokuapp.com/dynamic_controls");
		driver.findElement(By.id("btn")).click();
		
		Assert.assertTrue(driver.findElement(By.id("message")).isDisplayed());
		driver.findElement(By.id("message")).getText();
		driver.findElement(By.id("btn")).click();
		
		driver.findElement(By.cssSelector("input#checkbox")).click();
		

	}



+++++++++++++++++++	Explicit WAIT  ++++++++++++++++++++

WebDriverWait --> its a class that lets us wait for certain actions
	
		- wait until element with id "id" becomes visible on page (if page takes long to load)
		- wait until element with id "id" disappears
		- wait until element with id "id" has certain Text
		- wait until element with id "id" becomes clickable

WebDriverWait needs 2 things:
	- 1. element or locator
	- 2. condition

WebDriverWait has 2 constructor arguments: 
	-1. webdriver Object,
	-2. time duration -> it only takes SECONDS

Example:

	wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("#finish h4")));

IT RETURNS ALSO A WEB ELEMENT: you can save it as wel element 

	WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("#finish h4")));
		String actual = element.getText();
		System.out.println("test: "+actual);
		Assert.assertEquals(actual, "Hello World!");

1. wait.until(); --> Starts the wait Actions
2. ExpectedCondition.visibilityOfElementLocated() --> The condition
3. By.cssSelector("#finish h4") --> the locator used to find element

"" purpose of this is to wait until web page element loads ""


timeoutException --> will throw 


	public void waitForVisible() {
		System.setProperty(TestConstants.CHROMEDRIVER, TestConstants.CHROME_PATH);
		WebDriver driver = new ChromeDriver();
		driver.get("http://the-internet.herokuapp.com/dynamic_loading/1");
		driver.findElement(By.tagName("button")).click();
		
		WebDriverWait wait = new WebDriverWait(driver, 5);
		
		// locator By.cssSelector("#finish h4")
		// condition expected condition.visiblilitofelement()
		
		WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("#finish h4")));
		String actual = element.getText();
		System.out.println("test: "+actual);
		Assert.assertEquals(actual, "Hello World!");
		
	}

++++++++++++++++++++++ wait for disappear  ++++++++++++++++++++++

-- will work on web sites where you click and the button is not there then it disappears
 url ===> http://the-internet.herokuapp.com/dynamic_controls

	@Test
	public void waitForDisappear() {
		System.setProperty(TestConstants.CHROMEDRIVER, TestConstants.CHROME_PATH);
		WebDriver driver = new ChromeDriver();
		driver.get("http://the-internet.herokuapp.com/dynamic_controls");
		driver.findElement(By.tagName("button")).click();
		
		WebDriverWait wait = new WebDriverWait(driver, 5);
		//wait for text wait for it to disapear
		//wait until elemen disappears then move on the next line
		Boolean gone = wait.until(ExpectedConditions.invisibilityOfElementLocated(By.xpath("//*[.='Wait for it... ']")));
		assertTrue(gone);
		
		//message that appears once the checkbox disappears
		// will fail since the xpath matches the element that is visible on the page
		gone = wait.until(ExpectedConditions.invisibilityOfElementLocated(By.xpath("//*[.=\"It's gone!\"]")));
		assertTrue(gone);
		
	}


ExpectedConditions.elementToBeclickable() --> does not always work as expected
sometimes returns true as soon as element is visible and active. it does not always handle
the elements blocked by 



++++++++++++++++++++ FluentWaitDemo();++++++++++++++++++++++++++

Wait<WebDriver> wait = new FluentWait<WebDriver>(driver)
				.withTimeout(5, TimeUnit.SECONDS) //customize the timeouts
				.pollingEvery(100, TimeUnit.MILLISECONDS) // control how often selenium will retry the same operation
				.ignoring(NoSuchElementException.class); // import selenium no NoSuchElementException




@Test
	public void FluentWaitDemo() {
		System.setProperty(TestConstants.CHROMEDRIVER, TestConstants.CHROME_PATH);
		WebDriver driver = new ChromeDriver();
		driver.get("http://the-internet.herokuapp.com/dynamic_controls");
		driver.findElement(By.tagName("button")).click();
		
		//FluentWait
		// customize the wait by passing parameter we want. we are using FluentWait to do that
		Wait<WebDriver> wait = new FluentWait<WebDriver>(driver)
				.withTimeout(5, TimeUnit.SECONDS) //customize the timeouts
				.pollingEvery(100, TimeUnit.MILLISECONDS) // control how often selenium will retry the same operation
				.ignoring(NoSuchElementException.class);// pass the exception which will ingnored while trying the same operation
		
		// user the wait to find the element 
		WebElement element = wait.until(new Function<WebDriver, WebElement>(){
			public WebElement apply(WebDriver driver) {
				return driver.findElement(By.id("message"));
			}
		});
		
		assertTrue(element.isDisplayed());
		assertEquals(element.getText(), "It's gone!");

	}




+++++++++++++++++++ JavaScrip Executor +++++++++++++++++++++++++++
-- this will execute a simple command on the window by using JavaScript

//	@Test
	public void sendJSCommand() {
		System.setProperty(TestConstants.CHROMEDRIVER, TestConstants.CHROME_PATH);
		WebDriver driver = new ChromeDriver();
		//using this class we can send javascript commands to the browser
		JavascriptExecutor jsExecutor = (JavascriptExecutor) driver;
		// executeScript performs the command
		// the java script command will be passed as string
		jsExecutor.executeScript("alert ('WARNING')");
//		jsExecutor.executeScript("alert ('hello')");
		
	}



+++++++++++++++++++ Scroll down +++++++++++++++++++++++++++

-- this will Scroll down a page using JavaScrip

	@Test
	public void scroll() throws InterruptedException {
		System.setProperty(TestConstants.CHROMEDRIVER, TestConstants.CHROME_PATH);
		WebDriver driver = new ChromeDriver();
		
		JavascriptExecutor jsExecutor = (JavascriptExecutor) driver;
		driver.get("http://the-internet.herokuapp.com/");
		Thread.sleep(3000);
		WebElement element = driver.findElement(By.linkText("Elemental Selenium"));
		//first parameter: javascript code
		//second parameter: element against which the js code will be executed
		jsExecutor.executeScript("arguments[0].scrollIntoView(true)",	 element);
	}

}


+++++++++++++++++++ Click +++++++++++++++++++++++++++
-- this will click on the bottom of the text where you selected to scroll down by clicking

	@Test
	public void click() throws InterruptedException {
		System.setProperty(TestConstants.CHROMEDRIVER, TestConstants.CHROME_PATH);
		WebDriver driver = new ChromeDriver();
		
		JavascriptExecutor jsExecutor = (JavascriptExecutor) driver;
		driver.get("https://www.amazon.com/");
		Thread.sleep(4000);
		WebElement element = driver.findElement(By.linkText("Privacy Notice"));
		//first parameter: javascript code
		//second parameter: element against which the js code will be executed
		jsExecutor.executeScript("arguments[0].click()",	 element);
	}



















