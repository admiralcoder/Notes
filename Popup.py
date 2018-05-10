WEBDRIVER API

---------------------- POP UP ---------------------

anything that pop up form a browser
alerts, confirmation, dialog

there are 2 types of pop ups:

		1. JavaScript language to write websites
		is not a compiles language
		scripting language
		runs from browser
		2. JavaScript alerts= alerts produced by JavaScript
		looks different on all browser
		blocks out 

	To deal with JavaScript Alerts we can use the alert class from selenium

Alert alert;  = driver.switchto.alert();


driver.switchto.alert(); = returns the alert object currently displayed on the page
this line only works when there is an alert present.
if we call this line when there is an alert we get an exception

+++++++++ EXAMPLE 1 : if you have a pop up with ok button only

	@Test
	public void alertTest() throws InterruptedException {
		driver.get("http://the-internet.herokuapp.com/javascript_alerts");
		Thread.sleep(3000);
		driver.findElement(By.xpath("(//button)[1]")).click();
		Alert alert = driver.switchTo().alert();//capture the alert only works when it will popup
		Thread.sleep(3000);
		alert.accept();// click on the alert
	}



+++++++++ EXAMPLE 2: if you have a pop up with a cancel and ok button
	
	@Test
	public void alertCancel() throws InterruptedException {
		driver.get("http://the-internet.herokuapp.com/javascript_alerts");
		driver.findElement(By.xpath("(//button)[2]")).click();
		Thread.sleep(3000);
		Alert alert = driver.switchTo().alert();//capture the alert only works when it will popup
		Thread.sleep(3000);
		alert.dismiss();// click on the alert
		}


"We have to deal with alerts to be able to continue working on that page otherwise "
"unHnaledALertExeption will be thrown we cannot click anthing on the page if there is an alert"


+++++++++ EXAMPLE 3: if you have a pop up with a Text to fill out 

@Test
	public void alertType() throws InterruptedException {
		driver.get("http://the-internet.herokuapp.com/javascript_alerts");
		driver.findElement(By.xpath("(//button)[3]")).click();
		Thread.sleep(3000);
		Alert alert = driver.switchTo().alert();//capture the alert only works when it will popup
		Thread.sleep(3000);
		System.out.println(alert.getText());
		alert.sendKeys("hii");// click on the alert enter information
		System.out.println(alert.getText());
		alert.accept();
	}


"alert object can only be used when there"



+++++++++ EXAMPLE 4: if throws exception 


@Test
	public void test() throws InterruptedException {
	// Start Testing
		try {
			driver.switchTo().alert().dismiss();
		} catch (NoAlertPresentException e) {
			e.printStackTrace();
		}
	}
	// continue testing if you see no alert




======================== BROWSER POP UPS =========================

-

@Test
	public void acceptBrowserPopup() throws InterruptedException {
		driver.get("https://www.primefaces.org/showcase/ui/overlay/confirmDialog.xhtml");
		WebElement button= driver.findElement(By.cssSelector("button[type='submit']"));
		button.click();
		WebElement no = driver.findElement(By.xpath("//span[.='No']"));
		no.click();
		
		button.click();
		
		WebElement x = driver.findElement(By.xpath("//span[@class='ui-icon ui-icon-closethick']"));
		Thread.sleep(3000);
		x.click();

	}

======================== IFRAME html page into another =========================

	Iframe
	frames are used to embed on html page into another google maps inside travel websites is one EXAMPLE
	if the page has two html pages embedded  each html document is known as a frames


	WEBDRIVER controls one html at a time
	if we want to control another html page

iFrame --> this is a tag that is used to put one html document inside another. selenium cannot see 
what inside a iframe. i frame represents that second embedded page we need to switch 
to iFrame


driver.switchTo().frame() used to jump from frame to frame
driver.switchTo().parentFrame(); used to jump to parent frame 

++++++++++++++++++ search inside frame

//	@Test
	public void test() throws InterruptedException {
		driver.get("http://the-internet.herokuapp.com/iframe");
		//1. we have to find the iFrame
		//2. call driver.switch.frame method by passing the iframe
		WebElement iframe = driver.findElement(By.tagName("iframe"));
		driver.switchTo().frame(iframe);
		driver.findElement(By.id("tinymce")).clear();
		driver.findElement(By.id("tinymce")).sendKeys("more text");
		
		driver.switchTo().parentFrame();
		
		System.out.println(driver.findElement(By.linkText("Elemental Selenium")));

	}

++++++++++++++++++ search inside frame get out and verify if text is there
	
//	@Test
	public void test2() throws InterruptedException {
		driver.get("http://the-internet.herokuapp.com/iframe");
		//we can also switch to iframes by passing the name or ID directly
		driver.switchTo().frame("mce_0_ifr");
		driver.findElement(By.id("tinymce")).clear();
		driver.findElement(By.id("tinymce")).sendKeys("more text");
		
		driver.switchTo().parentFrame();
		
		System.out.println(driver.findElement(By.linkText("Elemental Selenium")));

	}

++++++++++++++++++ search inside frame get out and verify if text is there
	
	@Test
	public void test3() throws InterruptedException {
		driver.get("http://the-internet.herokuapp.com/iframe");
		//switch by count 
		driver.switchTo().frame(0);
		driver.findElement(By.id("tinymce")).clear();
		driver.findElement(By.id("tinymce")).sendKeys("more text");
		
		driver.switchTo().parentFrame();
		
		System.out.println(driver.findElement(By.linkText("Elemental Selenium")));

	}


when we get no suchelement exception
	



======================== MUlTIPLE tabs/WINDOWS =========================



for selenium  tab = window

selenium can control one tab at a time
when we open up page with selenium, that window is the default window.

if we open tother pages windwos tab we hae to swtich to them explicitly selenium
by default con not see the new tabs


String handle= driver.getWindowHandle();// every time windows open a browser it 
				gives them ID that gets saved on handle name. 


getWindowHandle(); returns a set of window handles all the open windows
in order to switch to another window tab we need to know the window handle of that window

	@Test
	public void test() throws InterruptedException {
		String handle= driver.getWindowHandle();
		System.out.println(handle);
		System.out.println(driver.getTitle());
		System.out.println(driver.getCurrentUrl());
		
		driver.findElement(By.linkText("Click Here")).click();
		
		String newWindowHandle = "";
		Set<String> windowHandles = new HashSet();
		windowHandles= driver.getWindowHandles();
		
		for (String string : windowHandles) {
			System.out.println(string );
			if(!string.equals(handle)) {
				newWindowHandle=string;
			}
		}
		
		driver.switchTo().window(newWindowHandle);
		
		Thread.sleep(3000);
		System.out.println(driver.findElement(By.tagName("h3")).getText());
		System.out.println(driver.getTitle());
		System.out.println(driver.getCurrentUrl());
	}





+++++++ DRIVER.close 

driver.close(); ==> closes the current tab
driver.quit(); ==> closes all tabs



















